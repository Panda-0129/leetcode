# [213] House Robber II (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/house-robber-ii/) 

:+1: 2667 &nbsp; &nbsp; :thumbsdown: 63

---

### My Solution


### Description
<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 24 ms
- Completed time: 2019-04-02 22:57:43

```Python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.robinInterval(nums[1:]), self.robinInterval(nums[:-1]))
    
    
    def robinInterval(self, nums):
        pre, prepre = 0, 0
        
        for num in nums:
            res = max(num + prepre, pre) 
            prepre = pre
            pre = res
        
        return pre
```


### Related Problems
[House Robber](https://leetcode.com/problems/house-robber/) (Medium) <br>
[Paint House](https://leetcode.com/problems/paint-house/) (Medium) <br>
[Paint Fence](https://leetcode.com/problems/paint-fence/) (Medium) <br>
[House Robber III](https://leetcode.com/problems/house-robber-iii/) (Medium) <br>
[Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) (Hard) <br>
[Coin Path](https://leetcode.com/problems/coin-path/) (Hard) <br>



### What a(n) Medium problem!
Among **617919** total submissions, **232120** are accepted, with an acceptance rate of **37.6%**. <br>

- Likes: 2667
- Dislikes: 63

