# Algorithm - Insert Sort

- time complexity $O(n^2)$

```c++
void sort(std::vector<int> &nums) {  
  int n = nums.size();  
  for (int j = 1; j < n; j++) {  
    int tmp = nums[j];  /// Extract the value to be sorted
    int i = j - 1;  /// Starting point for comparison
    while (i >= 0 && nums[i] > tmp) {  
      nums[i+1] = nums[i];  /// Assign the value of the left element to nums[i + 1]
      i--;  
    }  
    nums[i+1] = tmp;  
  }  
}
```