struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int diameter_of_tree(struct TreeNode *root, int *max_diam) {
    if (!root) {
        return 0;
    }

    // O(n)
    int l = diameter_of_tree(root->left, max_diam);
    int r = diameter_of_tree(root->right, max_diam);
    int this_diam = l + r;

    if (*max_diam < this_diam) {
        *max_diam = this_diam;
    }

    return 1 + (l > r ? l : r);
}

int diameterOfBinaryTree(struct TreeNode *root) {
    if (!root) {
        return 0;
    }

    int diam = 0;

    // O(n)
    diameter_of_tree(root, &diam);
    return diam;
}
