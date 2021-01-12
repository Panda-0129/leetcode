# [633] Sum of Square Numbers (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/sum-of-square-numbers/) 

:+1: 625 &nbsp; &nbsp; :thumbsdown: 364

---

### My Solution


### Description
<p>Given a non-negative integer <code>c</code>, decide whether there&#39;re two integers <code>a</code> and <code>b</code> such that <code>a<sup>2</sup> + b<sup>2</sup> = c</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> c = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 * 1 + 2 * 2 = 5
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> c = 3
<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> c = 4
<strong>Output:</strong> true
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> c = 2
<strong>Output:</strong> true
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> c = 1
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= c &lt;= 2<sup>31</sup> - 1</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 124 ms
- Completed time: 2019-03-23 23:12:51

```Python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, math.ceil(math.sqrt(c))
        while i <= j:
            sum = i*i + j*j
            if sum == c:
                return True
            elif sum > c:
                j-=1
            else:
                i+=1
        return False
```


### Related Problems
[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) (Easy) <br>



### What a(n) Medium problem!
Among **241365** total submissions, **78280** are accepted, with an acceptance rate of **32.4%**. <br>

- Likes: 625
- Dislikes: 364

