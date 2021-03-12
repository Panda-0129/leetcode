# [971] Shortest Bridge (Medium)

[![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/shortest-bridge/)  [![Breadth-first%20Search_badge](https://img.shields.io/badge/topic-Breadth-first%20Search-green.svg)](https://leetcode.com/problems/shortest-bridge/) 

:+1: 1221 &nbsp; &nbsp; :thumbsdown: 83

---

### My Solution


### Description
<p>In a given 2D binary array <code>A</code>, there are two islands.&nbsp; (An island is a 4-directionally connected group of&nbsp;<code>1</code>s not connected to any other 1s.)</p>

<p>Now, we may change <code>0</code>s to <code>1</code>s so as to connect the two islands together to form 1 island.</p>

<p>Return the smallest number of <code>0</code>s that must be flipped.&nbsp; (It is guaranteed that the answer is at least 1.)</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> A = [[0,1],[1,0]]
<strong>Output:</strong> 1
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> A = [[0,1,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> 2
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= A.length == A[0].length &lt;= 100</code></li>
	<li><code>A[i][j] == 0</code> or <code>A[i][j] == 1</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 428 ms
- Completed time: 2020-10-19 16:53:20

```Python
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            A[i][j] = 2
            bfs.append((i, j))
            
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] == 1:
                    dfs(x, y)
        
        dfs_start = (0, 0)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    dfs_start = (i, j)
        
        bfs = []
        i, j = dfs_start
        dfs(i, j)
        
        step = 0
        while bfs:
            new = []
            
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < len(A) and 0 <= y < len(A[0]):
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            new.append((x, y))
            
            bfs = new
            step += 1
                    
```


### Related Problems




### What a(n) Medium problem!
Among **92121** total submissions, **45786** are accepted, with an acceptance rate of **49.7%**. <br>

- Likes: 1221
- Dislikes: 83

