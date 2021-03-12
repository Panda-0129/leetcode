# [680] Valid Palindrome II (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/valid-palindrome-ii/) 

:+1: 2382 &nbsp; &nbsp; :thumbsdown: 145

---

### My Solution


### Description
<p>
Given a non-empty string <code>s</code>, you may delete <b>at most</b> one character.  Judge whether you can make it a palindrome.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aba"
<b>Output:</b> True
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "abca"
<b>Output:</b> True
<b>Explanation:</b> You could delete the character 'c'.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.</li>
</ol>
</p>


### My Submission

- Language: Python
- Runtime: 188 ms
- Completed time: 2019-03-23 23:56:13

```Python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(self, s):
            i, j = 0, len(s) - 1
            while i <= j:
               if s[i] != s[j]:
                   return False
               i+=1
               j-=1
            return True
        
        left,  right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(self, s[left + 1:right + 1]) or isPalindrome(self, s[left:right])
            left+=1
            right-=1
        return True
```


### Related Problems
[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy) <br>



### What a(n) Easy problem!
Among **660316** total submissions, **244847** are accepted, with an acceptance rate of **37.1%**. <br>

- Likes: 2382
- Dislikes: 145

