from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0

            tl, ll = dfs(node.left)
            tr, lr = dfs(node.right)

            take = ll + lr + node.val
            leave = max(tl, ll) + max(tr, lr)
            return take, leave

        # O(n)
        return max(dfs(root))
