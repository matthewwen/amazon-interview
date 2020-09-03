# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        [head, curr] = [None, None]
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                if head == None:
                    [head, curr] = [l1, l1]
                else:
                    [curr.next, curr] = [l1, l1]
                l1 = l1.next
            else:
                if head == None:
                    [head, curr] = [l2, l2]
                else:
                    [curr.next, curr] = [l2, l2]
                l2 = l2.next
        if l1 != None:
            if head == None:
                head = l1
            else:
                curr.next = l1
        elif l2 != None:
            if head == None:
                head = l2
            else:
                curr.next = l2
            
        return head
