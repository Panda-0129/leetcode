# [792] Binary Search (Easy)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/binary-search/) 

:+1: 1068 &nbsp; &nbsp; :thumbsdown: 55

---

### My Solution


### Description
<p>Given a <strong>sorted</strong> (in ascending order) integer array <code>nums</code> of <code>n</code> elements and a <code>target</code> value, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index, otherwise return <code>-1</code>.</p>

<p><br />
<strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in <code>nums</code> and its index is 4

</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in <code>nums</code> so return -1
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>You may assume that all elements in <code>nums</code> are unique.</li>
	<li><code>n</code> will be in the range <code>[1, 10000]</code>.</li>
	<li>The value of each element in <code>nums</code> will be in the range <code>[-9999, 9999]</code>.</li>
</ol>



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
Among **406805** total submissions, **219510** are accepted, with an acceptance rate of **54.0%**. <br>

- Likes: 1068
- Dislikes: 55

