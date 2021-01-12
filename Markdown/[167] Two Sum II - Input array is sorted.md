# [167] Two Sum II - Input array is sorted (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) 

:+1: 2227 &nbsp; &nbsp; :thumbsdown: 678

---

### My Solution


### Description
<p>Given an array of integers that is already <strong><em>sorted in ascending order</em></strong>, find two numbers such that they add up to a specific target number.</p>

<p>The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Your returned answers (both index1 and index2) are not zero-based.</li>
	<li>You may assume that each input would have <em>exactly</em> one solution and you may not use the <em>same</em> element twice.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> numbers = [2,7,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> numbers = [2,3,4], target = 6
<strong>Output:</strong> [1,3]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> numbers = [-1,0], target = -1
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums</code>&nbsp;is sorted in <strong>increasing order</strong>.</li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-03-23 23:15:36

```Python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i <= j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            elif sum > target:
                j-=1
            else:
                i+=1
```


### Related Problems
[Two Sum](https://leetcode.com/problems/two-sum/) (Easy) <br>
[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) (Easy) <br>
[Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) (Easy) <br>



### What a(n) Easy problem!
Among **912935** total submissions, **505485** are accepted, with an acceptance rate of **55.4%**. <br>

- Likes: 2227
- Dislikes: 678

