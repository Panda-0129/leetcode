# [40] Combination Sum II (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/combination-sum-ii/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/combination-sum-ii/) 

:+1: 2543 &nbsp; &nbsp; :thumbsdown: 86

---

### My Solution


### Description
<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2020-09-27 10:01:28

```Python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, target):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(begin, length):
                if candidates[i] > target:
                    break
                
                if i > begin and candidates[i - 1] == candidates[i]:
                    continue 
                
                path.append(candidates[i])
                dfs(i + 1, path, target - candidates[i])
                path.pop()
            
        length = len(candidates)
        candidates.sort()
        res = []
        path = []
        dfs(0, path, target)
            
        return res
```


### Related Problems
[Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) <br>



### What a(n) Medium problem!
Among **782210** total submissions, **392817** are accepted, with an acceptance rate of **50.2%**. <br>

- Likes: 2543
- Dislikes: 86

