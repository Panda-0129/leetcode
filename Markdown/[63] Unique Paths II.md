# [63] Unique Paths II (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/unique-paths-ii/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/unique-paths-ii/) 

:+1: 2337 &nbsp; &nbsp; :thumbsdown: 270

---

### My Solution


### Description
<p>A robot is located at the top-left corner of a <code>m x n</code> grid (marked &#39;Start&#39; in the diagram below).</p>

<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39;Finish&#39; in the diagram below).</p>

<p>Now consider if some obstacles are added to the grids. How many unique paths would there be?</p>

<p>An obstacle and space is marked as <code>1</code> and <code>0</code> respectively in the grid.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,1],[0,0]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;obstacleGrid.length</code></li>
	<li><code>n ==&nbsp;obstacleGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>obstacleGrid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 56 ms
- Completed time: 2019-11-01 15:03:49

```Python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            if obstacleGrid[0][0] == 1:
                return 0
            else:
                return 1
        row = len(obstacleGrid) + 1
        column = len(obstacleGrid[0]) + 1
        dp = [[0] * column for _ in range(row)]
        for i in range(row - 1, 0, -1):
            for j in range(column - 1, 0, -1):
                if obstacleGrid[row - 2][column - 2] == 0:
                    dp[row - 2][column - 2] = 1
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i - 1][j - 1] = 0
                else:
                    dp[i - 1][j - 1] = dp[i][j - 1] + dp[i - 1][j]

        return dp[0][0]       
```


### Related Problems
[Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium) <br>
[Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) (Hard) <br>



### What a(n) Medium problem!
Among **972649** total submissions, **341545** are accepted, with an acceptance rate of **35.1%**. <br>

- Likes: 2337
- Dislikes: 270

