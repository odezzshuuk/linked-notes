# Sort Algorithm - Heap Sort

[Heap](data-structure-heap.md)

- An application of priority queue
- Time complexity $O(nlogn)$
- Applicable when space is tight, such as embedded systems or low-cost mobile devices
- Cannot utilize cache

## Algorithm Analysis

- Variable definition
  - nums: The heap to be sorted, represented by an array. For a min-heap: nums.size() = 3
  - i: parent node index
  - right_idx: right child node index, int
  - left_idx: left child node index, int
  - largest: largest node index, int
- Build heap
  1. The process of traversing non-leaf nodes from bottom to top and calling the sink method
  3. By swapping parent node, left child node, and right child node, the maximum value among the 4 nodes is used as the new parent node.
  4. Find the index of the maximum value among `i, right_idx, left_idx`, and assign the maximum value to `largest`.
  5. Determine if left and right nodes exist `left_idx, right_idx < len`
  6. Compare element sizes
  7. If the largest node is not the parent node, swap the largest node with the parent node.

    ```c++
    /// overall code for step 4, 5
    if (left_idx < len && nums[i] < nums[left_idx]) largest = left_idx;
    else largest = i;  // If parent node is greater than left node, then largest index equals parent node
    if (right_idx < len && nums[i] < nums[largest]) largest = right_idx;
   ```

- Sort
  - Place the first element at the end of the array `std::swap(nums[0], nums[j])`
  - Rebuild the heap with the remaining elements excluding the first element

## Code

[[leetcode912_ArraySorting]]

## Summary

- step1: Traverse non-leaf nodes from bottom to top, call sink() to build the heap
- step2: Swap the top element and the last element
- step3: Array size - 1, repeat step1, step2