# [392] Is Subsequence (Easy)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/is-subsequence/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/is-subsequence/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/is-subsequence/) 

:+1: 2277 &nbsp; &nbsp; :thumbsdown: 229

---

### My Solution


### Description
<p>Given two strings <code>s</code> and <code>t</code>, check if <code>s</code> is a <strong>subsequence</strong> of <code>t</code>.</p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code>&nbsp;consist&nbsp;only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If there are lots of incoming <code>s</code>, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if <code>t</code> has its subsequence. In this scenario, how would you change your code?


### My Submission

- Language: Python
- Runtime: 252 ms
- Completed time: 2019-03-31 21:19:15

```Python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        i, j = 0, 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i+=1
            j+=1
    
        return i == len(s)
```


### Related Problems
[Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) (Medium) <br>
[Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/) (Medium) <br>



### What a(n) Easy problem!
Among **564320** total submissions, **279330** are accepted, with an acceptance rate of **49.5%**. <br>

- Likes: 2277
- Dislikes: 229

