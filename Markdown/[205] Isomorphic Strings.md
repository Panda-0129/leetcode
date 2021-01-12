# [205] Isomorphic Strings (Easy)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/isomorphic-strings/) 

:+1: 1762 &nbsp; &nbsp; :thumbsdown: 435

---

### My Solution


### Description
<p>Given two strings <code>s</code> and <code>t</code>, <em>determine if they are isomorphic</em>.</p>

<p>Two strings <code>s</code> and <code>t</code> are isomorphic if the characters in <code>s</code> can be replaced to get <code>t</code>.</p>

<p>All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "egg", t = "add"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "foo", t = "bar"
<strong>Output:</strong> false
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "paper", t = "title"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>t.length == s.length</code></li>
	<li><code>s</code> and <code>t</code> consist of any valid ascii character.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 44 ms
- Completed time: 2019-10-08 10:31:13

```Python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_tmp = {}    
        for index, ch in enumerate(s):
            if ch in dict_tmp:
                if dict_tmp[ch] != t[index]:
                    return False
            elif t[index] in dict_tmp.values():
                return False
            else:
                dict_tmp[ch] = t[index]

        return True
```


### Related Problems
[Word Pattern](https://leetcode.com/problems/word-pattern/) (Easy) <br>



### What a(n) Easy problem!
Among **830977** total submissions, **335187** are accepted, with an acceptance rate of **40.3%**. <br>

- Likes: 1762
- Dislikes: 435

