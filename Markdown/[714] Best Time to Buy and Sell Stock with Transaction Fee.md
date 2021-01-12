# [714] Best Time to Buy and Sell Stock with Transaction Fee (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) 

:+1: 1974 &nbsp; &nbsp; :thumbsdown: 61

---

### My Solution


### Description
<p>Your are given an array of integers <code>prices</code>, for which the <code>i</code>-th element is the price of a given stock on day <code>i</code>; and a non-negative integer <code>fee</code> representing a transaction fee.</p>
<p>You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)</p>
<p>Return the maximum profit you can make.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> prices = [1, 3, 2, 8, 4, 9], fee = 2
<b>Output:</b> 8
<b>Explanation:</b> The maximum profit can be achieved by:
<li>Buying at prices[0] = 1</li><li>Selling at prices[3] = 8</li><li>Buying at prices[4] = 4</li><li>Selling at prices[5] = 9</li>The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < prices.length <= 50000</code>.</li>
<li><code>0 < prices[i] < 50000</code>.</li>
<li><code>0 <= fee < 50000</code>.</li>
</p>


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
Among **149605** total submissions, **83537** are accepted, with an acceptance rate of **55.8%**. <br>

- Likes: 1974
- Dislikes: 61

