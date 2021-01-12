# [718] Maximum Length of Repeated Subarray (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)  [![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) 

:+1: 1702 &nbsp; &nbsp; :thumbsdown: 49

---

### My Solution


### Description
<p>Given two integer arrays <code>A</code> and <code>B</code>, return the maximum length of an subarray that appears in both arrays.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b>
A: [1,2,3,2,1]
B: [3,2,1,4,7]
<b>Output:</b> 3
<b>Explanation:</b> 
The repeated subarray with maximum length is [3, 2, 1].
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>1 &lt;= len(A), len(B) &lt;= 1000</li>
	<li>0 &lt;= A[i], B[i] &lt; 100</li>
</ol>

<p>&nbsp;</p>



### My Submission

- Language: Python
- Runtime: 3496 ms
- Completed time: 2020-11-13 11:21:38

```Python
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_row = len(A) + 1
        len_col = len(B) + 1
        
        dp = [[0 for _ in range(len_col)] for _ in range(len_row)]
        
        for i in range(1, len_row):
            for j in range(1, len_col):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        
        return max(max(row) for row in dp)
```


### Related Problems
[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Medium) <br>



### What a(n) Medium problem!
Among **159335** total submissions, **79855** are accepted, with an acceptance rate of **50.1%**. <br>

- Likes: 1702
- Dislikes: 49

