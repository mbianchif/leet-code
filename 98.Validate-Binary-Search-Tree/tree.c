#include <stdbool.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool is_in_range(int x, long a, long b) {
    return a < x && x < b;
}

bool __is_valid_BST(struct TreeNode *root, long a, long b) {
    if (!root) return true;

    if (!is_in_range(root->val, a, b)) {
        return false;
    }

    if (!__is_valid_BST(root->left, a, root->val)) {
        return false;
    }

    if (!__is_valid_BST(root->right, root->val, b)) {
        return false;
    }

    return true;
}

bool isValidBST(struct TreeNode* root) {
    return __is_valid_BST(root, LONG_MIN, LONG_MAX);
}
