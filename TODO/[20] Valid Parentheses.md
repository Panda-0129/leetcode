# [20] Valid Parentheses (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/valid-parentheses/)  [![Stack_badge](https://img.shields.io/badge/topic-Stack-green.svg)](https://leetcode.com/problems/valid-parentheses/) 

:+1: 6987 &nbsp; &nbsp; :thumbsdown: 288

---

### My Solution


### Description
<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;([)]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;{[]}&quot;
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2021-03-08 20:14:30

```Python
class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        
        for char in s:
            if char in valid_dict.values():
                stack.append(char)
            elif char in valid_dict.keys():
                if stack == [] or stack.pop() != valid_dict[char]:
                    return False
            else:
                return False
        
        return stack == []
        
                
```


### Related Problems
[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium) <br>
[Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) (Hard) <br>
[Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) (Hard) <br>
[Check If Word Is Valid After Substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) (Medium) <br>



### What a(n) Easy problem!
Among **3355050** total submissions, **1339111** are accepted, with an acceptance rate of **39.9%**. <br>

- Likes: 6987
- Dislikes: 288

