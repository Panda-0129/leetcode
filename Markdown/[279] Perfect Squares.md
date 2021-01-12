# [279] Perfect Squares (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/perfect-squares/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/perfect-squares/)  [![Breadth-first%20Search_badge](https://img.shields.io/badge/topic-Breadth-first%20Search-green.svg)](https://leetcode.com/problems/perfect-squares/) 

:+1: 3804 &nbsp; &nbsp; :thumbsdown: 224

---

### My Solution


### Description
<p>Given a positive integer <i>n</i>, find the least number of perfect square numbers (for example, <code>1, 4, 9, 16, ...</code>) which sum to <i>n</i>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>12</code>
<b>Output:</b> 3 
<strong>Explanation: </strong><code>12 = 4 + 4 + 4.</code></pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>13</code>
<b>Output:</b> 2
<strong>Explanation: </strong><code>13 = 4 + 9.</code></pre>


### My Submission

- Language: Python
- Runtime: 6780 ms
- Completed time: 2019-12-02 15:03:24

```Python
import sys

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1
        return dp[-1]        
```


### Related Problems
[Count Primes](https://leetcode.com/problems/count-primes/) (Easy) <br>
[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) (Medium) <br>



### What a(n) Medium problem!
Among **752209** total submissions, **365335** are accepted, with an acceptance rate of **48.6%**. <br>

- Likes: 3804
- Dislikes: 224

