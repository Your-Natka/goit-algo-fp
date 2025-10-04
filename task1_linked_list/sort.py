from linked_list import LinkedList, Node

def insertion_sort(llist: LinkedList) -> LinkedList:
    """Сортування однозв'язного списку методом вставки"""
    sorted_list = LinkedList()
    current = llist.head

    while current:
        data = current.data
        if not sorted_list.head or data < sorted_list.head.data:
            new_node = Node(data)
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            search = sorted_list.head
            while search.next and search.next.data < data:
                search = search.next
            new_node = Node(data)
            new_node.next = search.next
            search.next = new_node
        current = current.next

    return sorted_list