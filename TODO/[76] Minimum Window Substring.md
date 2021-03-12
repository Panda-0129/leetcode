# [76] Minimum Window Substring (Hard)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/minimum-window-substring/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/minimum-window-substring/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/minimum-window-substring/)  [![Sliding%20Window_badge](https://img.shields.io/badge/topic-Sliding%20Window-green.svg)](https://leetcode.com/problems/minimum-window-substring/) 

:+1: 6186 &nbsp; &nbsp; :thumbsdown: 418

---

### My Solution


### Description
<p>Given two strings <code>s</code> and <code>t</code>, return <em>the minimum window in <code>s</code> which will contain all the characters in <code>t</code></em>. If there is no such window in <code>s</code> that covers all characters in <code>t</code>, return <em>the empty string <code>&quot;&quot;</code></em>.</p>

<p><strong>Note</strong> that If there is such a window, it is&nbsp;guaranteed that there will always be only one unique minimum window in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ADOBECODEBANC", t = "ABC"
<strong>Output:</strong> "BANC"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a", t = "a"
<strong>Output:</strong> "a"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(n)</code> time?


### My Submission

- Language: Python
- Runtime: 104 ms
- Completed time: 2020-09-21 15:39:04

```Python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        left, right, valid = 0, 0, 0
        request = dict.fromkeys(list(t), 0)
        inside = dict.fromkeys(list(s), 0)
        start, length = 0, sys.maxsize

        for ch in t:
            request[ch] += 1

        while right < len(s):

            ch_in = s[right]
            right += 1

            if ch_in in request:
                inside[ch_in] += 1
                if inside[ch_in] == request[ch_in]:
                    valid += 1

            while valid == len(request):
                if right - left < length:
                    start = left
                    length = right - left
                ch_out = s[left]
                left += 1
                if ch_out in request:
                    if inside[ch_out] == request[ch_out]:
                        valid -= 1
                    inside[ch_out] -= 1

        if length == sys.maxsize:
            return ""
        else:
            return s[start:start + length]
```


### Related Problems
[Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) (Hard) <br>
[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Medium) <br>
[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Hard) <br>
[Permutation in String](https://leetcode.com/problems/permutation-in-string/) (Medium) <br>
[Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) (Hard) <br>
[Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) (Hard) <br>



### What a(n) Hard problem!
Among **1406259** total submissions, **506901** are accepted, with an acceptance rate of **36.0%**. <br>

- Likes: 6186
- Dislikes: 418

