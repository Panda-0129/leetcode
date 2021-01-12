# [215] Kth Largest Element in an Array (Medium)

[![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/kth-largest-element-in-an-array/)  [![Heap_badge](https://img.shields.io/badge/topic-Heap-green.svg)](https://leetcode.com/problems/kth-largest-element-in-an-array/) 

:+1: 4824 &nbsp; &nbsp; :thumbsdown: 312

---

### My Solution


### Description
<p>Find the <strong>k</strong>th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[3,2,1,5,6,4] </code>and k = 2
<strong>Output:</strong> 5
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[3,2,3,1,2,4,5,5,6] </code>and k = 4
<strong>Output:</strong> 4</pre>

<p><strong>Note: </strong><br />
You may assume k is always valid, 1 &le; k &le; array&#39;s length.</p>



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
Among **1357072** total submissions, **780024** are accepted, with an acceptance rate of **57.5%**. <br>

- Likes: 4824
- Dislikes: 312

