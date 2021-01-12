# [524] Longest Word in Dictionary through Deleting (Medium)

[![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) 

:+1: 705 &nbsp; &nbsp; :thumbsdown: 257

---

### My Solution


### Description
<p>
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
</p>
<p><b>Example 1:</b><br>
<pre>
<b>Input:</b>
s = "abpcplea", d = ["ale","apple","monkey","plea"]

<b>Output:</b> 
"apple"
</pre>
</p>

</p>
<p><b>Example 2:</b><br>
<pre>
<b>Input:</b>
s = "abpcplea", d = ["a","b","c"]

<b>Output:</b> 
"a"
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>All the strings in the input will only contain lower-case letters.</li>
<li>The size of the dictionary won't exceed 1,000.</li>
<li>The length of all the strings in the input won't exceed 1,000.</li>
</ol>
</p>


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
Among **157641** total submissions, **77078** are accepted, with an acceptance rate of **48.9%**. <br>

- Likes: 705
- Dislikes: 257

