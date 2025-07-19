from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def _height(self, root):
        if root is None:
            return 0

        # O(n)
        l = self._height(root.left)
        r = self._height(root.right)
        return 1 + max(l, r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # O(n)
        if not self.isBalanced(root.left):
            return False

        # O(n)
        if not self.isBalanced(root.right):
            return False

        # O(n)
        l = self._height(root.left)
        r = self._height(root.right)
        return abs(l - r) < 2
