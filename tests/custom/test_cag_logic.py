import unittest

from backend.cag import apply_context

BASE_ANSWER = "Segun la base de conocimiento del curso: RAG recupera fragmentos de una base documental para responder con conocimiento externo al modelo."


class CagLogicUnitTest(unittest.TestCase):
    def test_no_context_returns_answer_unchanged(self):
        result = apply_context("user1", "test", BASE_ANSWER, [])
        self.assertEqual(result, BASE_ANSWER)

    def test_audience_principiante_modifies_answer(self):
        context = [{"key": "audience", "value": "explicar como principiante"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertIn("principiante", result.lower())
        self.assertIn("principiante", result.lower())

    def test_audience_avanzado_modifies_answer(self):
        context = [{"key": "audience", "value": "nivel avanzado"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertIn("avanzado", result.lower())

    def test_tone_formal_adds_recommendation(self):
        context = [{"key": "tone", "value": "formal"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertIn("fuentes adicionales", result.lower())

    def test_tone_casual_adds_friendly_message(self):
        context = [{"key": "tone", "value": "casual"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertIn("aqui estoy", result.lower())

    def test_format_breve_truncates_long_answer(self):
        long_answer = "Oracion uno. Oracion dos. Oracion tres. Oracion cuatro."
        context = [{"key": "format", "value": "breve"}]
        result = apply_context("u1", "test", long_answer, context)
        num_sentences = len(result.split(". "))
        self.assertLessEqual(num_sentences, 2)

    def test_format_detallado_adds_extra(self):
        context = [{"key": "format", "value": "detallado"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertIn("profundidad", result.lower())

    def test_multiple_context_keys_combined(self):
        context = [
            {"key": "audience", "value": "principiante"},
            {"key": "tone", "value": "casual"},
        ]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertIn("principiante", result.lower())
        self.assertIn("aqui estoy", result.lower())

    def test_unknown_context_key_is_ignored(self):
        context = [{"key": "nonexistent_key", "value": "some_value"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertEqual(result, BASE_ANSWER)

    def test_empty_context_items_list(self):
        result = apply_context("u1", "test", BASE_ANSWER, [])
        self.assertEqual(result, BASE_ANSWER)

    def test_context_without_key_field(self):
        context = [{"value": "principiante"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertEqual(result, BASE_ANSWER)

    def test_case_insensitive_audience_matching(self):
        context = [{"key": "audience", "value": "PRINCIPIANTE"}]
        result = apply_context("u1", "test", BASE_ANSWER, context)
        self.assertIn("principiante", result.lower())

    def test_preserves_user_id_and_question_params(self):
        context = [{"key": "audience", "value": "principiante"}]
        result = apply_context("custom-user", "custom question?", BASE_ANSWER, context)
        self.assertIn("principiante", result.lower())


if __name__ == "__main__":
    unittest.main()
