# [75] Sort Colors (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/sort-colors/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/sort-colors/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/sort-colors/) 

:+1: 4645 &nbsp; &nbsp; :thumbsdown: 266

---

### My Solution


### Description
<p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>&nbsp;</strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>Here, we will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent the color red, white, and blue respectively.</p>

<p><strong>Follow up:</strong></p>

<ul>
	<li>Could you&nbsp;solve this problem without using&nbsp;the library&#39;s sort function?</li>
	<li>Could you come up with a&nbsp;one-pass algorithm using only <code>O(1)</code> constant space?</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,0,1]
<strong>Output:</strong> [0,1,2]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-03-26 21:32:12

```Python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index, left, right =0, 0, len(nums)-1
        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left+=1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right-=1
                index-=1
            index+=1
```


### Related Problems
[Sort List](https://leetcode.com/problems/sort-list/) (Medium) <br>
[Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) (Medium) <br>
[Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) (Medium) <br>



### What a(n) Medium problem!
Among **1248381** total submissions, **610314** are accepted, with an acceptance rate of **48.9%**. <br>

- Likes: 4645
- Dislikes: 266

