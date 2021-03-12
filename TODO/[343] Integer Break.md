# [343] Integer Break (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/integer-break/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/integer-break/) 

:+1: 1461 &nbsp; &nbsp; :thumbsdown: 254

---

### My Solution


### Description
<p>Given an integer <code>n</code>, break it into the sum of <strong>at least two positive integers</strong> and maximize the product of those integers.</p>

<p>Return <em>the maximum product you can get</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 2 = 1 + 1, 1 &times; 1 = 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 36
<strong>Explanation:</strong> 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 58</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 32 ms
- Completed time: 2019-11-22 14:15:14

```Python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max(j * (i - j), dp[i - j] * j))

        return dp[-1]        
```


### Related Problems




### What a(n) Medium problem!
Among **245754** total submissions, **125931** are accepted, with an acceptance rate of **51.2%**. <br>

- Likes: 1461
- Dislikes: 254

