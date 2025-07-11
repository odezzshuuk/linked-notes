# Binary Tree layer insert

```c++
void BTLayerInsert(TreeNode *&root, std::vector<int> list) {
  root = new TreeNode(list[0]);  
  std::queue<TreeNode *> tq;  
  tq.push(root);  
  int j = 1;  
 
  while (j != list.size()) {  
    TreeNode *node = tq.front();  
    tq.pop();  
    
    if (j < list.size()) {  
      TreeNode *lnode;  
      TreeNode *rnode;  
    
      if (list[j]) {
        lnode = new TreeNode(list[j++]);  
        node->left = lnode;  
        tq.push(lnode);  
      } else {
        j++;  
      }  
      
      if (list[j]) {  
        rnode = new TreeNode(list[j++]);  
        node->right = rnode;  
        tq.push(rnode);  
      } else {  
         j++;  
      }  
    }  
  }  
}
```
