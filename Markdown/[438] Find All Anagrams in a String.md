# [438] Find All Anagrams in a String (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/find-all-anagrams-in-a-string/) 

:+1: 3765 &nbsp; &nbsp; :thumbsdown: 194

---

### My Solution


### Description
<p>Given a string <b>s</b> and a <b>non-empty</b> string <b>p</b>, find all the start indices of <b>p</b>'s anagrams in <b>s</b>.</p>

<p>Strings consists of lowercase English letters only and the length of both strings <b>s</b> and <b>p</b> will not be larger than 20,100.</p>

<p>The order of output does not matter.</p>

<p><b>Example 1:</b>
<pre>
<b>Input:</b>
s: "cbaebabacd" p: "abc"

<b>Output:</b>
[0, 6]

<b>Explanation:</b>
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
</pre>
</p>

<p><b>Example 2:</b>
<pre>
<b>Input:</b>
s: "abab" p: "ab"

<b>Output:</b>
[0, 1, 2]

<b>Explanation:</b>
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
</pre>
</p>


### My Submission

- Language: Python
- Runtime: 120 ms
- Completed time: 2020-09-21 16:00:08

```Python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right, valid = 0, 0, 0
        request = dict.fromkeys(list(p), 0)
        inside = dict.fromkeys(list(s), 0)
        res = []
        
        for ch in p:
            request[ch] += 1

        while right < len(s):

            ch_in = s[right]
            right += 1

            if ch_in in request:
                inside[ch_in] += 1
                if inside[ch_in] == request[ch_in]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(request):
                    res.append(left)
                ch_out = s[left]
                left += 1
                if ch_out in request:
                    if inside[ch_out] == request[ch_out]:
                        valid -= 1
                    inside[ch_out] -= 1
        
        return res
```


### Related Problems
[Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy) <br>
[Permutation in String](https://leetcode.com/problems/permutation-in-string/) (Medium) <br>



### What a(n) Medium problem!
Among **734019** total submissions, **327608** are accepted, with an acceptance rate of **44.6%**. <br>

- Likes: 3765
- Dislikes: 194

