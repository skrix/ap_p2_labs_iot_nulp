from src.lab3.node import Node

def in_order_traversal(root: Node, result=[]):
    if root is None or root.value is None:
        return
    else:
        in_order_traversal(root.left)
        result.append(root.value)
        in_order_traversal(root.right)
    return result

def pre_order_traversal(root: Node, result=[]):
    if root is None or root.value is None:
        return
    else:
        result.append(root.value)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
    return result

def post_order_traversal(root: Node, result=[]):
    if root is None or root.value is None:
        return
    else:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        result.append(root.value)
    return result
