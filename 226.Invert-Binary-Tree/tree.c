#include <stdlib.h>

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

struct TreeNode *invertTree(struct TreeNode *root) {
  if (!root) {
    return NULL;
  }

  // O(n)
  struct TreeNode *tmp = root->left;
  root->left = invertTree(root->right);
  root->right = invertTree(tmp);

  return root;
}
