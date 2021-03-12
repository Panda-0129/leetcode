# [1322] Minimum Moves to Reach Target with Rotations (Hard)

[![Breadth-first%20Search_badge](https://img.shields.io/badge/topic-Breadth-first%20Search-green.svg)](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) 

:+1: 150 &nbsp; &nbsp; :thumbsdown: 43

---

### My Solution


### Description
<p>In an&nbsp;<code>n*n</code>&nbsp;grid, there is a snake that spans 2 cells and starts moving from the top left corner at <code>(0, 0)</code> and <code>(0, 1)</code>. The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at&nbsp;<code>(n-1, n-2)</code>&nbsp;and&nbsp;<code>(n-1, n-1)</code>.</p>

<p>In one move the snake can:</p>

<ul>
	<li>Move one cell to the right&nbsp;if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.</li>
	<li>Move down one cell&nbsp;if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.</li>
	<li>Rotate clockwise if it&#39;s in a horizontal position and the two cells under it are both empty. In that case the snake moves from&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r, c+1)</code>&nbsp;to&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r+1, c)</code>.<br />
	<img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image-2.png" style="width: 300px; height: 134px;" /></li>
	<li>Rotate counterclockwise&nbsp;if it&#39;s in a vertical position and the two cells to its right are both empty. In that case the snake moves from&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r+1, c)</code>&nbsp;to&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r, c+1)</code>.<br />
	<img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image-1.png" style="width: 300px; height: 121px;" /></li>
</ul>

<p>Return the minimum number of moves to reach the target.</p>

<p>If there is no way to reach the target, return&nbsp;<code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image.png" style="width: 400px; height: 439px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
&nbsp;              [0,0,0,0,1,1],
&nbsp;              [0,0,1,0,1,0],
&nbsp;              [0,1,1,0,0,0],
&nbsp;              [0,1,1,0,0,0]]
<strong>Output:</strong> 11
<strong>Explanation:
</strong>One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,0,1,1,1,1],
&nbsp;              [0,0,0,0,1,1],
&nbsp;              [1,1,0,0,0,1],
&nbsp;              [1,1,1,0,0,1],
&nbsp;              [1,1,1,0,0,1],
&nbsp;              [1,1,1,0,0,0]]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1</code></li>
	<li>It is guaranteed that the snake starts at empty cells.</li>
</ul>



### My Submission

- Language: Java
- Runtime: 9 ms
- Completed time: 2020-11-18 00:47:22

```Java
class Solution {
    public int minimumMoves(int[][] grid) {
        int n = grid.length;
        int[][][] dp = new int[n][n][2]; // 放上三种状态，尾巴的横纵坐标和垂直或水平,0表示水平,1表示垂直。
        int[] dx = {0, 1}, dy = {1, 0}; // 如果让蛇向右移动一格，那么蛇整个身体x轴不变，y轴+1，同理向下也一样。
        dp[0][0][0] = 1;
        // base case是1，为什么是一呢，因为java开辟数组时默认会把所有数组归为0，本来应该是0，但是为了方便先让他比答案多1，最后返回时再-1就行了
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Rotate
                for (int k = 0; k < 2; k++) {
                    if (dp[i][j][k] == 0) continue; // 等于0说明当前位置不可达，不用计算。
                    if (i + 1 >= n || j + 1 >= n) continue; // 如果i+1或j+1超出边界，说明它不可能做翻转操作，因为另一种状态以及越界了。
                    if (k == 0) { // 水平位置判断下面以及右下位置是否有障碍，没有才能更新
                        if (grid[i+1][j] != 1 && grid[i+1][j+1] != 1)
                            // 如果要更新的状态本来里面存的次数要少，那就不用更新了。
                            if (dp[i][j][1-k] == 0 || dp[i][j][1-k] > dp[i][j][k] + 1) dp[i][j][1-k] = dp[i][j][k] + 1;
                    } else { // 垂直位置判断右边以及右下位置
                        if (grid[i][j+1] != 1 && grid[i+1][j+1] != 1)
                            if (dp[i][j][1-k] == 0 || dp[i][j][1-k] > dp[i][j][k] + 1) dp[i][j][1-k] = dp[i][j][k] + 1;
                    }
                }
                
                // move
                for (int k = 0; k < 2; k++) {
                    if (dp[i][j][k] == 0) continue; // 同理当前位置不可达，结束
                    int[] nx = new int[2], ny = new int[2]; // nx,ny表示蛇身体的位置，前一个是尾巴，后一个是头
                    for (int w = 0; w < 2; w++) { // w循环表示蛇向右移动和向下移动
                        boolean flag = true; // 用于判断蛇是否能到达，就是有没有障碍物
                        nx[0] = i;nx[1] = i + dx[k]; // 计算蛇的身体位置。
                        ny[0] = j;ny[1] = j + dy[k];
                        for (int mv = 0; mv < 2; mv++) { // mv循环表示移动蛇的尾巴和头，先移尾巴后头。
                            nx[mv] += dx[w];ny[mv] += dy[w]; // 计算移动后的位置。
                            if (nx[mv] < 0 || nx[mv] >= n || ny[mv] < 0 || ny[mv] >= n) flag = false; 
                            // 如果移动后身体的某个位置超出数组，说明不可达。
                            else if (grid[nx[mv]][ny[mv]] == 1) flag = false; // 同样有障碍也不可达。
                        }
                        if (flag == false) continue; // 不可达就不能更新。
                        if (dp[nx[0]][ny[0]][k] == 0 || dp[nx[0]][ny[0]][k] > dp[i][j][k] + 1) dp[nx[0]][ny[0]][k] = dp[i][j][k] + 1;
                    }
                }
            }
        }
        return dp[n-1][n-2][0] - 1; // 蛇最后结束的位置就是尾巴在(n-1, n-2)上处于水平状态。然后别忘了之前的-1。
    }
}
```


### Related Problems




### What a(n) Hard problem!
Among **12579** total submissions, **5839** are accepted, with an acceptance rate of **46.4%**. <br>

- Likes: 150
- Dislikes: 43

