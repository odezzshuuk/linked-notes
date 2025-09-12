# Bubble Sort

- time complexity is $O(n^2)$

## How It works

- swap two adjacent elements if the left one is greater than the right one
- put the largest number to the end of the array in each loop

## code

```c++
void sort(std::vector<int> &nums) {
  int len = nums.size();
  for (int i = len; i > 0; i--) {
    for (int j = 0; j < i; j++) {
      if (nums[j] > nums[j + 1]) std::swap(nums[j], nums[j + 1]);  
    }
  }
}
```