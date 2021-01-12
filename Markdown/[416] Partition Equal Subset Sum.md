# [416] Partition Equal Subset Sum (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/partition-equal-subset-sum/) 

:+1: 3806 &nbsp; &nbsp; :thumbsdown: 86

---

### My Solution


### Description
<p>Given a <b>non-empty</b> array <code>nums</code> containing <b>only positive integers</b>, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,11,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be partitioned as [1, 5, 5] and [11].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> The array cannot be partitioned into equal sum subsets.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 744 ms
- Completed time: 2019-12-05 09:11:46

```Python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num

        if sum % 2 == 0:
            sum = int(sum / 2)
        else:
            return False

        dp = [False] * (sum + 1)
        dp[0] = True

        for num in nums:
            for i in range(sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[sum]        
```


### Related Problems
[Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) (Medium) <br>



### What a(n) Medium problem!
Among **557708** total submissions, **249428** are accepted, with an acceptance rate of **44.7%**. <br>

- Likes: 3806
- Dislikes: 86

