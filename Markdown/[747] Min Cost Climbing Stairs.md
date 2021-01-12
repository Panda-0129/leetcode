# [747] Min Cost Climbing Stairs (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/min-cost-climbing-stairs/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/min-cost-climbing-stairs/) 

:+1: 2703 &nbsp; &nbsp; :thumbsdown: 586

---

### My Solution


### Description
<p>
On a staircase, the <code>i</code>-th step has some non-negative cost <code>cost[i]</code> assigned (0 indexed).
</p><p>
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> cost = [10, 15, 20]
<b>Output:</b> 15
<b>Explanation:</b> Cheapest is start on cost[1], pay that cost and go to the top.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
<b>Output:</b> 6
<b>Explanation:</b> Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>cost</code> will have a length in the range <code>[2, 1000]</code>.</li>
<li>Every <code>cost[i]</code> will be an integer in the range <code>[0, 999]</code>.</li>
</ol>
</p>


### My Submission

- Language: Python
- Runtime: 88 ms
- Completed time: 2019-10-09 20:22:53

```Python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[len(cost)]
```


### Related Problems
[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (Easy) <br>



### What a(n) Easy problem!
Among **402168** total submissions, **204522** are accepted, with an acceptance rate of **50.9%**. <br>

- Likes: 2703
- Dislikes: 586

