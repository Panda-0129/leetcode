# [279] Perfect Squares (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/perfect-squares/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/perfect-squares/)  [![Breadth-first%20Search_badge](https://img.shields.io/badge/topic-Breadth-first%20Search-green.svg)](https://leetcode.com/problems/perfect-squares/) 

:+1: 4082 &nbsp; &nbsp; :thumbsdown: 231

---

### My Solution


### Description
<p>Given an integer <code>n</code>, return <em>the least number of perfect square numbers that sum to</em> <code>n</code>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, <code>1</code>, <code>4</code>, <code>9</code>, and <code>16</code> are perfect squares while <code>3</code> and <code>11</code> are not.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> 3
<strong>Explanation:</strong> 12 = 4 + 4 + 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 2
<strong>Explanation:</strong> 13 = 4 + 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>



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
Among **778744** total submissions, **381629** are accepted, with an acceptance rate of **49.0%**. <br>

- Likes: 4082
- Dislikes: 231

