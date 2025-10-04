from linked_list import LinkedList, Node

def reverse_linked_list(llist: LinkedList) -> LinkedList:
    """Реверсування однозв'язного списку"""
    prev = None
    current = llist.head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    llist.head = prev
    return llist