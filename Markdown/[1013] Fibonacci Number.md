# [1013] Fibonacci Number (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/fibonacci-number/) 

:+1: 977 &nbsp; &nbsp; :thumbsdown: 214

---

### My Solution


### Description
<p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 28 ms
- Completed time: 2020-09-11 15:46:36

```Python
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        
        if N == 1 or N == 2:
            return 1
        
        pre = 1
        curr = 1
        
        for n in range(2, N):
            sum = pre + curr
            pre = curr
            curr = sum
        
        return curr
```


### Related Problems
[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (Easy) <br>
[Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) (Medium) <br>
[Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) (Medium) <br>
[N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) (Easy) <br>



### What a(n) Easy problem!
Among **434864** total submissions, **292437** are accepted, with an acceptance rate of **67.2%**. <br>

- Likes: 977
- Dislikes: 214

