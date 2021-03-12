# [14] Longest Common Prefix (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/longest-common-prefix/) 

:+1: 3809 &nbsp; &nbsp; :thumbsdown: 2157

---

### My Solution


### Description
<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lower-case English letters.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 32 ms
- Completed time: 2020-09-08 09:13:50

```Python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = min(strs, key=len)
        
        for i, ch in enumerate(prefix):
            for string in strs:
                if string[i] != ch:
                    prefix = prefix[:i]
                
        return prefix
```


### Related Problems




### What a(n) Easy problem!
Among **2675942** total submissions, **967105** are accepted, with an acceptance rate of **36.1%**. <br>

- Likes: 3809
- Dislikes: 2157

