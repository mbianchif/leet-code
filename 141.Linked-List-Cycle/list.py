from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        # O(n)
        while slow and fast:
            if slow == fast:
                return True

            slow = slow.next
            temp = fast.next
            if not temp:
                return False

            fast = temp.next

        return False
