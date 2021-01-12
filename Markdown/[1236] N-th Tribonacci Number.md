# [1236] N-th Tribonacci Number (Easy)

[![Recursion_badge](https://img.shields.io/badge/topic-Recursion-green.svg)](https://leetcode.com/problems/n-th-tribonacci-number/) 

:+1: 436 &nbsp; &nbsp; :thumbsdown: 49

---

### My Solution


### Description
<p>The Tribonacci sequence T<sub>n</sub> is defined as follows:&nbsp;</p>

<p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n &gt;= 0.</p>

<p>Given <code>n</code>, return the value of T<sub>n</sub>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 25
<strong>Output:</strong> 1389537
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 37</code></li>
	<li>The answer is guaranteed to fit within a 32-bit integer, ie. <code>answer &lt;= 2^31 - 1</code>.</li>
</ul>


### My Submission

- Language: Python
- Runtime: 28 ms
- Completed time: 2020-11-02 19:10:53

```Python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[n]
```


### Related Problems
[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (Easy) <br>
[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (Easy) <br>



### What a(n) Easy problem!
Among **111074** total submissions, **62348** are accepted, with an acceptance rate of **56.1%**. <br>

- Likes: 436
- Dislikes: 49

