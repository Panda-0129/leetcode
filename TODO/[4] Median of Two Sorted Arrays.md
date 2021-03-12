# [4] Median of Two Sorted Arrays (Hard)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/median-of-two-sorted-arrays/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/median-of-two-sorted-arrays/)  [![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/median-of-two-sorted-arrays/) 

:+1: 9411 &nbsp; &nbsp; :thumbsdown: 1453

---

### My Solution


### Description
<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0,0], nums2 = [0,0]
<strong>Output:</strong> 0.00000
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [], nums2 = [1]
<strong>Output:</strong> 1.00000
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2], nums2 = []
<strong>Output:</strong> 2.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> The overall run time complexity should be <code>O(log (m+n))</code>.


### My Submission

- Language: Python
- Runtime: 156 ms
- Completed time: 2020-12-17 10:58:32

```Python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        def getKth(nums1, start1, end1, nums2, start2, end2, k):
            length1 = end1 - start1 + 1
            length2 = end2 - start2 + 1
            
            if length1 > length2:
                return getKth(nums2, start2, end2, nums1, start1, end1, k)
            
            if length1 == 0:
                return nums2[start2 + k - 1]
            
            if k == 1:
                return min(nums1[start1], nums2[start2])
            
            
            i = start1 + min(length1, int(k / 2)) - 1
            j = start2 + min(length2, int(k / 2)) - 1
            
            if nums1[i] < nums2[j]:
                return getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
            else:
                return getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
            
        n = len(nums1)
        m = len(nums2)
        
        left = int((n + m + 1) / 2)
        right = int((n + m + 2) / 2)
        
        return (getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + 
               getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) * 0.5
```


### Related Problems




### What a(n) Hard problem!
Among **2825915** total submissions, **880461** are accepted, with an acceptance rate of **31.2%**. <br>

- Likes: 9411
- Dislikes: 1453

