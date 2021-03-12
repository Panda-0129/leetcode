# [39] Combination Sum (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/combination-sum/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/combination-sum/) 

:+1: 5554 &nbsp; &nbsp; :thumbsdown: 144

---

### My Solution


### Description
<p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the frequency of at least one of the chosen numbers is different.</p>

<p>It is <strong>guaranteed</strong> that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> candidates = [1], target = 1
<strong>Output:</strong> [[1]]
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> candidates = [1], target = 2
<strong>Output:</strong> [[1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>1 &lt;= candidates[i] &lt;= 200</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 500</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 52 ms
- Completed time: 2020-09-25 16:23:47

```Python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, s, cur_solution, res):
            if target == 0:
                res.append(cur_solution[:])
                return

            for i in range(s, len(candidates)):
                if candidates[i] > target:
                    return
                cur_solution.append(candidates[i])
                dfs(candidates, target - candidates[i], i, cur_solution, res)
                cur_solution.pop()

        cur_solution = []
        res = []
        candidates.sort()
        dfs(candidates, target, 0, cur_solution, res)

        return res
```


### Related Problems
[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (Medium) <br>
[Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) (Medium) <br>
[Combinations](https://leetcode.com/problems/combinations/) (Medium) <br>
[Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) (Medium) <br>
[Factor Combinations](https://leetcode.com/problems/factor-combinations/) (Medium) <br>
[Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) (Medium) <br>



### What a(n) Medium problem!
Among **1173579** total submissions, **697156** are accepted, with an acceptance rate of **59.4%**. <br>

- Likes: 5554
- Dislikes: 144

