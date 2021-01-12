# [800] Letter Case Permutation (Medium)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/letter-case-permutation/)  [![Bit%20Manipulation_badge](https://img.shields.io/badge/topic-Bit%20Manipulation-green.svg)](https://leetcode.com/problems/letter-case-permutation/) 

:+1: 1626 &nbsp; &nbsp; :thumbsdown: 115

---

### My Solution


### Description
<p>Given a string S, we can transform every letter individually&nbsp;to be lowercase or uppercase to create another string.</p>

<p>Return <em>a list of all possible strings we could create</em>. You can return the output&nbsp;in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;a1b2&quot;
<strong>Output:</strong> [&quot;a1b2&quot;,&quot;a1B2&quot;,&quot;A1b2&quot;,&quot;A1B2&quot;]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;3z4&quot;
<strong>Output:</strong> [&quot;3z4&quot;,&quot;3Z4&quot;]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;12345&quot;
<strong>Output:</strong> [&quot;12345&quot;]
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;0&quot;
<strong>Output:</strong> [&quot;0&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>S</code> will be a string with length between <code>1</code> and <code>12</code>.</li>
	<li><code>S</code> will consist only of letters or digits.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 52 ms
- Completed time: 2019-10-15 12:28:13

```Python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [res_sub + ch.upper() for res_sub in res] + [res_sub + ch.lower() for res_sub in res]
            else:
                res = [res_sub + ch for res_sub in res]    
        return res
```


### Related Problems
[Subsets](https://leetcode.com/problems/subsets/) (Medium) <br>
[Brace Expansion](https://leetcode.com/problems/brace-expansion/) (Medium) <br>



### What a(n) Medium problem!
Among **164113** total submissions, **108552** are accepted, with an acceptance rate of **66.1%**. <br>

- Likes: 1626
- Dislikes: 115

