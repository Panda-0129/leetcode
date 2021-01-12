# [387] First Unique Character in a String (Easy)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/first-unique-character-in-a-string/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/first-unique-character-in-a-string/) 

:+1: 2532 &nbsp; &nbsp; :thumbsdown: 129

---

### My Solution


### Description
<p>Given a string, find the first non-repeating character in it and return its index. If it doesn&#39;t exist, return -1.</p>

<p><b>Examples:</b></p>

<pre>
s = &quot;leetcode&quot;
return 0.

s = &quot;loveleetcode&quot;
return 2.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> You may assume the string contains only lowercase English letters.</p>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-04-03 22:06:32

```Python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = "abcdefghijklmnopqrstuvwxyz"
        
        index = [s.index(c) for c in dic if s.count(c) == 1]
            
        return min(index) if len(index) != 0 else -1
```


### Related Problems
[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) (Medium) <br>



### What a(n) Easy problem!
Among **1224311** total submissions, **657589** are accepted, with an acceptance rate of **53.7%**. <br>

- Likes: 2532
- Dislikes: 129

