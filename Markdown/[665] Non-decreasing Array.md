# [665] Non-decreasing Array (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/non-decreasing-array/) 

:+1: 2398 &nbsp; &nbsp; :thumbsdown: 579

---

### My Solution


### Description
<p>Given an array <code>nums</code> with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <b>at most</b> <code>1</code> element.</p>

<p>We define an array is non-decreasing if <code>nums[i] &lt;= nums</code><code>[i + 1]</code> holds for every <code>i</code>&nbsp;(0-based) such that <code>(0&nbsp;&lt;= i &lt;= n - 2)</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> You can&#39;t get a non-decreasing array by modify at most one element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10 ^ 4</code></li>
	<li><code>- 10 ^ 5&nbsp;&lt;= nums[i] &lt;= 10 ^ 5</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 396 ms
- Completed time: 2019-03-31 21:37:09

```Python
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 1
        count = 0
        while i < len(nums):
            if nums[i-1] > nums[i]:
                count+=1
                if count > 1:
                    return False
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
            i+=1
        return True
        
```


### Related Problems




### What a(n) Easy problem!
Among **599191** total submissions, **117651** are accepted, with an acceptance rate of **19.6%**. <br>

- Likes: 2398
- Dislikes: 579

