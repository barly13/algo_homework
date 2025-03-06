from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    head = prev_node
    return head


def reverse_linked_list_2(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None

    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node

    return prev_node
