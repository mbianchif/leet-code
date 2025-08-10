from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)

        # O(n)
        indices = {v: i for i, v in enumerate(inorder)}

        def build_tree(i, j, k, l):
            if i == j:
                return None

            root_val = preorder[i]

            if j - i == 1:
                return TreeNode(root_val)

            root_idx_inorder = indices[root_val]
            left_size = root_idx_inorder - k

            left = build_tree(i + 1, i + 1 + left_size, k, root_idx_inorder)
            right = build_tree(i + 1 + left_size, j, root_idx_inorder + 1, l)
            return TreeNode(root_val, left, right)

        # O(n)
        return build_tree(0, n, 0, n)
