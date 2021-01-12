# [567] Permutation in String (Medium)

[![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/permutation-in-string/)  [![Sliding%20Window_badge](https://img.shields.io/badge/topic-Sliding%20Window-green.svg)](https://leetcode.com/problems/permutation-in-string/) 

:+1: 2072 &nbsp; &nbsp; :thumbsdown: 75

---

### My Solution


### Description
<p>Given two strings <b>s1</b> and <b>s2</b>, write a function to return true if <b>s2</b> contains the permutation of <b>s1</b>. In other words, one of the first string&#39;s permutations is the <b>substring</b> of the second string.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input: </b>s1 = &quot;ab&quot; s2 = &quot;eidbaooo&quot;
<b>Output: </b>True
<b>Explanation:</b> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>s1= &quot;ab&quot; s2 = &quot;eidboaoo&quot;
<b>Output:</b> False
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The input strings only contain lower case letters.</li>
	<li>The length of both given strings is in range [1, 10,000].</li>
</ul>



### My Submission

- Language: Python
- Runtime: 76 ms
- Completed time: 2020-09-21 15:51:49

```Python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right, valid = 0, 0, 0
        request = dict.fromkeys(list(s1), 0)
        inside = dict.fromkeys(list(s2), 0)
        
        for ch in s1:
            request[ch] += 1

        while right < len(s2):

            ch_in = s2[right]
            right += 1

            if ch_in in request:
                inside[ch_in] += 1
                if inside[ch_in] == request[ch_in]:
                    valid += 1

            while right - left >= len(s1):
                if valid == len(request):
                    return True
                ch_out = s2[left]
                left += 1
                if ch_out in request:
                    if inside[ch_out] == request[ch_out]:
                        valid -= 1
                    inside[ch_out] -= 1
        
        return False
```


### Related Problems
[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard) <br>
[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Medium) <br>



### What a(n) Medium problem!
Among **376225** total submissions, **167630** are accepted, with an acceptance rate of **44.6%**. <br>

- Likes: 2072
- Dislikes: 75

