# [343] Integer Break (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/integer-break/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/integer-break/) 

:+1: 1370 &nbsp; &nbsp; :thumbsdown: 244

---

### My Solution


### Description
<p>Given a positive integer <i>n</i>, break it into the sum of <b>at least</b> two positive integers and maximize the product of those integers. Return the maximum product you can get.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">2</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>2 = 1 + 1, 1 &times; 1 = 1.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">10</span>
<strong>Output: </strong><span id="example-output-2">36</span>
<strong>Explanation: </strong>10 = 3 + 3 + 4, 3 &times;&nbsp;3 &times;&nbsp;4 = 36.</pre>

<p><b>Note</b>: You may assume that <i>n</i> is not less than 2 and not larger than 58.</p>
</div>
</div>


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
Among **239154** total submissions, **122006** are accepted, with an acceptance rate of **51.0%**. <br>

- Likes: 1370
- Dislikes: 244

