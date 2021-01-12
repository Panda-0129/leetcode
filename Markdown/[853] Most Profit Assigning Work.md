# [853] Most Profit Assigning Work (Medium)

[![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/most-profit-assigning-work/) 

:+1: 449 &nbsp; &nbsp; :thumbsdown: 73

---

### My Solution


### Description
<p>We have jobs: <code>difficulty[i]</code>&nbsp;is the difficulty of the&nbsp;<code>i</code>th job, and&nbsp;<code>profit[i]</code>&nbsp;is the profit of the&nbsp;<code>i</code>th job.&nbsp;</p>

<p>Now we have some workers.&nbsp;<code>worker[i]</code>&nbsp;is the ability of the&nbsp;<code>i</code>th worker, which means that this worker can only complete a job with difficulty at most&nbsp;<code>worker[i]</code>.&nbsp;</p>

<p>Every worker can be assigned at most one job, but one job&nbsp;can be completed multiple times.</p>

<p>For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.&nbsp; If a worker cannot complete any job, his profit is $0.</p>

<p>What is the most profit we can make?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
<strong>Output: </strong>100 
<strong>Explanation: W</strong>orkers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.</pre>

<p><strong>Notes:</strong></p>

<ul>
	<li><code>1 &lt;= difficulty.length = profit.length &lt;= 10000</code></li>
	<li><code>1 &lt;= worker.length &lt;= 10000</code></li>
	<li><code>difficulty[i], profit[i], worker[i]</code>&nbsp; are in range&nbsp;<code>[1, 10^5]</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 340 ms
- Completed time: 2019-09-11 21:41:26

```Python
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        res = i = currentBest = 0
        job = sorted(zip(difficulty, profit), key = lambda t: t[0])
        
        for ability in sorted(worker):
            while i < len(job) and ability >= job[i][0]:
                currentBest = max(currentBest, job[i][1])
                i += 1
            res += currentBest

        return res
```


### Related Problems




### What a(n) Medium problem!
Among **61033** total submissions, **23732** are accepted, with an acceptance rate of **38.9%**. <br>

- Likes: 449
- Dislikes: 73

