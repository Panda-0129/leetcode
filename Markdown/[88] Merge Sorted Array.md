# [88] Merge Sorted Array (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/merge-sorted-array/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/merge-sorted-array/) 

:+1: 3199 &nbsp; &nbsp; :thumbsdown: 4843

---

### My Solution


### Description
<p>Given two sorted integer arrays <code>nums1</code> and <code>nums2</code>, merge <code>nums2</code> into <code>nums1</code> as one sorted array.</p>

<p>The number of elements initialized in <code>nums1</code> and <code>nums2</code> are <code>m</code> and <code>n</code> respectively. You may assume that <code>nums1</code> has enough space (size that is&nbsp;equal to <code>m + n</code>) to hold additional elements from <code>nums2</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>Output:</strong> [1,2,2,3,5,6]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums1 = [1], m = 1, nums2 = [], n = 0
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n, m &lt;= 200</code></li>
	<li><code>1 &lt;= n + m &lt;= 200</code></li>
	<li><code>nums1.length == m + n</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-03-24 19:59:00

```Python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        indexMerge = m + n -1
        index2 = n - 1
        while indexMerge > m - 1:
            nums1[indexMerge] = nums2[index2]
            indexMerge-=1
            index2-=1
        
        nums1.sort()
        
    
```


### Related Problems
[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) <br>
[Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) (Easy) <br>
[Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) (Medium) <br>



### What a(n) Easy problem!
Among **1902162** total submissions, **770997** are accepted, with an acceptance rate of **40.5%**. <br>

- Likes: 3199
- Dislikes: 4843

