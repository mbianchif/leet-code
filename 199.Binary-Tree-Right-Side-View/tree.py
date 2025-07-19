from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        if not root.right:
            return [root.val] + self.rightSideView(root.left)

        return [root.val] + self.rightSideView(root.right)
