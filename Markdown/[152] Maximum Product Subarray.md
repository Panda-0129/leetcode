# [152] Maximum Product Subarray (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/maximum-product-subarray/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/maximum-product-subarray/) 

:+1: 5929 &nbsp; &nbsp; :thumbsdown: 201

---

### My Solution


### Description
<p>Given an integer array&nbsp;<code>nums</code>, find the contiguous subarray within an array (containing at least one number) which has the largest product.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,3,-2,4]
<strong>Output:</strong> <code>6</code>
<strong>Explanation:</strong>&nbsp;[2,3] has the largest product 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;The result cannot be 2, because [-2,-1] is not a subarray.</pre>



### My Submission

- Language: Python
- Runtime: 56 ms
- Completed time: 2019-11-13 11:05:09

```Python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        current_max = [0] * len(nums)
        current_min = [0] * len(nums)
        res = current_max[0] = current_min[0] = nums[0]

        for i in range(1, len(nums)):
            current_max[i] = max(current_max[i - 1] * nums[i], current_min[i - 1] * nums[i], nums[i])
            current_min[i] = min(current_min[i - 1] * nums[i], current_max[i - 1] * nums[i], nums[i])
            res = max(res, current_max[i])

        return res
```


### Related Problems
[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Easy) <br>
[House Robber](https://leetcode.com/problems/house-robber/) (Medium) <br>
[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) <br>
[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) (Easy) <br>
[Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) (Medium) <br>



### What a(n) Medium problem!
Among **1320016** total submissions, **430365** are accepted, with an acceptance rate of **32.6%**. <br>

- Likes: 5929
- Dislikes: 201

