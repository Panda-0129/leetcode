# [309] Best Time to Buy and Sell Stock with Cooldown (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) 

:+1: 3285 &nbsp; &nbsp; :thumbsdown: 103

---

### My Solution


### Description
<p>Say you have an array for which the <i>i</i><sup>th</sup> element is the price of a given stock on day <i>i</i>.</p>

<p>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:</p>

<ul>
	<li>You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).</li>
	<li>After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)</li>
</ul>

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong> [1,2,3,0,2]
<strong>Output: </strong>3 
<strong>Explanation:</strong> transactions = [buy, sell, cooldown, buy, sell]
</pre>


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
Among **372841** total submissions, **179066** are accepted, with an acceptance rate of **48.0%**. <br>

- Likes: 3285
- Dislikes: 103

