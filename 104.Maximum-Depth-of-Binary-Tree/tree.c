struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
 

int maxDepth(struct TreeNode* root) {
    if (!root) {
      return 0;
    }

    // O(n)
    int l = 1 + maxDepth(root->left);
    int r = 1 + maxDepth(root->right);
    return l > r ? l : r;
}
