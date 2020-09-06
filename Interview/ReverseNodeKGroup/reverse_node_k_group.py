# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr, length = head, 0
        while curr:
            length += 1
            curr = curr.next

        curr, head, prev = head, None, None
        while curr:
            i, temp_head, temp_tail = 1, curr, curr
            while i < k <= length:
                item = temp_tail.next
                if item:
                    temp_tail.next = item.next
                    item.next = temp_head
                    temp_head = item
                    i += 1
                else:
                    break
            head = temp_head if head is None else head
            if prev:
                prev.next = temp_head
            length -= k
            prev = temp_tail
            curr = temp_tail.next

        return head

