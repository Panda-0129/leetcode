# [395] Longest Substring with At Least K Repeating Characters (Medium)

[![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)  [![Recursion_badge](https://img.shields.io/badge/topic-Recursion-green.svg)](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)  [![Sliding%20Window_badge](https://img.shields.io/badge/topic-Sliding%20Window-green.svg)](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) 

:+1: 2162 &nbsp; &nbsp; :thumbsdown: 249

---

### My Solution


### Description
<p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the length of the longest substring of</em> <code>s</code> <em>such that the frequency of each character in this substring is greater than or equal to</em> <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabb&quot;, k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest substring is &quot;aaa&quot;, as &#39;a&#39; is repeated 3 times.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababbc&quot;, k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest substring is &quot;ababb&quot;, as &#39;a&#39; is repeated 2 times and &#39;b&#39; is repeated 3 times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 28 ms
- Completed time: 2019-04-04 21:30:28

```Python
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
    
        
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
            
        return len(s)
```


### Related Problems




### What a(n) Medium problem!
Among **252715** total submissions, **109526** are accepted, with an acceptance rate of **43.3%**. <br>

- Likes: 2162
- Dislikes: 249

