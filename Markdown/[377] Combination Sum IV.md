# [377] Combination Sum IV (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/combination-sum-iv/) 

:+1: 1788 &nbsp; &nbsp; :thumbsdown: 216

---

### My Solution


### Description
<p>Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.</p>

<p><b>Example:</b></p>

<pre>
<i><b>nums</b></i> = [1, 2, 3]
<i><b>target</b></i> = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is <i><b>7</b></i>.
</pre>

<p>&nbsp;</p>

<p><b>Follow up:</b><br />
What if negative numbers are allowed in the given array?<br />
How does it change the problem?<br />
What limitation we need to add to the question to allow negative numbers?</p>

<p><b>Credits:</b><br />
Special thanks to <a href="https://leetcode.com/pbrother/">@pbrother</a> for adding this problem and creating all test cases.</p>



### My Submission

- Language: Python
- Runtime: 48 ms
- Completed time: 2019-12-04 09:37:58

```Python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[target]        
```


### Related Problems
[Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) <br>



### What a(n) Medium problem!
Among **315222** total submissions, **144614** are accepted, with an acceptance rate of **45.9%**. <br>

- Likes: 1788
- Dislikes: 216

