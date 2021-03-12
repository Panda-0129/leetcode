# [45] Jump Game II (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/jump-game-ii/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/jump-game-ii/) 

:+1: 3747 &nbsp; &nbsp; :thumbsdown: 172

---

### My Solution


### Description
<p>Given an array of non-negative integers <code>nums</code>, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Your goal is to reach the last index in the minimum number of jumps.</p>

<p>You can assume that you can always reach the last index.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2021-03-11 17:01:08

```Python
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            min_value = 10001
            for k in range(i):
                if nums[k] >= i - k:
                    min_value = min(dp[k] + 1, min_value)
            dp[i] = min_value
        
        return dp[-1]
```


### Related Problems
[Jump Game](https://leetcode.com/problems/jump-game/) (Medium) <br>
[Jump Game III](https://leetcode.com/problems/jump-game-iii/) (Medium) <br>



### What a(n) Medium problem!
Among **1014936** total submissions, **319248** are accepted, with an acceptance rate of **31.5%**. <br>

- Likes: 3747
- Dislikes: 172

