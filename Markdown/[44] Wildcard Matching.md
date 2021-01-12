# [44] Wildcard Matching (Hard)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/wildcard-matching/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/wildcard-matching/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/wildcard-matching/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/wildcard-matching/) 

:+1: 2611 &nbsp; &nbsp; :thumbsdown: 126

---

### My Solution


### Description
<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement wildcard pattern matching with support for <code>&#39;?&#39;</code> and <code>&#39;*&#39;</code> where:</p>

<ul>
	<li><code>&#39;?&#39;</code> Matches any single character.</li>
	<li><code>&#39;*&#39;</code> Matches any sequence of characters (including the empty sequence).</li>
</ul>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; matches any sequence.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cb&quot;, p = &quot;?a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong>&nbsp;&#39;?&#39; matches &#39;c&#39;, but the second letter is &#39;a&#39;, which does not match &#39;b&#39;.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;adceb&quot;, p = &quot;*a*b&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;The first &#39;*&#39; matches the empty sequence, while the second &#39;*&#39; matches the substring &quot;dce&quot;.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;acdcb&quot;, p = &quot;a*c?b&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length, p.length &lt;= 2000</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>&#39;?&#39;</code> or <code>&#39;*&#39;</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 812 ms
- Completed time: 2020-11-05 11:01:14

```Python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "*":
            return True

        len_row = len(p) + 1
        len_col = len(s) + 1

        dp = [[False for _ in range(len_col)] for _ in range(len_row)]
        dp[0][0] = True

        for i in range(1, len_row):
            if p[i - 1] != "*":
                break
            dp[i][0] = True

        for row in range(1, len_row):
            i = row - 1
            for col in range(1, len_col):
                j = col - 1

                if p[i] == s[j] or p[i] == "?":
                    dp[row][col] = dp[i][j]
                if p[i] == "*":
                    dp[row][col] = dp[i][col] or dp[row][j]

        return dp[len_row - 1][len_col - 1]
```


### Related Problems
[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) (Hard) <br>



### What a(n) Hard problem!
Among **1110260** total submissions, **280644** are accepted, with an acceptance rate of **25.3%**. <br>

- Likes: 2611
- Dislikes: 126

