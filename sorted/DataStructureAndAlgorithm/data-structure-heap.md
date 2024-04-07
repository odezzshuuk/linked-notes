# Data Structure - Heap

## What It Is

- Can be look as a [complete tree]()
- Max Heap: the value of each node is **greater than or equal to** its left and right child nodes
- Min Heap: the value of each node is **less than or equal to** its left and right child nodes

## Heap Algorithm

2 basic methods

- `swim()`: bottom-up to make the heap ordered

```c++
/// this is a max heap
std::vector<int> nums;
void swim(std::vector<int> nums, int i) {
  while (i > 1 && (i << 1) + 1 < nums.size()) {
    if (nums[i] > nums[i/2]) {
      std::swap(nums[i], nums[i/2]);
    }
  }
}
```
    
- `sink()`: When moving nodes from top to bottom, the upper nodes are replaced by the lower nodes 
    
```c++
void sink(std::vector<int> &nums, int i) {
  int j = 2 * i + 1;  // i is a non-leaf node
  if (j < nums.size() - 1 && nums[j] < nums[j + 1]) j++;
  if (a[i] < a[j]) {
    std::swap(nums[i], nums[j]);
    i = j;
  }
  sink(nums, i);
}
```

Method build from basic methods

- insert element: add new element to the end of array, which is the last leaf node, and `swim()` to the right position
- delete max element: swap the first element with the last element, and the new top node `sink()` to the right position
- array sort: repeat the process of calling `sink()`


## Binary Heap

- Binary Heap is a complete [tree](data-structure-tree.md)
- when heap is saved as an array, this array is not ordered, take a look at [Binary Tree Layer Print](binary-tree-layer-print.md)
- for $k$ node, parent node is $k/2$, child nodes are $2k, 2k+1$
- for max heap, element in the array satisfies `nums[k/2] >= nums[k] >= nums[2k] & nums[2k + 1]`
- for non-leaf node, the range of coordinates is $1,2,.......[n/2]$
- leaf node index is $[n/2] + 1, [n/2] + 2, ...., n$

[Heap Sort](heap-sort.md)

