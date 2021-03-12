# [242] Valid Anagram (Easy)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/valid-anagram/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/valid-anagram/) 

:+1: 2389 &nbsp; &nbsp; :thumbsdown: 160

---

### My Solution


### Description
<p>Given two strings <em>s</em> and <em>t&nbsp;</em>, write a function to determine if <em>t</em> is an anagram of <em>s</em>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <em>s</em> = &quot;anagram&quot;, <em>t</em> = &quot;nagaram&quot;
<b>Output:</b> true
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <em>s</em> = &quot;rat&quot;, <em>t</em> = &quot;car&quot;
<b>Output: </b>false
</pre>

<p><strong>Note:</strong><br />
You may assume the string contains only lowercase alphabets.</p>

<p><strong>Follow up:</strong><br />
What if the inputs contain unicode characters? How would you adapt your solution to such case?</p>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-09-04 23:08:04

```Python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        tmp = [0] * 26
        
        for ch in s:
            tmp[ord(ch) - ord('a')] +=1
        for ch in t:
            tmp[ord(ch) - ord('a')] -= 1
                
        return all(count == 0 for count in tmp)
```


### Related Problems
[Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium) <br>
[Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) (Easy) <br>
[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Medium) <br>



### What a(n) Easy problem!
Among **1316572** total submissions, **772286** are accepted, with an acceptance rate of **58.7%**. <br>

- Likes: 2389
- Dislikes: 160

