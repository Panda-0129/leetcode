# [97] Interleaving String (Hard)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/interleaving-string/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/interleaving-string/) 

:+1: 1803 &nbsp; &nbsp; :thumbsdown: 100

---

### My Solution


### Description
<p>Given strings <code>s1</code>, <code>s2</code>, and <code>s3</code>, find whether <code>s3</code> is formed by an <strong>interleaving</strong> of <code>s1</code> and <code>s2</code>.</p>

<p>An <strong>interleaving</strong> of two strings <code>s</code> and <code>t</code> is a configuration where they are divided into <strong>non-empty</strong> substrings such that:</p>

<ul>
	<li><code>s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub></code></li>
	<li><code>t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub></code></li>
	<li><code>|n - m| &lt;= 1</code></li>
	<li>The <strong>interleaving</strong> is <code>s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...</code> or <code>t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...</code></li>
</ul>

<p><strong>Note:</strong> <code>a + b</code> is the concatenation of strings <code>a</code> and <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg" style="width: 561px; height: 203px;" />
<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, s3 = &quot;aadbbcbcac&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, s3 = &quot;aadbbbaccc&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;&quot;, s2 = &quot;&quot;, s3 = &quot;&quot;
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>0 &lt;= s3.length &lt;= 200</code></li>
	<li><code>s1</code>, <code>s2</code>, and <code>s3</code> consist of lower-case English letters.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2020-11-06 10:42:58

```Python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        len_col = len(s2) + 1
        len_row = len(s1) + 1

        dp = [[False for _ in range(len_col)] for _ in range(len_row)]

        dp[0][0] = True
        for col in range(1, len_col):
            dp[0][col] = dp[0][col - 1] and s2[col - 1] == s3[col - 1]
        for row in range(1, len_row):
            dp[row][0] = dp[row - 1][0] and s1[row - 1] == s3[row - 1]

        for row in range(1, len_row):
            for col in range(1, len_col):
                dp[row][col] = (dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]) or (
                        dp[row][col - 1] and s2[col - 1] == s3[row + col - 1])

        return dp[-1][-1]
```


### Related Problems




### What a(n) Hard problem!
Among **529945** total submissions, **171551** are accepted, with an acceptance rate of **32.4%**. <br>

- Likes: 1803
- Dislikes: 100

