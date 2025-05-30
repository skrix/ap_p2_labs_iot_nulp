import unittest
from src.lab7.level3plus.aho_trie import AhoTrie

class TestAhoTrie(unittest.TestCase):

    def test_init(self):
        trie = AhoTrie()
        self.assertIsNotNone(trie.root)
        self.assertEqual(trie.root.fail, trie.root)
        self.assertEqual(trie.root.children, {})
        self.assertEqual(trie.root.output, [])

    def test_insert_single_word(self):
        trie = AhoTrie()
        trie.insert("hello")

        node = trie.root
        for char in "hello":
            self.assertIn(char, node.children)
            self.assertEqual(node.output, [])
            node = node.children[char]

        self.assertEqual(node.output, ["hello"])

    def test_insert_multiple_words(self):
        trie = AhoTrie()
        words = ["he", "she", "his", "hers"]
        for word in words:
            trie.insert(word)

        node_he = trie.root.children['h'].children['e']
        self.assertIn("he", node_he.output)

        node_she = trie.root.children['s'].children['h'].children['e']
        self.assertIn("she", node_she.output)

        node_his = trie.root.children['h'].children['i'].children['s']
        self.assertIn("his", node_his.output)

        node_hers = trie.root.children['h'].children['e'].children['r'].children['s']
        self.assertIn("hers", node_hers.output)
        self.assertIn("he", trie.root.children['h'].children['e'].output)

    def test_build_simple_fail_links(self):
        trie = AhoTrie()
        trie.insert("a")
        trie.insert("b")
        trie.insert("c")
        trie.build()

        self.assertEqual(trie.root.children['a'].fail, trie.root)
        self.assertEqual(trie.root.children['b'].fail, trie.root)
        self.assertEqual(trie.root.children['c'].fail, trie.root)


    def test_build_complex_case(self):
        trie = AhoTrie()
        trie.insert("abab")
        trie.insert("baba")
        trie.insert("ab")
        trie.insert("ba")
        trie.build()

        n_a = trie.root.children['a']
        n_ab = n_a.children['b']
        n_aba = n_ab.children['a']
        n_abab = n_aba.children['b']

        n_b = trie.root.children['b']
        n_ba = n_b.children['a']
        n_bab = n_ba.children['b']
        n_baba = n_bab.children['a']

        self.assertEqual(n_ab.fail, n_b)
        self.assertEqual(sorted(n_b.output), [])
        self.assertEqual(sorted(n_a.output), [])

        self.assertEqual(sorted(n_ab.output), sorted(["ab"]))
        self.assertEqual(sorted(n_ba.output), sorted(["ba"]))

        self.assertEqual(n_aba.fail, n_ba)
        self.assertEqual(sorted(n_aba.output), sorted(["ba"]))

        self.assertEqual(n_bab.fail, n_ab)
        self.assertEqual(sorted(n_bab.output), sorted(["ab"]))

        self.assertEqual(n_abab.fail, n_bab)
        self.assertEqual(sorted(n_abab.output), sorted(["ab", "abab"]))

        self.assertEqual(n_baba.fail, n_aba)
        self.assertEqual(sorted(n_baba.output), sorted(["ba", "baba"]))

    def test_search_no_match(self):
        trie = AhoTrie()
        trie.insert("keyword")
        trie.build()
        matches = list(trie.search("text without the word"))
        self.assertEqual(matches, [])

    def test_search_multiple_different_words(self):
        trie = AhoTrie()
        trie.insert("he")
        trie.insert("she")
        trie.insert("hers")
        trie.build()
        self.assertEqual(
            sorted(list(trie.search("ushers"))),
            sorted([
            (1, 3, "she"),
            (2, 3, "he"),
            (2, 5, "hers")
        ]))

        self.assertEqual(
            sorted(list(trie.search("ahishers"))),
            sorted([
            (3, 5, "she"),
            (4, 5, "he"),
            (4, 7, "hers")
        ]))

    def test_search_text_is_empty(self):
        trie = AhoTrie()
        trie.insert("word")
        trie.build()
        matches = list(trie.search(""))
        self.assertEqual(matches, [])

    def test_search_trie_is_empty(self):
        trie = AhoTrie()
        trie.build()
        matches = list(trie.search("any text"))
        self.assertEqual(matches, [])

    def test_search_simple(self):
        trie = AhoTrie()
        trie.insert("ab")
        trie.insert("b")
        trie.build()

        text = "cab"
        matches = sorted(list(trie.search(text)))
        expected = sorted([(1,2,"ab"), (2,2,"b")])
        self.assertEqual(matches, expected)

        text2 = "bab"
        matches2 = sorted(list(trie.search(text2)))
        expected2 = sorted([(0,0,"b"), (1,2,"ab"), (2,2,"b")])
        self.assertEqual(matches2, expected2)


if __name__ == "__main__":
    unittest.main()
