import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from backend.server import create_server


class CagIntegrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = create_server(port=0)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def url(self, path):
        return f"http://127.0.0.1:{self.port}{path}"

    def get_json(self, path):
        try:
            with urlopen(self.url(path), timeout=5) as response:
                return response.status, json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            body = json.loads(error.read().decode("utf-8"))
            error.close()
            return error.code, body

    def post_json(self, path, payload):
        request = Request(
            self.url(path),
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=5) as response:
                return response.status, json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            body = json.loads(error.read().decode("utf-8"))
            error.close()
            return error.code, body

    def test_overwrite_context_key_via_api(self):
        self.post_json("/api/context", {"user_id": "overwrite_user", "key": "lang", "value": "en"})
        status, body = self.post_json(
            "/api/context", {"user_id": "overwrite_user", "key": "lang", "value": "es"}
        )
        self.assertEqual(status, 201)
        self.assertTrue(body["saved"])
        status2, body2 = self.get_json("/api/context?user_id=overwrite_user")
        self.assertEqual(len(body2["context"]), 1)
        self.assertEqual(body2["context"][0], {"key": "lang", "value": "es"})

    def test_context_isolated_per_user(self):
        self.post_json("/api/context", {"user_id": "user_a", "key": "pref", "value": "A"})
        self.post_json("/api/context", {"user_id": "user_b", "key": "pref", "value": "B"})
        _, body_a = self.get_json("/api/context?user_id=user_a")
        _, body_b = self.get_json("/api/context?user_id=user_b")
        self.assertEqual(body_a["context"][0]["value"], "A")
        self.assertEqual(body_b["context"][0]["value"], "B")

    def test_ask_without_context_returns_empty_context_used(self):
        status, body = self.post_json(
            "/api/ask", {"user_id": "no_ctx_user", "question": "Que es RAG?"}
        )
        self.assertEqual(status, 200)
        self.assertEqual(body["context_used"], [])

    def test_ask_with_multiple_context_items(self):
        self.post_json(
            "/api/context", {"user_id": "multi_ctx", "key": "audience", "value": "principiante"}
        )
        self.post_json(
            "/api/context", {"user_id": "multi_ctx", "key": "tone", "value": "casual"}
        )
        status, body = self.post_json(
            "/api/ask", {"user_id": "multi_ctx", "question": "Que es CAG?"}
        )
        self.assertEqual(status, 200)
        self.assertIn("principiante", body["answer"].lower())
        self.assertIn("audience", body["context_used"])
        self.assertIn("tone", body["context_used"])

    def test_ask_returns_answer_with_sources(self):
        status, body = self.post_json(
            "/api/ask", {"user_id": "sources_test", "question": "Que es RAG?"}
        )
        self.assertEqual(status, 200)
        self.assertIn("RAG", body["answer"])
        self.assertIn("rag", body["sources"])

    def test_context_after_ask_is_persistent(self):
        self.post_json(
            "/api/context", {"user_id": "persist_ctx", "key": "audience", "value": "principiante"}
        )
        self.post_json("/api/ask", {"user_id": "persist_ctx", "question": "Que es CAG?"})
        _, ctx = self.get_json("/api/context?user_id=persist_ctx")
        self.assertEqual(len(ctx["context"]), 1)
        self.assertEqual(ctx["context"][0]["key"], "audience")

    def test_health_endpoint(self):
        status, body = self.get_json("/health")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "ok")

    def test_get_context_missing_user_id(self):
        status, body = self.get_json("/api/context")
        self.assertEqual(status, 400)
        self.assertIn("error", body)

    def test_post_context_missing_key(self):
        status, body = self.post_json("/api/context", {"user_id": "test", "key": "", "value": "v"})
        self.assertEqual(status, 400)

    def test_post_ask_missing_question(self):
        request = Request(
            self.url("/api/ask"),
            data=json.dumps({"user_id": "test"}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with self.assertRaises(HTTPError) as error:
            with urlopen(request, timeout=5):
                pass
        self.assertEqual(error.exception.code, 400)
        error.exception.close()


if __name__ == "__main__":
    unittest.main()
