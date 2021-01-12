# [345] Reverse Vowels of a String (Easy)

[![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/reverse-vowels-of-a-string/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/reverse-vowels-of-a-string/) 

:+1: 874 &nbsp; &nbsp; :thumbsdown: 1367

---

### My Solution


### Description
<p>Write a function that takes a string as input and reverse only the vowels of a string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;hello&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;holle&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;leetcode&quot;</span>
<strong>Output: </strong><span id="example-output-2">&quot;leotcede&quot;</span></pre>
</div>

<p><b>Note:</b><br />
The vowels does not include the letter &quot;y&quot;.</p>

<p>&nbsp;</p>



### My Submission

- Language: Python
- Runtime: 76 ms
- Completed time: 2019-03-23 23:07:12

```Python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        res = ['NA'] * len(s)
        while i <= j:
            if s[i] not in vowels:
                res[i] = s[i]
                i+=1
            elif s[j] not in vowels:
                res[j] = s[j]
                j-=1
            else:
                res[i] = s[j]
                res[j] = s[i]
                i+=1
                j-=1
        return ("".join(res))
        
```


### Related Problems
[Reverse String](https://leetcode.com/problems/reverse-string/) (Easy) <br>
[Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string/) (Easy) <br>



### What a(n) Easy problem!
Among **569161** total submissions, **255511** are accepted, with an acceptance rate of **44.9%**. <br>

- Likes: 874
- Dislikes: 1367

