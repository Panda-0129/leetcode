# [215] Kth Largest Element in an Array (Medium)

[![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/kth-largest-element-in-an-array/)  [![Heap_badge](https://img.shields.io/badge/topic-Heap-green.svg)](https://leetcode.com/problems/kth-largest-element-in-an-array/) 

:+1: 5267 &nbsp; &nbsp; :thumbsdown: 339

---

### My Solution


### Description
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>largest element in the array</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,1,5,6,4], k = 2
<strong>Output:</strong> 5
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3,1,2,4,5,5,6], k = 4
<strong>Output:</strong> 4
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 116 ms
- Completed time: 2019-03-24 21:37:44

```Python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse = True)
        
        return nums[k - 1]


```


### Related Problems
[Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) (Medium) <br>
[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) <br>
[Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) (Easy) <br>
[Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) (Easy) <br>
[K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (Medium) <br>



### What a(n) Medium problem!
Among **1447415** total submissions, **847725** are accepted, with an acceptance rate of **58.6%**. <br>

- Likes: 5267
- Dislikes: 339

