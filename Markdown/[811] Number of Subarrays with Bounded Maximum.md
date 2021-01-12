# [811] Number of Subarrays with Bounded Maximum (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) 

:+1: 682 &nbsp; &nbsp; :thumbsdown: 45

---

### My Solution


### Description
<p>We are given an array <code>A</code> of positive integers, and two positive integers <code>L</code> and <code>R</code> (<code>L &lt;= R</code>).</p>

<p>Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least <code>L</code> and at most <code>R</code>.</p>

<pre>
<strong>Example :</strong>
<strong>Input:</strong> 
A = [2, 1, 4, 3]
L = 2
R = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three subarrays that meet the requirements: [2], [2, 1], [3].
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>L, R&nbsp; and <code>A[i]</code> will be an integer in the range <code>[0, 10^9]</code>.</li>
	<li>The length of <code>A</code> will be in the range of <code>[1, 50000]</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 404 ms
- Completed time: 2019-10-25 14:40:39

```Python
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        dp = [0 for _ in range(len(A))]
        sub_start = -1

        for index, num in enumerate(A):
            if num < L:
                dp[index] = dp[index - 1]
            elif num > R:
                dp[index] = 0
                sub_start = index
            else:
                dp[index] = index - sub_start

        return sum(dp)
```


### Related Problems




### What a(n) Medium problem!
Among **46429** total submissions, **21956** are accepted, with an acceptance rate of **47.3%**. <br>

- Likes: 682
- Dislikes: 45

