
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        # Recursion is a natural fit here: the sum of the list is just the
        # current node's data plus the sum of everything after it.
        def _sum(node):
            if node is None:
                return 0  # base case: an empty list contributes nothing
            return node.data + _sum(node.next)  # recursive case

        return _sum(self.head)

    def recursive_reverse(self):
        # Walk the list one node at a time, flipping each node's 'next'
        # pointer to point backward at 'prev'. The recursion carries the
        # growing reversed chain (prev) forward until it reaches the end.
        def _reverse(prev, current):
            if current is None:
                return prev  # base case: 'prev' is the new head

            next_node = current.next
            current.next = prev
            return _reverse(current, next_node)

        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        def _search(node):
            if node is None:
                return False  # base case: fell off the end, not found
            if node.data == target:
                return True
            return _search(node.next)  # recursive case

        return _search(self.head)

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        result = " -> ".join(values)
        print(result)
        return result
