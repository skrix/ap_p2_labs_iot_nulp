from src.lab7.level3.trie import Trie

def build_trie(patterns):
    trie_instance = Trie()
    for pattern in patterns:
        trie_instance.insert(pattern)
    return trie_instance
