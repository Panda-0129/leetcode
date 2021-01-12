# [69] Sqrt(x) (Easy)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/sqrtx/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/sqrtx/) 

:+1: 1712 &nbsp; &nbsp; :thumbsdown: 2176

---

### My Solution


### Description
<p>Given a non-negative integer <code>x</code>,&nbsp;compute and return <em>the square root of</em> <code>x</code>.</p>

<p>Since the return type&nbsp;is an integer, the decimal digits are <strong>truncated</strong>, and only <strong>the integer part</strong> of the result&nbsp;is returned.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 4
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 44 ms
- Completed time: 2019-03-31 23:27:07

```Python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) / 2
            sqrt = x/mid
            if mid == sqrt:
                return mid
            elif mid > sqrt:
                high = mid - 1
            else:
                low = mid + 1
                
        return high
```


### Related Problems
[Pow(x, n)](https://leetcode.com/problems/powx-n/) (Medium) <br>
[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) (Easy) <br>



### What a(n) Easy problem!
Among **1883276** total submissions, **655495** are accepted, with an acceptance rate of **34.8%**. <br>

- Likes: 1712
- Dislikes: 2176

