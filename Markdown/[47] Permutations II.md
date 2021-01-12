# [47] Permutations II (Medium)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/permutations-ii/) 

:+1: 2640 &nbsp; &nbsp; :thumbsdown: 73

---

### My Solution


### Description
<p>Given a collection of numbers, <code>nums</code>,&nbsp;that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 48 ms
- Completed time: 2020-09-29 17:18:08

```Python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    
                    used[i] = True
                    path.append(nums[i])
                    dfs(path, used)
                    used[i] = False
                    path.pop()
                    
        res = []
        nums.sort()
        used = [False for _ in range(len(nums))]
        dfs([], used)
        
        return res
```


### Related Problems
[Next Permutation](https://leetcode.com/problems/next-permutation/) (Medium) <br>
[Permutations](https://leetcode.com/problems/permutations/) (Medium) <br>
[Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/) (Medium) <br>
[Number of Squareful Arrays](https://leetcode.com/problems/number-of-squareful-arrays/) (Hard) <br>



### What a(n) Medium problem!
Among **861404** total submissions, **421615** are accepted, with an acceptance rate of **48.9%**. <br>

- Likes: 2640
- Dislikes: 73

