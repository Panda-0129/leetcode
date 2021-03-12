# [923] Super Egg Drop (Hard)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/super-egg-drop/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/super-egg-drop/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/super-egg-drop/) 

:+1: 1275 &nbsp; &nbsp; :thumbsdown: 97

---

### My Solution


### Description
<p>You are given <code>k</code> identical eggs and you have access to a building with <code>n</code> floors labeled from <code>1</code> to <code>n</code>.</p>

<p>You know that there exists a floor <code>f</code> where <code>0 &lt;= f &lt;= n</code> such that any egg dropped at a floor <strong>higher</strong> than <code>f</code> will <strong>break</strong>, and any egg dropped <strong>at or below</strong> floor <code>f</code> will <strong>not break</strong>.</p>

<p>Each move, you may take an unbroken egg and drop it from any floor <code>x</code> (where <code>1 &lt;= x &lt;= n</code>). If the egg breaks, you can no longer use it. However, if the egg does not break, you may <strong>reuse</strong> it in future moves.</p>

<p>Return <em>the <strong>minimum number of moves</strong> that you need to determine <strong>with certainty</strong> what the value of </em><code>f</code> is.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 1, n = 2
<strong>Output:</strong> 2
<strong>Explanation: </strong>
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 2, n = 6
<strong>Output:</strong> 3
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 14
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 2436 ms
- Completed time: 2020-09-24 15:31:27

```Python
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        
        def dp(K, N):
            if (K, N) in memo:
                return memo[(K,N)]
            
            if K == 1:
                return N
            if N == 0:
                return 0
            
            res = sys.maxsize
            
            # for i in range(1, N + 1):
            #     res = min(res, max(dp(K - 1, i - 1), dp(K, N - i)) + 1)
            lo, hi = 1, N
            while lo <= hi:
                mid = int(lo + (hi - lo) / 2)
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                
                if broken < not_broken:
                    lo = mid + 1
                    res = min(not_broken + 1, res)
                else:
                    hi = mid - 1
                    res = min(broken + 1, res)
            
            memo[(K, N)] = res
            
            return res
        
        return dp(K, N)
```


### Related Problems




### What a(n) Hard problem!
Among **103088** total submissions, **27853** are accepted, with an acceptance rate of **27.0%**. <br>

- Likes: 1275
- Dislikes: 97

