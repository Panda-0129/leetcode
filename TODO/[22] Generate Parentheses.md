# [22] Generate Parentheses (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/generate-parentheses/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/generate-parentheses/) 

:+1: 7307 &nbsp; &nbsp; :thumbsdown: 315

---

### My Solution


### Description
<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2021-03-09 10:35:05

```Python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ["(" + x + ")" + y for x in dp[j] for y in dp[i - j - 1]]
        
        return dp[n]
```


### Related Problems
[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (Medium) <br>
[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) <br>



### What a(n) Medium problem!
Among **1068957** total submissions, **699637** are accepted, with an acceptance rate of **65.5%**. <br>

- Likes: 7307
- Dislikes: 315

