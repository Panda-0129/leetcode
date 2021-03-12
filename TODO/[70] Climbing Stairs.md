# [70] Climbing Stairs (Easy)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/climbing-stairs/) 

:+1: 6079 &nbsp; &nbsp; :thumbsdown: 192

---

### My Solution


### Description
<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 20 ms
- Completed time: 2019-04-02 21:31:57

```Python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre, prepre = 2, 1
        
        for i in range(2, n):
            current = pre + prepre
            prepre = pre
            pre = current
            
        return pre
```


### Related Problems
[Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) (Easy) <br>
[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (Easy) <br>
[N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) (Easy) <br>



### What a(n) Easy problem!
Among **1862962** total submissions, **906706** are accepted, with an acceptance rate of **48.7%**. <br>

- Likes: 6079
- Dislikes: 192

