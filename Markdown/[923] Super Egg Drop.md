# [923] Super Egg Drop (Hard)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/super-egg-drop/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/super-egg-drop/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/super-egg-drop/) 

:+1: 1181 &nbsp; &nbsp; :thumbsdown: 94

---

### My Solution


### Description
<p>You are given <code>K</code> eggs, and you have access to a building with <code>N</code> floors from <code>1</code> to <code>N</code>.&nbsp;</p>

<p>Each egg is identical in function, and if an egg breaks, you cannot drop it&nbsp;again.</p>

<p>You know that there exists a floor <code>F</code> with <code>0 &lt;= F &lt;= N</code> such that any egg dropped at a floor higher than <code>F</code> will break, and any egg dropped at or below floor <code>F</code> will not break.</p>

<p>Each <em>move</em>, you may take an egg (if you have an unbroken one) and drop it from any floor <code>X</code> (with&nbsp;<code>1 &lt;= X &lt;= N</code>).&nbsp;</p>

<p>Your goal is to know&nbsp;<strong>with certainty</strong>&nbsp;what the value of <code>F</code> is.</p>

<p>What is the minimum number of moves that you need to know with certainty&nbsp;what <code>F</code> is, regardless of the initial value of <code>F</code>?</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>K = <span id="example-input-1-1">1</span>, N = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn&#39;t break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>K = <span id="example-input-2-1">2</span>, N = 6
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>K = <span id="example-input-3-1">3</span>, N = <span id="example-input-3-2">14</span>
<strong>Output: </strong><span id="example-output-3">4</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= 100</code></li>
	<li><code>1 &lt;= N &lt;= 10000</code></li>
</ol>
</div>
</div>
</div>



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
Among **95879** total submissions, **25959** are accepted, with an acceptance rate of **27.1%**. <br>

- Likes: 1181
- Dislikes: 94

