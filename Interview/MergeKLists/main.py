# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head, curr = None, None

        heap = []
        for i, item in enumerate(lists):
            if item is not None:
               heapq.heappush(heap, (item.val, i, item))

        while len(heap) > 0:
            _, i, item = heapq.heappop(heap)
            if head is None:
                head, curr = item, item
            else:
                curr.next, curr = item, item
            new_item = item.next
            if new_item is not None:
                heapq.heappush(heap, (new_item.val, i, new_item))

        return head





    pass
