# [216] Combination Sum III (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/combination-sum-iii/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/combination-sum-iii/) 

:+1: 1600 &nbsp; &nbsp; :thumbsdown: 62

---

### My Solution


### Description
<p>Find all valid combinations of <code>k</code> numbers that sum up to <code>n</code> such that the following conditions are true:</p>

<ul>
	<li>Only numbers <code>1</code> through <code>9</code> are used.</li>
	<li>Each number is used <strong>at most once</strong>.</li>
</ul>

<p>Return <em>a list of all possible valid combinations</em>. The list must not contain the same combination twice, and the combinations may be returned in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 7
<strong>Output:</strong> [[1,2,4]]
<strong>Explanation:</strong>
1 + 2 + 4 = 7
There are no other valid combinations.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 9
<strong>Output:</strong> [[1,2,6],[1,3,5],[2,3,4]]
<strong>Explanation:</strong>
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 4, n = 1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 2
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid combinations.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> k = 9, n = 45
<strong>Output:</strong> [[1,2,3,4,5,6,7,8,9]]
<strong>Explanation:</strong>
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 32 ms
- Completed time: 2020-09-28 10:59:48

```Python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(begin, path, target):
            if len(path) == k and target == 0:
                res.append(path[:])
                return
            
            for i in range(begin, 9):
                if target < i + 1:
                    return
                path.append(i + 1)
                dfs(i + 1, path, target - i - 1)
                path.pop()
        
        res = []
        dfs(0, [], n)
        
        return res
```


### Related Problems
[Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) <br>



### What a(n) Medium problem!
Among **354394** total submissions, **212194** are accepted, with an acceptance rate of **59.9%**. <br>

- Likes: 1600
- Dislikes: 62

