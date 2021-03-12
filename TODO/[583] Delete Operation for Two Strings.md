# [583] Delete Operation for Two Strings (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/delete-operation-for-two-strings/) 

:+1: 1419 &nbsp; &nbsp; :thumbsdown: 34

---

### My Solution


### Description
<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of <strong>steps</strong> required to make</em> <code>word1</code> <em>and</em> <code>word2</code> <em>the same</em>.</p>

<p>In one <strong>step</strong>, you can delete exactly one character in either string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;sea&quot;, word2 = &quot;eat&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need one step to make &quot;sea&quot; to &quot;ea&quot; and another step to make &quot;eat&quot; to &quot;ea&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;leetcode&quot;, word2 = &quot;etco&quot;
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of only lowercase English letters.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 344 ms
- Completed time: 2020-11-10 09:26:50

```Python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_row = len(word1) + 1
        len_col = len(word2) + 1
        
        dp = [[0 for _ in range(len_col)] for _ in range(len_row)]
        
        for i in range(len_row):
            dp[i][0] = i
        
        for j in range(len_col):
            dp[0][j] = j
        
        for i in range(1, len_row):
            for j in range(1, len_col):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        
        return dp[-1][-1]
```


### Related Problems
[Edit Distance](https://leetcode.com/problems/edit-distance/) (Hard) <br>
[Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) (Medium) <br>
[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (Medium) <br>



### What a(n) Medium problem!
Among **123102** total submissions, **61706** are accepted, with an acceptance rate of **50.1%**. <br>

- Likes: 1419
- Dislikes: 34

