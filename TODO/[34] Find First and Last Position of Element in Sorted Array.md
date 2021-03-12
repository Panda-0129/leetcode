# [34] Find First and Last Position of Element in Sorted Array (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) 

:+1: 5107 &nbsp; &nbsp; :thumbsdown: 196

---

### My Solution


### Description
<p>Given an array of integers <code>nums</code> sorted in ascending order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p><strong>Follow up:</strong>&nbsp;Could you write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 104 ms
- Completed time: 2020-09-17 16:01:44

```Python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def left_bound(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                mid = int(left + (right - left) / 2)
                
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    right = mid - 1
                    
            if left >= len(nums) or nums[left] != target:
                return -1
            
            return left
        
        def right_bound(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                mid = int(left + (right - left) / 2)
                
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    left = mid + 1
            
            if right < 0 or nums[right] != target:
                return -1
            
            return right
        
        return [left_bound(nums, target), right_bound(nums, target)]
```


### Related Problems
[First Bad Version](https://leetcode.com/problems/first-bad-version/) (Easy) <br>



### What a(n) Medium problem!
Among **1771878** total submissions, **661748** are accepted, with an acceptance rate of **37.3%**. <br>

- Likes: 5107
- Dislikes: 196

