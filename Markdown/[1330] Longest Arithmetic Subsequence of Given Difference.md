# [1330] Longest Arithmetic Subsequence of Given Difference (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/) 

:+1: 442 &nbsp; &nbsp; :thumbsdown: 30

---

### My Solution


### Description
<p>Given an integer array <code>arr</code>&nbsp;and an integer <code><font face="monospace">difference</font></code>, return the length of the longest subsequence in <font face="monospace"><code>arr</code>&nbsp;</font>which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals&nbsp;<code>difference</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4], difference = 1
<strong>Output:</strong> 4
<strong>Explanation: </strong>The longest arithmetic subsequence is [1,2,3,4].</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,5,7], difference = 1
<strong>Output:</strong> 1
<strong>Explanation: </strong>The longest arithmetic subsequence is any single element.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,5,7,8,5,3,4,2,1], difference = -2
<strong>Output:</strong> 4
<strong>Explanation: </strong>The longest arithmetic subsequence is [7,5,3,1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>-10^4 &lt;= arr[i], difference &lt;= 10^4</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 520 ms
- Completed time: 2020-11-02 19:29:32

```Python
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        
        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
        
        return max(dp.values())
```


### Related Problems




### What a(n) Medium problem!
Among **47889** total submissions, **22224** are accepted, with an acceptance rate of **46.4%**. <br>

- Likes: 442
- Dislikes: 30

