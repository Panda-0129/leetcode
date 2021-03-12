# [524] Longest Word in Dictionary through Deleting (Medium)

[![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) 

:+1: 961 &nbsp; &nbsp; :thumbsdown: 295

---

### My Solution


### Description
<p>Given a string <code>s</code> and a string array <code>dictionary</code>, return <em>the longest string in the dictionary that can be formed by deleting some of the given string characters</em>. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abpcplea&quot;, dictionary = [&quot;ale&quot;,&quot;apple&quot;,&quot;monkey&quot;,&quot;plea&quot;]
<strong>Output:</strong> &quot;apple&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abpcplea&quot;, dictionary = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
<strong>Output:</strong> &quot;a&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 1000</code></li>
	<li><code>s</code> and <code>dictionary[i]</code> consist of lowercase English letters.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 732 ms
- Completed time: 2019-03-24 20:56:08

```Python
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        
        if len(d) == 0:
            return ""
        
        def isSubstring(s, dString):
            i, j = 0, 0
            while i < len(s) and j < len(dString):
                if s[i] == dString[j]:
                    j += 1
                if j == len(dString):
                    return True
                i += 1
            return False

        isTrue = []
        d.sort()

        for i in range(0, len(d)):
            if isSubstring(s, d[i]):
                isTrue.append(i)

        if len(isTrue) == 0:
            return ""
        
        maxLength = 0
        maxPos = 0
        for pos in isTrue:
            if len(d[pos]) > maxLength:
                maxLength = len(d[pos])
                maxPos = pos

        return d[maxPos]
```


### Related Problems
[Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) (Easy) <br>



### What a(n) Medium problem!
Among **203708** total submissions, **101998** are accepted, with an acceptance rate of **50.1%**. <br>

- Likes: 961
- Dislikes: 295

