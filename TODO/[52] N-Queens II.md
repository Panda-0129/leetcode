# [52] N-Queens II (Hard)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/n-queens-ii/) 

:+1: 764 &nbsp; &nbsp; :thumbsdown: 179

---

### My Solution


### Description
<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>the number of distinct solutions to the&nbsp;<strong>n-queens puzzle</strong></em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two distinct solutions to the 4-queens puzzle as shown.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 152 ms
- Completed time: 2020-09-14 19:18:01

```Python
class Solution:
    res = 0
    def totalNQueens(self, n: int) -> int:
        
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

        return len(res)
```


### Related Problems
[N-Queens](https://leetcode.com/problems/n-queens/) (Hard) <br>



### What a(n) Hard problem!
Among **259653** total submissions, **156493** are accepted, with an acceptance rate of **60.3%**. <br>

- Likes: 764
- Dislikes: 179

