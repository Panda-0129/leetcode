# [51] N-Queens (Hard)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/n-queens/) 

:+1: 2718 &nbsp; &nbsp; :thumbsdown: 98

---

### My Solution


### Description
<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>all distinct solutions to the <strong>n-queens puzzle</strong></em>.</p>

<p>Each solution contains a distinct board configuration of the n-queens&#39; placement, where <code>&#39;Q&#39;</code> and <code>&#39;.&#39;</code> both indicate a queen and an empty space, respectively.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> [[&quot;.Q..&quot;,&quot;...Q&quot;,&quot;Q...&quot;,&quot;..Q.&quot;],[&quot;..Q.&quot;,&quot;Q...&quot;,&quot;...Q&quot;,&quot;.Q..&quot;]]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [[&quot;Q&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 160 ms
- Completed time: 2020-09-14 19:09:01

```Python
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isValid(board, row, col):
            for i in range(n):
                if board[i][col] == 'Q':
                    return False

            for i, j in zip(reversed(range(0, row)), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False

            for i, j in zip(reversed(range(0, row)), reversed(range(0, col))):
                if board[i][j] == 'Q':
                    return False

            return True

        def backtracking(board, row):
            if row == len(board):
                res.append(copy.deepcopy(board))
                return
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row + 1)
                board[row][col] = '.'

        res = []
        board = [list('.' * n) for _ in range(n)]
        backtracking(board, 0)
        
        for board in res:
            for index, line in enumerate(board):
                tmp = ''.join(line)
                board[index] = tmp

        return res
```


### Related Problems
[N-Queens II](https://leetcode.com/problems/n-queens-ii/) (Hard) <br>
[Grid Illumination](https://leetcode.com/problems/grid-illumination/) (Hard) <br>



### What a(n) Hard problem!
Among **489481** total submissions, **243695** are accepted, with an acceptance rate of **49.8%**. <br>

- Likes: 2718
- Dislikes: 98

