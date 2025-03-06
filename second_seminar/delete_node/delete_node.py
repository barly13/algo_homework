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







