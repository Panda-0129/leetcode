# [179] Largest Number (Medium)

[![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/largest-number/) 

:+1: 2690 &nbsp; &nbsp; :thumbsdown: 289

---

### My Solution


### Description
<p>Given a list of non-negative integers <code>nums</code>, arrange them such that they form the largest number.</p>

<p><strong>Note:</strong> The result may be very large, so you need to return a string instead of an integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,2]
<strong>Output:</strong> &quot;210&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,30,34,5,9]
<strong>Output:</strong> &quot;9534330&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> &quot;1&quot;
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> nums = [10]
<strong>Output:</strong> &quot;10&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 44 ms
- Completed time: 2019-10-12 15:13:26

```Python
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def ch_cmp(a, b):
            return int(b + a) - int(a + b)
        
        nums = sorted([str(num) for num in nums], key=cmp_to_key(ch_cmp))
        res = ''.join(nums)
        
        return res.lstrip('0') or '0'
```


### Related Problems




### What a(n) Medium problem!
Among **761763** total submissions, **231643** are accepted, with an acceptance rate of **30.4%**. <br>

- Likes: 2690
- Dislikes: 289

