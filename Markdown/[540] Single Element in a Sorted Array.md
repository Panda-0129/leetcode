# [540] Single Element in a Sorted Array (Medium)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/single-element-in-a-sorted-array/) 

:+1: 2108 &nbsp; &nbsp; :thumbsdown: 85

---

### My Solution


### Description
<p>You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly&nbsp;once. Find this single element that appears only once.</p>

<p><b>Follow up:</b> Your solution should run in O(log n) time and O(1) space.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,2,3,3,4,4,8,8]
<strong>Output:</strong> 2
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,3,7,7,10,11,11]
<strong>Output:</strong> 10
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= nums[i]&nbsp;&lt;= 10^5</code></li>
</ul>


### My Submission

- Language: Python
- Runtime: 72 ms
- Completed time: 2019-04-01 20:47:03

```Python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 0:
                mid+=1
            if nums[mid] == nums[mid - 1]:
                low = mid + 1    
            else:
                high = mid - 1   
                
        return nums[low]
        
```


### Related Problems




### What a(n) Medium problem!
Among **301656** total submissions, **174723** are accepted, with an acceptance rate of **57.9%**. <br>

- Likes: 2108
- Dislikes: 85

