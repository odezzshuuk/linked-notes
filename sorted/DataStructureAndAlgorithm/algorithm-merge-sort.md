# Merge Sort

- By ensuring that the two arrays to be merged are sorted after partitioning, the complexity is simplified.
- Time complexity: O(n^2)
- When a temporary array is used, space complexity: O(n)

## Algorithm Analysis

Merge function: `merge(std::vector<int> nums, int left, int right)`: 

- `nums`: The array to be sorted
- `left`: Left boundary after partitioning
- `right`: Right boundary after partitioning

Variable Definitions

- `tmp`: Temporary array that stores sorted elements; it is updated with each recursion
- `mid`: Partition point, with the left subarray as [left, mid] and the right subarray as (mid, right]
- `i`: Left pointer pointing to the left subarray after partitioning
  - `i = left`;
- `j`: Right pointer pointing to the right subarray after partitioning
  - `j = mid + 1`;
- `cur`: Pointer to elements in the temporary array

Partitioning Process

- Find the midpoint: int mid = (left + right) / 2;
- Recursively process the left half: merge(nums, left, mid);
- Recursively process the right half: merge(nums, mid + 1, right);
- Base condition for recursion termination: if (left == right) return;, which means the array can no longer be partitioned as it contains only one element.

Recursive Merging

- The left pointer i and right pointer j start at the beginning of their respective subarrays.
- The smaller value between nums[i] and nums[j] is assigned to tmp[cur].
- Once an element's position is determined, move the corresponding pointer forward: i++; or j++;
- When one array's pointer reaches the end, it means all elements in that array have been placed, and the remaining elements in the other array are all greater than the sorted elements.
- The elements in the range [left, right] are now fully sorted.
- Return to the previous recursive process.
