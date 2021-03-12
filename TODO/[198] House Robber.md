# [198] House Robber (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/house-robber/) 

:+1: 6636 &nbsp; &nbsp; :thumbsdown: 187

---

### My Solution


### Description
<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <b>without alerting the police</b></em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 24 ms
- Completed time: 2019-04-02 22:42:00

```Python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, prepre = 0, 0
        
        for num in nums:
            res = max(prepre + num, pre)
            prepre = pre
            pre = res
        
        return pre
```


### Related Problems
[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (Medium) <br>
[House Robber II](https://leetcode.com/problems/house-robber-ii/) (Medium) <br>
[Paint House](https://leetcode.com/problems/paint-house/) (Medium) <br>
[Paint Fence](https://leetcode.com/problems/paint-fence/) (Medium) <br>
[House Robber III](https://leetcode.com/problems/house-robber-iii/) (Medium) <br>
[Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) (Hard) <br>
[Coin Path](https://leetcode.com/problems/coin-path/) (Hard) <br>
[Delete and Earn](https://leetcode.com/problems/delete-and-earn/) (Medium) <br>



### What a(n) Medium problem!
Among **1597216** total submissions, **685566** are accepted, with an acceptance rate of **42.9%**. <br>

- Likes: 6636
- Dislikes: 187

