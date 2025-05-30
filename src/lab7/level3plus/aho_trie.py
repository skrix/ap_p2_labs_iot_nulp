from src.lab7.level3plus.aho_node import AhoNode
from collections import deque

class AhoTrie:
    def __init__(self):
        self.root = AhoNode()
        self.root.fail = self.root

    def insert(self, word):
        if not isinstance(word, str) or not word:
            return

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = AhoNode()
            node = node.children[char]
        if word not in node.output:
            node.output.append(word)

    def search(self, text):
        current_node = self.root
        for index, char in enumerate(text):
            while current_node != self.root and char not in current_node.children:
                current_node = current_node.fail

            current_node = current_node.children.get(char, self.root)

            if current_node.output:
                for word in current_node.output:
                    start = index - len(word) + 1
                    yield (start, index, word)

    def build(self):
        queue = deque()
        for child_node in self.root.children.values():
            child_node.fail = self.root
            queue.append(child_node)

        while queue:
            current_node = queue.popleft()
            for char, next_node in current_node.children.items():
                queue.append(next_node)

                next_node_fail = current_node.fail
                while next_node_fail != self.root and char not in next_node_fail.children:
                    next_node_fail = next_node_fail.fail

                if char in next_node_fail.children:
                    next_node.fail = next_node_fail.children[char]
                else:
                    next_node.fail = self.root

                if next_node.fail and next_node.fail.output:
                    current_output_set = set(next_node.output)
                    current_output_set.update(next_node.fail.output)
                    next_node.output = sorted(list(current_output_set))

