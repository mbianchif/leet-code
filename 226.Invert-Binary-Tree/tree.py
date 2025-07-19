from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        stack = [root]

        # O(n)
        while stack:
            if node := stack.pop():
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root
