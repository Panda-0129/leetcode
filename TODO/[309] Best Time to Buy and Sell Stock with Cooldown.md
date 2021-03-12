# [309] Best Time to Buy and Sell Stock with Cooldown (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) 

:+1: 3471 &nbsp; &nbsp; :thumbsdown: 109

---

### My Solution


### Description
<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:</p>

<ul>
	<li>After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).</li>
</ul>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,0,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> transactions = [buy, sell, cooldown, buy, sell]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 5000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2019-11-21 09:37:55

```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        buy, wait_for_sell, cooldown = 0, -prices[0], -sys.maxsize
        for i in range(1, len(prices)):
            pre_state_sell = wait_for_sell
            wait_for_sell = max(wait_for_sell, buy - prices[i])
            buy = max(buy, cooldown)
            cooldown = pre_state_sell + prices[i]

        return max(cooldown, buy)        
```


### Related Problems
[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) <br>
[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Easy) <br>



### What a(n) Medium problem!
Among **386754** total submissions, **186299** are accepted, with an acceptance rate of **48.2%**. <br>

- Likes: 3471
- Dislikes: 109

