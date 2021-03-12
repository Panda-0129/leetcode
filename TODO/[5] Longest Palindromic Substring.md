# [5] Longest Palindromic Substring (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/longest-palindromic-substring/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/longest-palindromic-substring/) 

:+1: 9936 &nbsp; &nbsp; :thumbsdown: 659

---

### My Solution


### Description
<p>Given a string <code>s</code>, return&nbsp;<em>the longest palindromic substring</em> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Note:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> &quot;a&quot;
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ac&quot;
<strong>Output:</strong> &quot;a&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters (lower-case and/or upper-case),</li>
</ul>


### My Submission

- Language: Python
- Runtime: 1036 ms
- Completed time: 2019-10-29 17:21:01

```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, start, end):
            while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
                start -= 1
                end += 1

            return s[start + 1:end]

        if len(s) <= 1 or not s:
            return s

        res = s[0:1]
        for i in range(len(s)):
            tmp = expand(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = expand(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp

        return res        
```


### Related Problems
[Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) (Hard) <br>
[Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) (Easy) <br>
[Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) (Hard) <br>
[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) (Medium) <br>
[Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (Medium) <br>



### What a(n) Medium problem!
Among **4037211** total submissions, **1233369** are accepted, with an acceptance rate of **30.6%**. <br>

- Likes: 9936
- Dislikes: 659

