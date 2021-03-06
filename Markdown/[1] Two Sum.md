# [1] Two Sum (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/two-sum/)  [![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/two-sum/) 

:+1: 18705 &nbsp; &nbsp; :thumbsdown: 662

---

### My Solution


### Description
<p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Output:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>3</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>



### My Submission

- Language: Python
- Runtime: 4756 ms
- Completed time: 2019-12-09 16:41:21

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            for j in range(index + 1, len(nums)):
                if nums[j] == target - num:
                    return [index, j]
```


### Related Problems
[3Sum](https://leetcode.com/problems/3sum/) (Medium) <br>
[4Sum](https://leetcode.com/problems/4sum/) (Medium) <br>
[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Easy) <br>
[Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) (Easy) <br>
[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium) <br>
[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) (Easy) <br>
[Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) (Easy) <br>
[Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) (Medium) <br>
[Count Good Meals](https://leetcode.com/problems/count-good-meals/) (Medium) <br>



### What a(n) Easy problem!
Among **8054061** total submissions, **3719119** are accepted, with an acceptance rate of **46.2%**. <br>

- Likes: 18705
- Dislikes: 662

