# [494] Target Sum (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/target-sum/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/target-sum/) 

:+1: 3795 &nbsp; &nbsp; :thumbsdown: 155

---

### My Solution


### Description
<p>You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols <code>+</code> and <code>-</code>. For each integer, you should choose one from <code>+</code> and <code>-</code> as its new symbol.</p>

<p>Find out how many ways to assign symbols to make sum of integers equal to target S.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> nums is [1, 1, 1, 1, 1], S is 3. 
<b>Output:</b> 5
<b>Explanation:</b> 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The length of the given array is positive and will not exceed 20.</li>
	<li>The sum of elements in the given array will not exceed 1000.</li>
	<li>Your output answer is guaranteed to be fitted in a 32-bit integer.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 928 ms
- Completed time: 2020-11-18 16:41:58

```Python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        list_sum = sum(nums)

        if abs(list_sum) < abs(S):
            return 0

        len_row = len(nums)
        len_col = list_sum * 2 + 1

        dp = [[0 for _ in range(len_col)] for _ in range(len_row)]

        dp[0][list_sum + nums[0]] = 1
        dp[0][list_sum - nums[0]] += 1

        for i in range(1, len_row):
            for j in range(len_col):
                l = dp[i - 1][j - nums[i]] if len_col > j - nums[i] >= 0 else 0
                r = dp[i - 1][j + nums[i]] if len_col > j + nums[i] >= 0 else 0
                dp[i][j] = l + r

        return dp[len_row - 1][list_sum + S]
```


### Related Problems
[Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) (Hard) <br>



### What a(n) Medium problem!
Among **483302** total submissions, **220859** are accepted, with an acceptance rate of **45.7%**. <br>

- Likes: 3795
- Dislikes: 155

