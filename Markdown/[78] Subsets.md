# [78] Subsets (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/subsets/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/subsets/)  [![Bit%20Manipulation_badge](https://img.shields.io/badge/topic-Bit%20Manipulation-green.svg)](https://leetcode.com/problems/subsets/) 

:+1: 5035 &nbsp; &nbsp; :thumbsdown: 106

---

### My Solution


### Description
<p>Given an&nbsp;integer array&nbsp;<code>nums</code>, return <em>all possible subsets (the power set)</em>.</p>

<p>The solution set must not contain duplicate subsets.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2020-09-28 10:32:36

```Python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(begin, path, res):
            res.append(path[:])
            
            for i in range(begin, length):
                path.append(nums[i])
                dfs(i + 1, path, res)
                path.pop()
            
        res = []
        length = len(nums)
        dfs(0, [], res)
        
        return res
```


### Related Problems
[Subsets II](https://leetcode.com/problems/subsets-ii/) (Medium) <br>
[Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/) (Medium) <br>
[Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) (Medium) <br>



### What a(n) Medium problem!
Among **1081580** total submissions, **696755** are accepted, with an acceptance rate of **64.4%**. <br>

- Likes: 5035
- Dislikes: 106

