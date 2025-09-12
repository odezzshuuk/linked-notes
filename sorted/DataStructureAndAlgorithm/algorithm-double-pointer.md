# Algorithm - Double Pointers

- Used for traversing two elements in an **ordered** array
- One pointer for traversal, one pointer for operation
- The key is to move the operating pointer appropriately
- Also known as sliding window

## Using fast and slow pointers to remove spaces from a string

- Fast pointer scans, slow pointer records **characters** that meet the conditions
- Slow pointer recording conditions, simultaneously satisfying the following three conditions:
  - `fast > 1;`
  - `s[fast - 1] == s[fast];`
  - `s[fast] == ' ';`
- The final result is from the beginning to the **character pointed to by the slow pointer**
- Trim using the resize member function

## Example

[[leetcode3LongestSubstringWithoutRepeatingCharacters]]