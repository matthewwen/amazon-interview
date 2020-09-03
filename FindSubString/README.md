[Problem Statement](https://leetcode.com/discuss/interview-question/370157) 

Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers

Example 1:
```
Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
```

Example 2:
```
Input: s = "aabab", k = 3
Output: 0
```
Constraints:

The input string consists of only lowercase English letters [a-z]

0 ≤ k ≤ 26