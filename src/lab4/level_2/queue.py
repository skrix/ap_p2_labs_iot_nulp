from src.lab4.level_2.node import Node


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
        if root.left is None:
            max_node = root
            new_root = root.right
            max_node.right = None
            return (new_root, max_node)

        new_left, max_node = self._delete(root.left)
        root.left = new_left
        return (root, max_node)

    def _insert(self, current, node):
        if current is None:
            return node
        if node.priority >= current.priority:
            current.left = self._insert(current.left, node)
        else:
            current.right = self._insert(current.right, node)
        return current

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
