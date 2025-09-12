# Algorithm - Backtracking

- Related to [[Depth-First Search]]

## Summary

- **Return Condition**: The condition that stops the recursive process.
- For example, in a binary tree traversal:

```cpp
void dfs(TreeNode* root) {
  // The return condition determines the depth of the search.
  if (root == nullptr) {
    return;
  }
  
  // Prioritize traversing the left subtree.
  dfs(root->left);
  
  // Then traverse the right subtree.
  dfs(root->right);
}
```