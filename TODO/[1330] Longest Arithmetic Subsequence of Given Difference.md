# [1330] Longest Arithmetic Subsequence of Given Difference (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)  [![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/) 

:+1: 492 &nbsp; &nbsp; :thumbsdown: 30

---

### My Solution


### Description
<p>Given an integer array <code>arr</code> and an integer <code>difference</code>, return the length of the longest subsequence in <code>arr</code> which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals <code>difference</code>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from <code>arr</code> by deleting some or no elements without changing the order of the remaining elements.</p>

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
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= arr[i], difference &lt;= 10<sup>4</sup></code></li>
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
Among **50959** total submissions, **23784** are accepted, with an acceptance rate of **46.7%**. <br>

- Likes: 492
- Dislikes: 30

