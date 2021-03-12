# [712] Minimum ASCII Delete Sum for Two Strings (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) 

:+1: 1257 &nbsp; &nbsp; :thumbsdown: 54

---

### My Solution


### Description
<p>Given two strings <code>s1, s2</code>, find the lowest ASCII sum of deleted characters to make two strings equal.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> s1 = "sea", s2 = "eat"
<b>Output:</b> 231
<b>Explanation:</b> Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> s1 = "delete", s2 = "leet"
<b>Output:</b> 403
<b>Explanation:</b> Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < s1.length, s2.length <= 1000</code>.</li>
<li>All elements of each string will have an ASCII value in <code>[97, 122]</code>.</li> 
</p>


### My Submission

- Language: Python
- Runtime: 1108 ms
- Completed time: 2020-11-11 10:31:38

```Python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len_row = len(s1) + 1
        len_col = len(s2) + 1

        dp = [[0 for _ in range(len_col)] for _ in range(len_row)]

        for i in range(1, len_row):
            dp[i][0] = ord(s1[i - 1]) + dp[i - 1][0]

        for j in range(1, len_col):
            dp[0][j] = ord(s2[j - 1]) + dp[0][j - 1]

        for i in range(1, len_row):
            for j in range(1, len_col):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]), dp[i - 1][j - 1] + ord(s1[i - 1]) + ord(s2[j - 1]))

        return dp[-1][-1]
```


### Related Problems
[Edit Distance](https://leetcode.com/problems/edit-distance/) (Hard) <br>
[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (Medium) <br>
[Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) (Medium) <br>



### What a(n) Medium problem!
Among **74260** total submissions, **44196** are accepted, with an acceptance rate of **59.5%**. <br>

- Likes: 1257
- Dislikes: 54

