# [90] Subsets II (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/subsets-ii/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/subsets-ii/) 

:+1: 2323 &nbsp; &nbsp; :thumbsdown: 102

---

### My Solution


### Description
<p>Given an integer array <code>nums</code> that may contain duplicates, return <em>all possible subsets (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2020-09-28 10:44:20

```Python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(begin, path):
            res.append(path[:])
            
            for i in range(begin, len(nums)):
                if nums[i - 1] == nums[i] and begin < i:
                    continue
                
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        
        nums.sort()
        res = []
        dfs(0, [])
        
        return res
```


### Related Problems
[Subsets](https://leetcode.com/problems/subsets/) (Medium) <br>



### What a(n) Medium problem!
Among **674070** total submissions, **329891** are accepted, with an acceptance rate of **48.9%**. <br>

- Likes: 2323
- Dislikes: 102

