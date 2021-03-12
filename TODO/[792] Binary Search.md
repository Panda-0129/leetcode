# [792] Binary Search (Easy)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/binary-search/) 

:+1: 1195 &nbsp; &nbsp; :thumbsdown: 58

---

### My Solution


### Description
<p>Given an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in nums and its index is 4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in nums so return -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-9999 &lt;= nums[i], target &lt;= 9999</code></li>
	<li>All the integers in <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted in an ascending order.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 332 ms
- Completed time: 2020-09-17 15:49:29

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = 0
        left = len(nums) - 1
        
        while right <= left:
            mid = int(left + (right - left) / 2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                right = mid + 1
            elif nums[mid] > target:
                left = mid - 1
            
        return -1
```


### Related Problems
[Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) (Medium) <br>



### What a(n) Easy problem!
Among **443912** total submissions, **240136** are accepted, with an acceptance rate of **54.1%**. <br>

- Likes: 1195
- Dislikes: 58

