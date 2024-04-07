# Binary Tree Layer Print

```c++
void layer_print_tree(TreeNode *root) {
  std::queue<TreeNode *> tq;
  tq.push(root);
  int j = 0;
  while (!tq.empty()) {
    TreeNode *node = tq.front();
    tq.pop();
    if (node) {
      std::cout << node->val << " ";
      tq.push(node->left);
      tq.push(node->right);
    } else {
      std::cout << "NULL" << " ";
    }
  }
}
```
