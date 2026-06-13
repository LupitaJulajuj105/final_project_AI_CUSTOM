import unittest

from backend.context_store import ContextStore


class ContextStoreUnitTest(unittest.TestCase):
    def setUp(self):
        self.store = ContextStore()

    def test_save_and_list_for_user(self):
        self.store.save("user1", "key1", "value1")
        items = self.store.list_for_user("user1")
        self.assertIn({"key": "key1", "value": "value1"}, items)

    def test_save_multiple_keys_for_user(self):
        self.store.save("user1", "color", "azul")
        self.store.save("user1", "idioma", "es")
        items = self.store.list_for_user("user1")
        self.assertEqual(len(items), 2)
        self.assertIn({"key": "color", "value": "azul"}, items)
        self.assertIn({"key": "idioma", "value": "es"}, items)

    def test_save_overwrites_existing_key(self):
        self.store.save("user1", "theme", "dark")
        self.store.save("user1", "theme", "light")
        items = self.store.list_for_user("user1")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], {"key": "theme", "value": "light"})

    def test_list_for_unknown_user_returns_empty(self):
        items = self.store.list_for_user("nonexistent")
        self.assertEqual(items, [])

    def test_users_are_isolated(self):
        self.store.save("alice", "lang", "en")
        self.store.save("bob", "lang", "es")
        alice_items = self.store.list_for_user("alice")
        bob_items = self.store.list_for_user("bob")
        self.assertEqual(alice_items, [{"key": "lang", "value": "en"}])
        self.assertEqual(bob_items, [{"key": "lang", "value": "es"}])

    def test_save_returns_true(self):
        result = self.store.save("user1", "k", "v")
        self.assertTrue(result)

    def test_empty_context_returns_empty_list(self):
        self.store.save("user1", "k", "v")
        items = self.store.list_for_user("user1")
        self.assertEqual(len(items), 1)

    def test_list_for_user_returns_copy_not_reference(self):
        self.store.save("u1", "k1", "v1")
        items = self.store.list_for_user("u1")
        items.append({"key": "k2", "value": "v2"})
        items_again = self.store.list_for_user("u1")
        self.assertEqual(len(items_again), 1)


if __name__ == "__main__":
    unittest.main()
