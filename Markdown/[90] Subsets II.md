# [90] Subsets II (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/subsets-ii/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/subsets-ii/) 

:+1: 2151 &nbsp; &nbsp; :thumbsdown: 96

---

### My Solution


### Description
<p>Given a collection of integers that might contain duplicates, <strong><em>nums</em></strong>, return all possible subsets (the power set).</p>

<p><strong>Note:</strong> The solution set must not contain duplicate subsets.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,2,2]
<strong>Output:</strong>
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
</pre>



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
Among **655160** total submissions, **317497** are accepted, with an acceptance rate of **48.5%**. <br>

- Likes: 2151
- Dislikes: 96

