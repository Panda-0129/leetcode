# [695] Max Area of Island (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/max-area-of-island/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/max-area-of-island/) 

:+1: 2831 &nbsp; &nbsp; :thumbsdown: 95

---

### My Solution


### Description
<p>Given a non-empty 2D array <code>grid</code> of 0&#39;s and 1&#39;s, an <b>island</b> is a group of <code>1</code>&#39;s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)</p>

<p><b>Example 1:</b></p>

<pre>
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,0,<b>1</b>,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,<b>1</b>,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
</pre>
Given the above grid, return <code>6</code>. Note the answer is not 11, because the island must be connected 4-directionally.

<p><b>Example 2:</b></p>

<pre>
[[0,0,0,0,0,0,0,0]]</pre>
Given the above grid, return <code>0</code>.

<p><b>Note:</b> The length of each dimension in the given <code>grid</code> does not exceed 50.</p>



### My Submission

- Language: Python
- Runtime: 116 ms
- Completed time: 2019-09-12 15:43:02

```Python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, grid):

            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j, grid) + dfs(i + 1, j, grid) + dfs(i, j - 1, grid) + dfs(i, j + 1, grid)
        
            return 0

        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res = max(dfs(i, j, grid), res)
    
        return res
```


### Related Problems
[Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium) <br>
[Island Perimeter](https://leetcode.com/problems/island-perimeter/) (Easy) <br>
[Largest Submatrix With Rearrangements](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) (Medium) <br>



### What a(n) Medium problem!
Among **336972** total submissions, **218597** are accepted, with an acceptance rate of **64.9%**. <br>

- Likes: 2831
- Dislikes: 95

