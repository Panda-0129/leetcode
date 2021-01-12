# [1250] Longest Common Subsequence (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/longest-common-subsequence/) 

:+1: 2397 &nbsp; &nbsp; :thumbsdown: 29

---

### My Solution


### Description
<p>Given two strings <code>text1</code> and <code>text2</code>, return the length of their longest common subsequence.</p>

<p>A <em>subsequence</em> of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, &quot;ace&quot; is a subsequence of &quot;abcde&quot; while &quot;aec&quot; is not).&nbsp;A <em>common subsequence</em>&nbsp;of two strings is a subsequence that is common to both strings.</p>

<p>&nbsp;</p>

<p>If there is no common subsequence, return 0.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abcde&quot;, text2 = &quot;ace&quot; 
<strong>Output:</strong> 3  
<strong>Explanation:</strong> The longest common subsequence is &quot;ace&quot; and its length is 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest common subsequence is &quot;abc&quot; and its length is 3.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;def&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no such common subsequence, so the result is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text1.length &lt;= 1000</code></li>
	<li><code>1 &lt;= text2.length &lt;= 1000</code></li>
	<li>The input strings consist of lowercase English characters only.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 432 ms
- Completed time: 2019-10-16 10:14:48

```Python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for __ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
```


### Related Problems
[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) (Medium) <br>
[Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) (Medium) <br>
[Shortest Common Supersequence ](https://leetcode.com/problems/shortest-common-supersequence/) (Hard) <br>



### What a(n) Medium problem!
Among **286609** total submissions, **167935** are accepted, with an acceptance rate of **58.6%**. <br>

- Likes: 2397
- Dislikes: 29

