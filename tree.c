#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    struct TreeNode *left;
    struct TreeNode *right;
};

int max(int a, int b) { return a > b ? a : b; }

int height(struct TreeNode *root) {
    if (!root) {
        return 0;
    }

    // O(n)
    int l = height(root->left);
    int r = height(root->right);
    return 1 + max(l, r);
}

bool isBalanced(struct TreeNode *root) {
    if (!root) {
        return true;
    }

    // O(n)
    if (!isBalanced(root->left)) {
        return false;
    }

    // O(n)
    if (!isBalanced(root->right)) {
        return false;
    }

    // O(n)
    int l = height(root->left);
    int r = height(root->right);
    return abs(l - r) < 2;
}
