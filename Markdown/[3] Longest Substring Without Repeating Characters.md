# [3] Longest Substring Without Repeating Characters (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  [![Sliding%20Window_badge](https://img.shields.io/badge/topic-Sliding%20Window-green.svg)](https://leetcode.com/problems/longest-substring-without-repeating-characters/) 

:+1: 12635 &nbsp; &nbsp; :thumbsdown: 668

---

### My Solution


### Description
<p>Given a string <code>s</code>, find the length of the <b>longest substring</b> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-09-25 19:55:22

```Python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos, maxLength = 0, 0
        ch_dict = {}

        for index, ch in enumerate(s):
            if ch in ch_dict and pos <= ch_dict[ch]:
                pos = ch_dict[ch] + 1
            else:
                maxLength = max(maxLength, index - pos + 1)
        
            ch_dict[ch] = index
    
        return maxLength
```


### Related Problems
[Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) (Medium) <br>
[Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) (Medium) <br>
[Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) (Hard) <br>
[Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) (Medium) <br>



### What a(n) Medium problem!
Among **6228028** total submissions, **1945752** are accepted, with an acceptance rate of **31.2%**. <br>

- Likes: 12635
- Dislikes: 668

