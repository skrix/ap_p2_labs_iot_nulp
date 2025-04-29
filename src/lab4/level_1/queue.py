from src.lab4.level_1.node import Node


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        node = Node(value=value, priority=priority)

        # 1 - new node is new queue head:
        #     when queue is empty
        if self.head is None:
            self.head = node
            return node

        # 2 - new node is new queue head:
        #     when head priority less than new node priority
        if node.priority > self.head.priority:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return node

        # 3 - new node somewhere in queue:
        #     looking for next and prev for new node
        next = self.head
        while next and next.priority >= node.priority:
            prev = next
            next = next.next

        if next:
            # 3 - new node somewhere in queue:
            #     when found prev and next for new node
            node.next = next
            node.prev = prev
            prev.next = node
            next.prev = node
        else:
            # 4 - new node at the end in queue:
            #     when found prev but not next for new node
            prev.next = node
            node.prev = prev

        return node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            result = self.head
            self.head = self.head.next
            self.head.prev = None
            return result

    def status(self):
        result = []
        for current_node in self:
            result.append([current_node.value, current_node.priority])
        return result

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
