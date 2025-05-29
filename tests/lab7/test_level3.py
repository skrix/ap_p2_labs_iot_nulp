import unittest

from src.lab7.level3.base_task import build_trie
from src.lab7.level3.trie_node import TrieNode
from src.lab7.level3.trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search_single_word(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("apples"))
        self.assertFalse(self.trie.search("banana"))

    def test_insert_multiple_words(self):
        words = ["hello", "world", "hi"]
        for word in words:
            self.trie.insert(word)

        self.assertTrue(self.trie.search("hello"))
        self.assertTrue(self.trie.search("world"))
        self.assertTrue(self.trie.search("hi"))
        self.assertFalse(self.trie.search("hell"))
        self.assertFalse(self.trie.search("worl"))
        self.assertFalse(self.trie.search("h"))

    def test_insert_empty_string(self):
        self.assertFalse(self.trie.search(""))
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))

    def test_insert_duplicate_word(self):
        self.trie.insert("test")
        self.trie.insert("test")
        self.assertTrue(self.trie.search("test"))

    def test_search_in_empty_trie(self):
        self.assertFalse(self.trie.search("anyword"))
        self.assertFalse(self.trie.search(""))

    def test_starts_with_existing_prefix(self):
        self.trie.insert("apple")
        self.trie.insert("apricot")
        self.assertTrue(self.trie.starts_with("a"))
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("apple"))
        self.assertTrue(self.trie.starts_with("apri"))
        self.assertTrue(self.trie.starts_with("apricot"))

    def test_starts_with_non_existing_prefix(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.starts_with("b"))
        self.assertFalse(self.trie.starts_with("applesto"))
        self.assertFalse(self.trie.starts_with("ax"))

    def test_starts_with_empty_string(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.starts_with(""))

    def test_starts_with_in_empty_trie(self):
        self.assertTrue(self.trie.starts_with(""))
        self.assertFalse(self.trie.starts_with("a"))

    def test_build_trie_empty_list(self):
        patterns = []
        trie_instance = build_trie(patterns)
        self.assertIsInstance(trie_instance, Trie)
        self.assertFalse(trie_instance.search("anyword"))
        self.assertTrue(trie_instance.starts_with(""))

    def test_build_trie_with_patterns(self):
        patterns = ["apple", "apricot", "ape", "application"]
        trie_instance = build_trie(patterns)

        self.assertIsInstance(trie_instance, Trie)
        self.assertTrue(trie_instance.search("apple"))
        self.assertTrue(trie_instance.search("apricot"))
        self.assertTrue(trie_instance.search("ape"))
        self.assertTrue(trie_instance.search("application"))
        self.assertFalse(trie_instance.search("app"))

        self.assertTrue(trie_instance.starts_with("a"))
        self.assertTrue(trie_instance.starts_with("ap"))
        self.assertTrue(trie_instance.starts_with("app"))
        self.assertTrue(trie_instance.starts_with("appl"))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
