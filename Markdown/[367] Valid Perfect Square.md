# [367] Valid Perfect Square (Easy)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/valid-perfect-square/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/valid-perfect-square/) 

:+1: 1068 &nbsp; &nbsp; :thumbsdown: 187

---

### My Solution


### Description
<p>Given a <strong>positive</strong> integer <i>num</i>, write a function which returns True if <i>num</i> is a perfect square else False.</p>

<p><b>Follow up:</b> <b>Do not</b> use any built-in library function such as <code>sqrt</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> num = 16
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> num = 14
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2^31 - 1</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 28 ms
- Completed time: 2019-10-19 15:37:43

```Python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        
        while right >= left:
            mid = left + (right - left) // 2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
```


### Related Problems
[Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy) <br>
[Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/) (Medium) <br>



### What a(n) Easy problem!
Among **598094** total submissions, **251113** are accepted, with an acceptance rate of **42.0%**. <br>

- Likes: 1068
- Dislikes: 187

