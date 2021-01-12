# [967] Minimum Falling Path Sum (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/minimum-falling-path-sum/) 

:+1: 1019 &nbsp; &nbsp; :thumbsdown: 75

---

### My Solution


### Description
<p>Given a <strong>square</strong> array of integers <code>A</code>, we want the <strong>minimum</strong> sum of a <em>falling path</em> through <code>A</code>.</p>

<p>A falling path starts at any element in the first row, and chooses one element from each row.&nbsp; The next row&#39;s choice must be in a column that is different from the previous row&#39;s column by at most one.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,2,3],[4,5,6],[7,8,9]]</span>
<strong>Output: </strong><span id="example-output-1">12</span>
<strong>Explanation: </strong>
The possible falling paths are:
</pre>

<ul>
	<li><code>[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]</code></li>
	<li><code>[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]</code></li>
	<li><code>[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]</code></li>
</ul>

<p>The falling path with the smallest sum is <code>[1,4,7]</code>, so the answer is <code>12</code>.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= A.length == A[0].length &lt;= 100</code></li>
	<li><code>-100 &lt;= A[i][j] &lt;= 100</code></li>
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
Among **100947** total submissions, **63778** are accepted, with an acceptance rate of **63.2%**. <br>

- Likes: 1019
- Dislikes: 75

