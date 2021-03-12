# [77] Combinations (Medium)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/combinations/) 

:+1: 2082 &nbsp; &nbsp; :thumbsdown: 80

---

### My Solution


### Description
<p>Given two integers <em>n</em> and <em>k</em>, return all possible combinations of <em>k</em> numbers out of 1 ... <em>n</em>.</p>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, k = 2
<strong>Output:</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 460 ms
- Completed time: 2020-09-27 10:45:09

```Python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(begin, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(begin, n):
                
                path.append(i + 1)
                dfs(i + 1, path)
                path.pop()
            
        res = []
        dfs(0, [])
        
        return res
```


### Related Problems
[Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) <br>
[Permutations](https://leetcode.com/problems/permutations/) (Medium) <br>



### What a(n) Medium problem!
Among **607465** total submissions, **350039** are accepted, with an acceptance rate of **57.6%**. <br>

- Likes: 2082
- Dislikes: 80

