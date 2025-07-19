struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int count(struct TreeNode *root) {
    if (!root) {
        return 0;
    }

    // O(n)
    int l = count(root->left);
    int r = count(root->right);

    return 1 + l + r;
}

int kthSmallest(struct TreeNode *root, int k) {
    if (!root) {
        return -1;
    }
    
    // O(n)
    int left = 1 + count(root->left);

    if (left < k) {
        // O(n^2)
        return kthSmallest(root->right, k - left);
    }

    if (k < left) {
        // O(n^2)
        return kthSmallest(root->left, k);
    }

    return root->val;
}
