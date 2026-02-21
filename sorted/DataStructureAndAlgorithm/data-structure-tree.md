# Trees and Binary Trees

## Trees

- **Tree**  
  - The root node has no predecessor elements.  
  - `n` data elements are divided into `m` mutually disjoint sets, where each set itself is a tree.  

- **Related Concepts**  
  - **Degree of a node**: The number of branches of a node.  
  - **Terminal node (Leaf node)**: A node with a degree of 0.  
  - **Non-terminal node**: A node with a degree greater than 0.  
  - **Degree of a tree**: The maximum degree among all nodes in the tree.  
  - **Depth of a tree**: The maximum level among all nodes in the tree.  
  - **Ordered tree & Unordered tree**: If the order of subtrees from left to right follows a specific sequence, it is an **ordered tree**; otherwise, it is an **unordered tree**.  
  - **Forest**: A collection of `m` mutually disjoint trees.  

## Binary Tree Concepts

**Full Binary Tree**: If a binary tree of depth `K` contains \( 2^K - 1 \) nodes, it is called a **full binary tree**.  

- A single node is considered a full binary tree.  

**Complete Binary Tree**:  A binary tree of depth `h` with `n` nodes is a **complete binary tree** if:  

- The nodes of a full binary tree of the same depth are numbered **top to bottom, left to right**.  
- Each node in the binary tree corresponds to nodes numbered **1 to n** in the full binary tree.  

**Balanced Binary Tree**: A binary tree where the absolute difference in height between the left and right subtrees is at most **1**, and both subtrees are also balanced binary trees.  

- In **C++**, the underlying implementation of `map`, `set`, `multimap`, and `multiset` is a balanced binary tree.  

**Binary Search Tree(BST)**: A **sorted** tree with ordered values:  

- **Left Subtree is Smaller**  

> If the left subtree is non-empty, all nodes in the left subtree have values **less than** the root node.  

- **Right Subtree is Larger**  

> If the right subtree is non-empty, all nodes in the right subtree have values **greater than** the root node.  

- **Left and right subtrees are also binary search trees.**  

### Properties of Binary Trees

- **Property 1**: The maximum number of nodes on the `i`th level of a binary tree is \( 2^{i-1} \).  
- **Property 2**: The maximum number of nodes in a binary tree of depth `K` is \( 2^K - 1 \).  
- **Property 3**: For any binary tree `BT`, if the number of nodes with degree `0` is `n₀` and the number of nodes with degree `2` is `n₂`, then  
  \[
  n₀ = n₂ + 1
  \]
- **Property 4**: A complete binary tree with `n` nodes has a depth of  
  \[
  \lfloor \log_2 n \rfloor + 1
  \]
  where `log₂ n` is the greatest integer **not greater** than `log₂ n`.  
- **Property 5**: In a complete binary tree with `n` nodes, if nodes are numbered **top to bottom, left to right**, then for any node `i`:
  - If `i = 1`, then node `i` is the root and has no parent. Otherwise, the parent node's index is `i/2`.
  - If `2i > n`, the node has no left child. Otherwise, the left child's index is `2i`.
  - If `2i + 1 > n`, the node has no right child. Otherwise, the right child's index is `2i + 1`.
  - **Application**:  
    - For sequential storage, if a node is stored at **index `i` in an array**,  
      - The **left child's index** is `2i` (if it exists).  
      - The **right child's index** is `2i + 1`.  
      - The **parent node's index** is `i / 2`.  

**Proof of Property 3**:  

\[
\begin{aligned}
& n = n_0 + n_1 + n_2 \\
& B = n_1 + 2n_2 \\
& n = B + 1 \\
\end{aligned}
\Rightarrow n_0 = n_2 + 1
\]

Where:  
- `B`: Total number of branches in the binary tree.  
- `n₀`: Number of nodes with degree `0`.  
- `n₁`: Number of nodes with degree `1`.  
- `n₂`: Number of nodes with degree `2`.  

### Binary Tree Storage

- **Sequential Storage Structure**  
  - Uses a continuous block of memory to store nodes based on their **level order** (breadth-first) numbering.  
  - Can represent node relationships implicitly.  
  - **Not suitable for non-complete binary trees.**  

- **Linked Storage Structure**  
  - Representation:  
    ```
    LeftChild ← data → RightChild
    ```

### Binary Tree Traversal

- **Traversal is a recursive process**  
- **Typically traversed from left to right**  
- **Traversal Orders**:  
  - **Preorder (TLR - Root, Left, Right)**:  
    ```c++
    if (root == nullptr) return;
    std::cout << root->val << std::endl;  // Preorder traversal
    recursion(root->left);
    std::cout << root->val << std::endl;  // Inorder traversal
    recursion(root->right);
    std::cout << root->val << std::endl;  // Postorder traversal
    ```
  - **Inorder (LTR - Left, Root, Right)**  
  - **Postorder (LRT - Left, Right, Root)**  

- **Level Order Traversal**  
  - Uses a queue-based approach to process nodes level by level.

## Trie (Prefix Tree)

- Also known as a **prefix tree**.  
- The root does **not** represent any character.  
- Each node has **26 children**, representing **26 English letters**.  

```c++
class Trie {
  std::vector<Trie*> next;  // Array of child nodes
  bool isEnd;  // Marks the end of a word

  Trie() : next(26), isEnd(false) {};  // Constructor

  void insert(std::string word) {
    auto node = this;
    for (auto ch : word) {
      ch -= 'a';
      if (node->next[ch] == nullptr) {
        node->next[ch] = new Trie();
      }
      node = node->next[ch];
    }
  }

  bool startWith(std::string &word) {
    Trie* node = this;
    for (auto ch : word) {
      ch -= 'a';
      if (node->next[ch] == nullptr) {
        return false;
      }
      node = node->next[ch];
    }
    return true;
  }

  bool search(std::string prefix) {
    Trie* node = this;
    for (auto ch : prefix) {
      ch -= 'a';
      if (node->next[ch] == nullptr) {
        return false;
      }
    }
    return true && node->isEnd;
  }
};
```

## Red-Black Tree

- A non-strictly balanced binary search tree (BST).
- Properties:
- The root node is black, and leaf nodes are black empty nodes.
- No two consecutive red nodes.
- Any path from a node to its reachable leaf nodes contains the same number of black nodes.
- Characteristics:
- Slower searches compared to AVL trees.
- Faster insertions and deletions than AVL trees.
