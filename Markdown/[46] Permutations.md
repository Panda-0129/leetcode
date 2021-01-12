# [46] Permutations (Medium)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/permutations/) 

:+1: 5184 &nbsp; &nbsp; :thumbsdown: 122

---

### My Solution


### Description
<p>Given an array <code>nums</code> of distinct integers, return <em>all the possible permutations</em>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 48 ms
- Completed time: 2020-09-13 16:27:42

```Python
import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        choices = []

        def backtrack(candidates, choices):
            if len(candidates) == len(choices):
                res.append(copy.deepcopy(choices))
                return

            for candidate in candidates:
                if candidate in choices:
                    continue
                choices.append(candidate)
                backtrack(candidates, choices)
                choices.pop()

        backtrack(nums, choices)

        return res

```


### Related Problems
[Next Permutation](https://leetcode.com/problems/next-permutation/) (Medium) <br>
[Permutations II](https://leetcode.com/problems/permutations-ii/) (Medium) <br>
[Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) (Hard) <br>
[Combinations](https://leetcode.com/problems/combinations/) (Medium) <br>



### What a(n) Medium problem!
Among **1112259** total submissions, **733772** are accepted, with an acceptance rate of **66.0%**. <br>

- Likes: 5184
- Dislikes: 122

