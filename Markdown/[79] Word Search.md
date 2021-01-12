# [79] Word Search (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/word-search/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/word-search/) 

:+1: 4989 &nbsp; &nbsp; :thumbsdown: 221

---

### My Solution


### Description
<p>Given an&nbsp;<code>m x n</code> <code>board</code> and a <code>word</code>, find if the word exists in the grid.</p>

<p>The word can be constructed from letters of sequentially adjacent cells, where &quot;adjacent&quot; cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;ABCCED&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;SEE&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;ABCB&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= word.length &lt;= 10<sup>3</sup></code></li>
	<li><code>board</code>&nbsp;and <code>word</code> consists only of lowercase and uppercase English letters.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 288 ms
- Completed time: 2020-10-12 11:18:35

```Python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        def searchWord(board, word, cur_index, init_x, init_y, marked, m, n):
            if cur_index == len(word) - 1:
                return board[init_x][init_y] == word[cur_index]
            
            if board[init_x][init_y] == word[cur_index]:
                marked[init_x][init_y] = True
                for direction in directions:
                    new_x = init_x + direction[0]
                    new_y = init_y + direction[1]
                    
                    if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and searchWord(board, word, cur_index + 1, new_x, new_y, marked, m, n):
                        return True
                    
                marked[init_x][init_y] = False
                
            return False
        
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if searchWord(board, word, 0, i, j, marked, m, n):
                    return True
        
        return False
                
```


### Related Problems
[Word Search II](https://leetcode.com/problems/word-search-ii/) (Hard) <br>



### What a(n) Medium problem!
Among **1612319** total submissions, **589088** are accepted, with an acceptance rate of **36.5%**. <br>

- Likes: 4989
- Dislikes: 221

