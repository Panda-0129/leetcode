# [62] Unique Paths (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/unique-paths/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/unique-paths/) 

:+1: 4364 &nbsp; &nbsp; :thumbsdown: 235

---

### My Solution


### Description
<p>A robot is located at the top-left corner of a <code>m x n</code> grid (marked &#39;Start&#39; in the diagram below).</p>

<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39;Finish&#39; in the diagram below).</p>

<p>How many possible unique paths are there?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" />
<pre>
<strong>Input:</strong> m = 3, n = 7
<strong>Output:</strong> 28
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong>
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Down
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> m = 7, n = 3
<strong>Output:</strong> 28
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> m = 3, n = 3
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li>It&#39;s guaranteed that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 44 ms
- Completed time: 2019-10-31 08:55:38

```Python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        dp = [[0] * m for _ in range(n)]
        dp[n - 1][m - 1] = 0
        for i in range(m - 1):
            dp[n - 1][i] = 1
        for i in range(n - 1):
            dp[i][m - 1] = 1

        for i in range(n - 1, 0, -1):
            for j in range(m - 1, 0, -1):
                dp[i - 1][j - 1] = dp[i][j - 1] + dp[i - 1][j]

        return dp[0][0]
        
```


### Related Problems
[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) (Medium) <br>
[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) (Medium) <br>
[Dungeon Game](https://leetcode.com/problems/dungeon-game/) (Hard) <br>



### What a(n) Medium problem!
Among **1041435** total submissions, **579009** are accepted, with an acceptance rate of **55.6%**. <br>

- Likes: 4364
- Dislikes: 235

