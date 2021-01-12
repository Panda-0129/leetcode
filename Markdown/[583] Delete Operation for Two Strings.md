# [583] Delete Operation for Two Strings (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/delete-operation-for-two-strings/) 

:+1: 1330 &nbsp; &nbsp; :thumbsdown: 31

---

### My Solution


### Description
<p>
Given two words <i>word1</i> and <i>word2</i>, find the minimum number of steps required to make <i>word1</i> and <i>word2</i> the same, where in each step you can delete one character in either string.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "sea", "eat"
<b>Output:</b> 2
<b>Explanation:</b> You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of given words won't exceed 500.</li>
<li>Characters in given words can only be lower-case letters.</li>
</ol>
</p>


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
Among **118156** total submissions, **58742** are accepted, with an acceptance rate of **49.7%**. <br>

- Likes: 1330
- Dislikes: 31

