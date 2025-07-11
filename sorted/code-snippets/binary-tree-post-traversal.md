# Binary Tree Post Traversal
 
```c++
void fx(TreeNode* root) {
  std::stack<TreeNode *> st;  
  TreeNode* prev = nullptr;  
  while (!st.empty() || root != nullptr) {  
    while (root != nullptr) {  
    st.push(root);
    root = root->left;  
    }  
    
    root = st.top(); 
    st.pop(); 
    
    if (root->right == nullptr || root->right == prev) {  
      std::cout << root->val << " ";  
      prev = root;  
      root = nullptr;  
    } else {  
      st.push(root);  
      root = root->right;  
    }  
  }  
}
```
