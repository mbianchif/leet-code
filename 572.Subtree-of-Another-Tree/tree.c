#include <stdbool.h>

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

bool __is_subtree(struct TreeNode *root, struct TreeNode *sub_root) {
  if (!root && !sub_root) {
    return true;
  }

  if (!root || !sub_root) {
    return false;
  }

  if (root->val != sub_root->val) {
    return false;
  }

  // O(m)
  if (!__is_subtree(root->left, sub_root->left)) {
    return false;
  }

  // O(m)
  if (!__is_subtree(root->right, sub_root->right)) {
    return false;
  }

  return true;
}

bool isSubtree(struct TreeNode *root, struct TreeNode *subRoot) {
  if (!root) {
    return false;
  }

  // O(min(n, m))
  if (__is_subtree(root, subRoot)) {
    return true;
  }

  // O(n * m)
  if (isSubtree(root->left, subRoot)) {
    return true;
  }

  // O(n * m)
  if (isSubtree(root->right, subRoot)) {
    return true;
  }

  return false;
}
