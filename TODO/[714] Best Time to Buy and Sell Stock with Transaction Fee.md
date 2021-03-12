# [714] Best Time to Buy and Sell Stock with Transaction Fee (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) 

:+1: 2124 &nbsp; &nbsp; :thumbsdown: 64

---

### My Solution


### Description
<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer <code>fee</code> representing a transaction fee.</p>

<p>Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,3,2,8,4,9], fee = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,3,7,5,10,3], fee = 3
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt; prices.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt; prices[i], fee &lt; 5 * 10<sup>4</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 776 ms
- Completed time: 2019-09-17 14:57:56

```Python
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        if len(prices) <= 1:
            return 0
        
        buy, sell = [0] * len(prices), [0] * len(prices)
        buy[0] = -prices[0] - fee

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i] - fee)
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            
        return sell[-1]
```


### Related Problems
[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Easy) <br>



### What a(n) Medium problem!
Among **156393** total submissions, **87859** are accepted, with an acceptance rate of **56.2%**. <br>

- Likes: 2124
- Dislikes: 64

