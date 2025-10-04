class Node:
    """Вузол однозв'язного списку"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Однозв'язний список"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додати елемент у кінець списку"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Додати елемент на початок списку"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __iter__(self):
        """Ітерація по списку"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        """Рядкове представлення списку"""
        return " -> ".join(str(item) for item in self)