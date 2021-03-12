# [967] Minimum Falling Path Sum (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/minimum-falling-path-sum/) 

:+1: 1118 &nbsp; &nbsp; :thumbsdown: 82

---

### My Solution


### Description
<p>Given an <code>n x n</code> array of integers <code>matrix</code>, return <em>the <strong>minimum sum</strong> of any <strong>falling path</strong> through</em> <code>matrix</code>.</p>

<p>A <strong>falling path</strong> starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position <code>(row, col)</code> will be <code>(row + 1, col - 1)</code>, <code>(row + 1, col)</code>, or <code>(row + 1, col + 1)</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> There are two falling paths with a minimum sum underlined below:
[[2,<u>1</u>,3],      [[2,<u>1</u>,3],
 [6,<u>5</u>,4],       [6,5,<u>4</u>],
 [<u>7</u>,8,9]]       [7,<u>8</u>,9]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[-19,57],[-40,-5]]
<strong>Output:</strong> -59
<strong>Explanation:</strong> The falling path with a minimum sum is underlined below:
[[<u>-19</u>,57],
 [<u>-40</u>,-5]]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[-48]]
<strong>Output:</strong> -48
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 108 ms
- Completed time: 2020-11-17 10:33:17

```Python
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for row in range(1, len(A)):
            for col in range(len(A[0])):
                if 0 < col < len(A[0]) - 1:
                    A[row][col] += min(A[row - 1][col - 1], A[row - 1][col], A[row - 1][col + 1])
                elif col == 0:
                    A[row][col] += min(A[row - 1][col], A[row - 1][col + 1])
                else:
                    A[row][col] += min(A[row - 1][col - 1], A[row - 1][col])

        return min(A[len(A) - 1])
```


### Related Problems
[Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii/) (Hard) <br>



### What a(n) Medium problem!
Among **107733** total submissions, **68460** are accepted, with an acceptance rate of **63.5%**. <br>

- Likes: 1118
- Dislikes: 82

