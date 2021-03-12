# [518] Coin Change 2 (Medium)



:+1: 2889 &nbsp; &nbsp; :thumbsdown: 75

---

### My Solution


### Description
<p>You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.</p>

<ul>
</ul>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> amount = 5, coins = [1, 2, 5]
<b>Output:</b> 4
<b>Explanation:</b> there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> amount = 3, coins = [2]
<b>Output:</b> 0
<b>Explanation:</b> the amount of 3 cannot be made up just with coins of 2.
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> amount = 10, coins = [10] 
<b>Output:</b> 1
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<p>You can assume that</p>

<ul>
	<li>0 &lt;= amount &lt;= 5000</li>
	<li>1 &lt;= coin &lt;= 5000</li>
	<li>the number of coins is less than 500</li>
	<li>the answer is guaranteed to fit into signed 32-bit integer</li>
</ul>



### My Submission

- Language: Python
- Runtime: 272 ms
- Completed time: 2020-09-13 10:29:07

```Python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
                
        return dp[amount]
```


### Related Problems




### What a(n) Medium problem!
Among **348137** total submissions, **180530** are accepted, with an acceptance rate of **51.9%**. <br>

- Likes: 2889
- Dislikes: 75

