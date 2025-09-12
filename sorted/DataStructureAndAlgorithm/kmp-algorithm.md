# KMP Algorithm (Pattern Matching Algorithm)

> named by creator's name: Knuth-Morris-Pratt

- use pattern string to generate prefix table (next array)
  - init suffix index `i`, prefix index `j`
  - considering the difference of prefix and suffix, `while (j > -1 && s[i] != s[j + 1]) {j = next[j]}`
  - considering the similarity of prefix and suffix, `if (s[i] == s[j + 1]) {j++}`
  - assign the value of [`next`](#prefix-table-next-array) element `next[i] = j;`
- Using prefix table for matching
  - Text string `s[i]`, pattern string `t[j]`
  - Iterate through text string `for (int i = 0;i < s.size(); i++)`
  - Text string and pattern string don't match: `while (j >= 0 && s[i] != t[j]) j = next[j];`
  - Text string and pattern string match: `if (s[i] == t[j]) j++;`
- mostly apply to string matching
- KMP won't backtrace the original string, so it's faster than brute force algorithm

## Prefix Table Next Array

- next array
  - size equals the length of the pattern string
  - elements: get the longest matching length of prefix and suffix for all substrings that include the first character
  - when prefix and suffix are different, j backtracks
  - when prefix and suffix are the same, `j++`
  - j has two meanings
    - next element
    - index of return position

  ```c++
  void getNext(int* next, const string& s) {
    // j has two meanings: ①index, ②next array element
    int j = -1;
    next[0] = j;
    for(int i = 1; i < s.size(); i++) { // Note i starts from 1
      while (j >= 0 && s[i] != s[j + 1]) { // prefix and suffix different, backtrack
        j = next[j]; // backtrack
      }
      if (s[i] == s[j + 1]) { // found matching prefix and suffix
        j++;
      }
      next[i] = j; // assign j (length of prefix) to next[i]
    }
  }
  ```