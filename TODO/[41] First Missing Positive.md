# [41] First Missing Positive (Hard)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/first-missing-positive/) 

:+1: 5334 &nbsp; &nbsp; :thumbsdown: 947

---

### My Solution


### Description
<p>Given an unsorted integer array <code>nums</code>, find the smallest missing positive integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 300</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you implement an algorithm that runs in <code>O(n)</code> time and uses constant extra space?</p>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2021-03-10 10:27:50

```Python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums.sort()
        
        for num in nums:
            if num == res:
                res += 1
        
        return res
```


### Related Problems
[Missing Number](https://leetcode.com/problems/missing-number/) (Easy) <br>
[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium) <br>
[Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) (Easy) <br>
[Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) (Hard) <br>



### What a(n) Hard problem!
Among **1345326** total submissions, **454406** are accepted, with an acceptance rate of **33.8%**. <br>

- Likes: 5334
- Dislikes: 947

