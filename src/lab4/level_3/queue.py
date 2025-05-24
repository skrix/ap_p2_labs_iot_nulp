from src.lab4.level_3.node import Node


class Queue:
    def __init__(self):
        self.root = None

    def enqueue(self, value, priority):
        node = Node(value=value, priority=priority)
        self.root = self._insert(self.root, node)
        return node

    def dequeue(self):
        if self.root is None:
            return None

        self.root, node = self._delete(self.root)
        return node

    def _delete(self, root):
        pass

    def _insert(self, current, node):
        pass

    def status(self):
        result = []
        for current_node in self:
            result.append([current_node.value, current_node.priority])
        return result

    def __iter__(self):
        yield from self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return None
        # left subtree (higher priorities)
        yield from self._inorder(node.left)
        # current node
        yield node
        # right subtree (lower priorities)
        yield from self._inorder(node.right)
