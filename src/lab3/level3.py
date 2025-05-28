from src.lab3.node import Node

def binary_tree_diameter(root: Node):
    result = 0

    def diameter(node: Node):
        nonlocal result

        if not node:
            return 0

        left_height = diameter(node.left)
        right_height = diameter(node.right)
        result = max(result, left_height + right_height)
        return 1 + max(left_height, right_height)

    diameter(root)
    return result
