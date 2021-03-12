# [32] Longest Valid Parentheses (Hard)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/longest-valid-parentheses/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/longest-valid-parentheses/) 

:+1: 4566 &nbsp; &nbsp; :thumbsdown: 171

---

### My Solution


### Description
<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, find the length of the longest valid (well-formed) parentheses substring.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)()())&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()()&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, or <code>&#39;)&#39;</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2020-11-09 21:03:41

```Python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0] * len(s) 
        
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                
                if s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i- 1] - 1] == "(":
                    dp[i] = dp[i - dp[i - 1] - 2] + 2 + dp[i - 1]
        
        return max(dp)
```


### Related Problems
[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) <br>



### What a(n) Hard problem!
Among **1165816** total submissions, **342023** are accepted, with an acceptance rate of **29.3%**. <br>

- Likes: 4566
- Dislikes: 171

