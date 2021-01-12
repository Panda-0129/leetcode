# [368] Largest Divisible Subset (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/largest-divisible-subset/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/largest-divisible-subset/) 

:+1: 1679 &nbsp; &nbsp; :thumbsdown: 86

---

### My Solution


### Description
<p>Given a set of <strong>distinct</strong> positive integers <code>nums</code>, return the largest subset <code>answer</code> such that every pair <code>(answer[i], answer[j])</code> of elements in this subset satisfies:</p>

<ul>
	<li><code>answer[i] % answer[j] == 0</code>, or</li>
	<li><code>answer[j] % answer[i] == 0</code></li>
</ul>

<p>If there are multiple solutions, return any of them.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> [1,3] is also accepted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,4,8]
<strong>Output:</strong> [1,2,4,8]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2 * 10<sup>9</sup></code></li>
	<li>All the integers in <code>nums</code> are <strong>unique</strong>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 432 ms
- Completed time: 2019-12-03 08:43:21

```Python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []

        dp = [[] for _ in range(len(nums))]
        max_index, max_size = 0, -1
        final_index, final_size = 0, -1
        nums.sort()

        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[i] % nums[j] == 0 and len(dp[j]) > max_size:
                    max_index = j
                    max_size = len(dp[j])
            if max_size != -1:
                dp[i] += dp[max_index]
            dp[i].append(nums[i])

            if len(dp[i]) > final_size:
                final_size = len(dp[i])
                final_index = i
            max_index, max_size = 0, -1

        return dp[final_index]        
```


### Related Problems




### What a(n) Medium problem!
Among **277670** total submissions, **106012** are accepted, with an acceptance rate of **38.2%**. <br>

- Likes: 1679
- Dislikes: 86

