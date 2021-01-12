# [392] Is Subsequence (Easy)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/is-subsequence/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/is-subsequence/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/is-subsequence/) 

:+1: 2089 &nbsp; &nbsp; :thumbsdown: 224

---

### My Solution


### Description
<p>Given a string <b>s</b> and a string <b>t</b>, check if <b>s</b> is subsequence of <b>t</b>.</p>

<p>A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p><b>Follow up:</b><br />
If there are lots of incoming S, say S1, S2, ... , Sk where k &gt;= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?</p>

<p><b>Credits:</b><br />
Special thanks to <a href="https://leetcode.com/pbrother/">@pbrother</a> for adding this problem and creating all test cases.</p>

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
	<li><code>0 &lt;= t.length &lt;= 10^4</code></li>
	<li>Both strings consists only of lowercase characters.</li>
</ul>



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
Among **533180** total submissions, **263670** are accepted, with an acceptance rate of **49.5%**. <br>

- Likes: 2089
- Dislikes: 224

