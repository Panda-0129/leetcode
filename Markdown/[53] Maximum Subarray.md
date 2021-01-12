# [53] Maximum Subarray (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/maximum-subarray/)  [![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/maximum-subarray/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/maximum-subarray/) 

:+1: 10275 &nbsp; &nbsp; :thumbsdown: 495

---

### My Solution


### Description
<p>Given an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [4,-1,2,1] has the largest sum = 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> 0
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1]
<strong>Output:</strong> -1
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> nums = [-100000]
<strong>Output:</strong> -100000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.


### My Submission

- Language: Python
- Runtime: 96 ms
- Completed time: 2019-03-31 22:05:06

```Python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxSum = currentSum = nums[0]
        
        for num in nums[1:]:
            currentSum = max(currentSum + num, num)    
            maxSum = max(maxSum, currentSum)
        
        return maxSum
```


### Related Problems
[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) <br>
[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (Medium) <br>
[Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) (Easy) <br>
[Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) (Medium) <br>



### What a(n) Easy problem!
Among **2664398** total submissions, **1266112** are accepted, with an acceptance rate of **47.5%**. <br>

- Likes: 10275
- Dislikes: 495

