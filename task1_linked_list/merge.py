from linked_list import LinkedList, Node

def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """Об'єднання двох відсортованих однозв'язних списків"""
    dummy = Node(0)
    tail = dummy
    a = list1.head
    b = list2.head

    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a:
        tail.next = a
    if b:
        tail.next = b

    merged = LinkedList()
    merged.head = dummy.next
    return merged