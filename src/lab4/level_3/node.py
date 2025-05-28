class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.key = -priority
        self.height = 1
        self.left = None
        self.right = None
