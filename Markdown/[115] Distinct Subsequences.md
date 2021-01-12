# [115] Distinct Subsequences (Hard)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/distinct-subsequences/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/distinct-subsequences/) 

:+1: 1685 &nbsp; &nbsp; :thumbsdown: 62

---

### My Solution


### Description
<p>Given two strings <code>s</code> and <code>t</code>, return <em>the&nbsp;number of distinct subsequences of <code>s</code> which equals <code>t</code></em>.</p>

<p>A string&#39;s <strong>subsequence</strong> is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ACE&quot;</code> is a subsequence of <code>&quot;ABCDE&quot;</code> while <code>&quot;AEC&quot;</code> is not).</p>

<p>It&#39;s guaranteed the answer fits on a 32-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;rabbbit&quot;, t = &quot;rabbit&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from S.
<code><strong><u>rabb</u></strong>b<strong><u>it</u></strong></code>
<code><strong><u>ra</u></strong>b<strong><u>bbit</u></strong></code>
<code><strong><u>rab</u></strong>b<strong><u>bit</u></strong></code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babgbag&quot;, t = &quot;bag&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong>
As shown below, there are 5 ways you can generate &quot;bag&quot; from S.
<code><strong><u>ba</u></strong>b<u><strong>g</strong></u>bag</code>
<code><strong><u>ba</u></strong>bgba<strong><u>g</u></strong></code>
<code><u><strong>b</strong></u>abgb<strong><u>ag</u></strong></code>
<code>ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u></code>
<code>babg<strong><u>bag</u></strong></code></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> and <code>t</code> consist of English letters.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 44 ms
- Completed time: 2020-11-10 09:02:12

```Python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_row = len(s) + 1
        len_col = len(t) + 1
        
        dp = [[0 for _ in range(len_col)] for _ in range(len_row)]
        
        for i in range(len_row):
            dp[i][0] = 1
            
        for i in range(1, len_row):
            for j in range(1, len_col):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1]
        
```


### Related Problems




### What a(n) Hard problem!
Among **389926** total submissions, **153626** are accepted, with an acceptance rate of **39.4%**. <br>

- Likes: 1685
- Dislikes: 62

