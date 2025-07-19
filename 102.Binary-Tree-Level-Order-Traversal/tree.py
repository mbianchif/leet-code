from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels = []

        if not root:
            return levels

        # O(n)
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels.append(level)

        return levels
