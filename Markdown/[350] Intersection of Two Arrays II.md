# [350] Intersection of Two Arrays II (Easy)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/) 

:+1: 1899 &nbsp; &nbsp; :thumbsdown: 484

---

### My Solution


### Description
<p>Given two arrays, write a function to compute their intersection.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-1-1">[1,2,2,1]</span>, nums2 = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[2,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-2-1">[4,9,5]</span>, nums2 = <span id="example-input-2-2">[9,4,9,8,4]</span>
<strong>Output: </strong><span id="example-output-2">[4,9]</span></pre>
</div>

<p><b>Note:</b></p>

<ul>
	<li>Each element in the result should appear as many times as it shows in both arrays.</li>
	<li>The result can be in any order.</li>
</ul>

<p><b>Follow up:</b></p>

<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <i>nums1</i>&#39;s size is small compared to <i>nums2</i>&#39;s size? Which algorithm is better?</li>
	<li>What if elements of <i>nums2</i> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>



### My Submission

- Language: Python
- Runtime: 32 ms
- Completed time: 2020-09-01 15:03:32

```Python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = {}
        for num in nums1:
            if num in tmp:
                tmp[num] += 1
            else:
                tmp[num] = 1
        
        k = 0
        for num in nums2:
            if num in tmp and tmp[num] > 0:
                tmp[num] -= 1
                nums2[k] = num
                k+=1
        
        return nums2[0:k]
        
```


### Related Problems
[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) (Easy) <br>
[Find Common Characters](https://leetcode.com/problems/find-common-characters/) (Easy) <br>



### What a(n) Easy problem!
Among **856068** total submissions, **444309** are accepted, with an acceptance rate of **51.9%**. <br>

- Likes: 1899
- Dislikes: 484

