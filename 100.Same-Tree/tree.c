#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isSameTree(struct TreeNode *p, struct TreeNode *q) {
    if (!p && !q) {
        return true;
    }

    if (!p || !q) {
        return false;
    }

    if (p->val != q->val) {
        return false;
    }

    // O(n)
    if (!isSameTree(p->left, q->left)) {
        return false;
    }

    // O(n)
    if (!isSameTree(p->right, q->right)) {
        return false;
    }

    return true;
}
