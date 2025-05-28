from src.lab3.node import Node
from copy import deepcopy

def invert_binary_tree(root: Node, result=None):
    if result is None:
       result = deepcopy(root)

    if root is None:
        return result

    result.left = invert_binary_tree(root.right)
    result.right = invert_binary_tree(root.left)
    return result
