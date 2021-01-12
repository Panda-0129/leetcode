# [10] Regular Expression Matching (Hard)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/regular-expression-matching/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/regular-expression-matching/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/regular-expression-matching/) 

:+1: 5206 &nbsp; &nbsp; :thumbsdown: 810

---

### My Solution


### Description
<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement regular expression matching with support for <code>&#39;.&#39;</code> and <code>&#39;*&#39;</code> where:<code>&nbsp;</code></p>

<ul>
	<li><code>&#39;.&#39;</code> Matches any single character.​​​​</li>
	<li><code>&#39;*&#39;</code> Matches zero or more of the preceding element.</li>
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
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; means zero or more of the preceding&nbsp;element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab&quot;, p = &quot;.*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aab&quot;, p = &quot;c*a*b&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches &quot;aab&quot;.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;mississippi&quot;, p = &quot;mis*is*p*.&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length&nbsp;&lt;= 20</code></li>
	<li><code>0 &lt;= p.length&nbsp;&lt;= 30</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>&#39;.&#39;</code>, and&nbsp;<code>&#39;*&#39;</code>.</li>
	<li>It is guaranteed for each appearance of the character <code>&#39;*&#39;</code>, there will be a previous valid character to match.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 48 ms
- Completed time: 2020-11-04 10:55:35

```Python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        if not s and len(p) == 1:
            return False

        len_row = len(s) + 1
        len_col = len(p) + 1

        dp = [[False for col in range(len_col)] for row in range(len_row)]

        dp[0][0] = True

        for col in range(2, len_col):
            j = col - 1
            if p[j] == "*":
                dp[0][col] = dp[0][col - 2]

        for row in range(1, len_row):
            i = row - 1
            for col in range(1, len_col):
                j = col - 1

                if s[i] == p[j] or p[j] == ".":
                    dp[row][col] = dp[row - 1][col - 1]

                elif p[j] == "*":
                    if p[j - 1] == s[i] or p[j - 1] == ".":
                        dp[row][col] = dp[row - 1][col] or dp[row][col - 2]
                    else:
                        dp[row][col] = dp[row][col - 2]
                else:
                    dp[row][col] = False

        return dp[len_row - 1][len_col - 1]
```


### Related Problems
[Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) (Hard) <br>



### What a(n) Hard problem!
Among **1830883** total submissions, **498165** are accepted, with an acceptance rate of **27.2%**. <br>

- Likes: 5206
- Dislikes: 810

