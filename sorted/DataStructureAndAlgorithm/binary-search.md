# Binary search

- suitable for sorted array

> not necessary to be strictly sorted, for example, [[quick select]] problem, the left of pivot is greater than the right of pivot, we can also use binary search to find the target value

- critical point is flexible, need to be summarized

## code

```c++
class Solution {
 public:
  int searchInsert(std::vector<int> &nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
      int mid = (left + right) / 2;
      if (nums[mid] > target) {
        right = mid - 1;
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        return mid;
      }
    }
  }
};
```

## deal with mid point

- `mid = (left + right) / 2;`
- `mid = (left + right + 1) / 2;`

## edge

- judge condition
  - `nums[mid] > target;`
  - `nums[mid] >= target;`
- changing range
  - `left = mid;`, `right = mid;`
  - `left = mid + 1`, `right = left - 1`

## example

[[leetcode34查找元素第一和最后的位置]]