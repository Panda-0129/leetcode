# [891] Score After Flipping Matrix (Medium)

[![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/score-after-flipping-matrix/) 

:+1: 596 &nbsp; &nbsp; :thumbsdown: 134

---

### My Solution


### Description
<p>We have a two dimensional matrix&nbsp;<code>A</code> where each value is <code>0</code> or <code>1</code>.</p>

<p>A move consists of choosing any row or column, and toggling each value in that row or column: changing all <code>0</code>s to <code>1</code>s, and all <code>1</code>s to <code>0</code>s.</p>

<p>After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.</p>

<p>Return the highest possible&nbsp;score.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,0,1,1],[1,0,1,0],[1,1,0,0]]</span>
<strong>Output: </strong><span id="example-output-1">39</span>
<strong>Explanation:
</strong>Toggled to <span id="example-input-1-1">[[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</span></pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20</code></li>
	<li><code>1 &lt;= A[0].length &lt;= 20</code></li>
	<li><code>A[i][j]</code>&nbsp;is <code>0</code> or <code>1</code>.</li>
</ol>
</div>



### My Submission

- Language: Python
- Runtime: 48 ms
- Completed time: 2019-10-24 20:02:10

```Python
from collections import Counter

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if A[i][0] == 0:
                A[i] = [0 if A[i][_] == 1 else 1 for _ in range(len(A[i]))]

        for i in range(len(A[0])):
            column = [col[i] for col in A]
            counter = Counter(column)
            if counter[0] > counter[1]:
                column = [0 if column[_] == 1 else 1 for _ in range(len(column))]
                for r in range(len(A)):
                    A[r][i] = column[r]

        res = 0
        for row in A:
            row.reverse()
            for i in range(len(A[0])):
                res += (2 ** i) * row[i]

        return res
```


### Related Problems




### What a(n) Medium problem!
Among **33709** total submissions, **24749** are accepted, with an acceptance rate of **73.4%**. <br>

- Likes: 596
- Dislikes: 134

