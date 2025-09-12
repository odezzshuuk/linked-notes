# Data Structure - Linked List

## What Is Linked List

- Linked lists are not continuously distributed in memory, the address depends on the operating system
- The head of the linked list is uniquely determined
- Single linked list definition
  - Element
  - Pointer to the next node
  - Constructor
- First element node: The node that stores the first element
- Head pointer: A pointer to the first node
- For convenience, a head node is often set up
  - Head node: A node pointing to the first node
  - Makes it easier to handle the first element node

```c++
struct ListNode {
    int val;  // Element stored on the node
    ListNode *next;  // Pointer to the next node
    ListNode(int x) : val(x), next(NULL) {}  // Node constructor
};
```

- Linked list deletion
- Adding nodes