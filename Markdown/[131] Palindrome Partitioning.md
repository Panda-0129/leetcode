# [131] Palindrome Partitioning (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/palindrome-partitioning/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/palindrome-partitioning/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/palindrome-partitioning/) 

:+1: 2831 &nbsp; &nbsp; :thumbsdown: 91

---

### My Solution


### Description
<p>Given a string <code>s</code>, partition <code>s</code> such that every substring of the partition is a <strong>palindrome</strong>. Return all possible palindrome partitioning of <code>s</code>.</p>

<p>A <strong>palindrome</strong> string is a string that reads the same backward as forward.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 72 ms
- Completed time: 2020-10-20 10:20:56

```Python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
            
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]], res)
                
            
        def isPalindrome(s):
            return s == s[::-1]
        
        res = []
        dfs(s, [], res)
        
        return res
```


### Related Problems
[Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) (Hard) <br>



### What a(n) Medium problem!
Among **555348** total submissions, **284711** are accepted, with an acceptance rate of **51.3%**. <br>

- Likes: 2831
- Dislikes: 91

