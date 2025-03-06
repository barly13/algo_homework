from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_node(head: ListNode, val: int):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    current = head

    while current is not None:
        if current.val == val:
            prev.next = current.next

        else:
            prev = current

        current = current.next

    return dummy.next


def has_cycle(head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True


def has_cycle_2(head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


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


def middle_of_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def is_subsequence(a: str, b: str) -> bool:
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1

        j += 1

    return i == len(a)


def is_palindrome(a: str) -> bool:
    left = 0
    right = len(a) - 1

    while left < right:
        if a[left] != a[right]:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_2(s: str) -> bool:
    if s[0] != s[-1]:
        return False

    mid = len(s) // 2
    for i in range(mid + 1):
        if s[0 + i] != s[-1 - i]:
            return False

    return True


def is_palindrome_3(s: str) -> bool:
    return s == s[::-1]

