# [928] Surface Area of 3D Shapes (Easy)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/surface-area-of-3d-shapes/)  [![Geometry_badge](https://img.shields.io/badge/topic-Geometry-green.svg)](https://leetcode.com/problems/surface-area-of-3d-shapes/) 

:+1: 297 &nbsp; &nbsp; :thumbsdown: 448

---

### My Solution


### Description
<p>You are given an <code>n x n</code> <code>grid</code> where you have placed some <code>1 x 1 x 1</code> cubes. Each value <code>v = grid[i][j]</code> represents a tower of <code>v</code> cubes placed on top of cell <code>(i, j)</code>.</p>

<p>After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.</p>

<p>Return <em>the total surface area of the resulting shapes</em>.</p>

<p><strong>Note:</strong> The bottom face of each shape counts toward its surface area.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid1.jpg" style="width: 82px; height: 82px;" />
<pre>
<strong>Input:</strong> grid = [[2]]
<strong>Output:</strong> 10
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> 34
</pre>

<p><strong>Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid3.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> grid = [[1,0],[0,2]]
<strong>Output:</strong> 16
</pre>

<p><strong>Example 4:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> 32
</pre>

<p><strong>Example 5:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[2,2,2],[2,1,2],[2,2,2]]
<strong>Output:</strong> 46
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 64 ms
- Completed time: 2019-09-03 23:47:31

```Python
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N, res = len(grid), 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    res = res + grid[i][j]*4 + 2
                if i < N - 1:
                    res = res - min(grid[i+1][j], grid[i][j])*2
                if j < N - 1:
                    res = res - min(grid[i][j+1], grid[i][j])*2
                    
        return res
                
```


### Related Problems




### What a(n) Easy problem!
Among **37157** total submissions, **22225** are accepted, with an acceptance rate of **59.8%**. <br>

- Likes: 297
- Dislikes: 448

