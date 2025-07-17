from typing import Optional


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        table = {}
        it = head

        # O(n)
        while it:
            table[it] = Node(it.val)
            it = it.next

        # O(n)
        it = head
        while it:
            node = table[it]

            node.next = table.get(it.next)
            node.random = table.get(it.random)

            it = it.next

        return table.get(head)
