from typing import Optional
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # O(n)
        idxs = [(node.val, i) for i, node in enumerate(lists) if node]

        # O(n)
        heapify(idxs)

        curr = None
        root = None

        # O(Nlogn)
        while idxs:
            _, i = heappop(idxs)
            if not root:
                root = lists[i]

            if curr:
                curr.next = lists[i]
            curr = lists[i]

            if next := lists[i].next:
                lists[i] = next
                heappush(idxs, (next.val, i))

        return root
