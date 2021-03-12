# [64] Minimum Path Sum (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/minimum-path-sum/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/minimum-path-sum/) 

:+1: 4382 &nbsp; &nbsp; :thumbsdown: 80

---

### My Solution


### Description
<p>Given a <code>m x n</code> <code>grid</code> filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,2,3],[4,5,6]]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 184 ms
- Completed time: 2019-04-02 23:29:21

```Python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if grid is None:
            return 0
        
        res = []
        
        for i in range(len(grid)):
            res.append([0] * len(grid[0]))

        res[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                res[i][j] += grid[i][j] + min(65532 if j == 0 else res[i][j-1], 65532 if i == 0 else res[i-1][j])

        return res[len(grid) - 1][len(grid[0]) - 1]
                
                
```


### Related Problems
[Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium) <br>
[Dungeon Game](https://leetcode.com/problems/dungeon-game/) (Hard) <br>
[Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) (Hard) <br>



### What a(n) Medium problem!
Among **916462** total submissions, **515831** are accepted, with an acceptance rate of **56.3%**. <br>

- Likes: 4382
- Dislikes: 80

