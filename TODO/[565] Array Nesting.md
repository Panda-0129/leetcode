# [565] Array Nesting (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/array-nesting/) 

:+1: 993 &nbsp; &nbsp; :thumbsdown: 106

---

### My Solution


### Description
<p>A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.</p>

<p>Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]&hellip; By that analogy, we stop adding right before a duplicate element occurs in S.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> A = [5,4,0,3,1,6,2]
<b>Output:</b> 4
<b>Explanation:</b> 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>N is an integer within the range [1, 20,000].</li>
	<li>The elements of A are all distinct.</li>
	<li>Each element of A is an integer within the range [0, N-1].</li>
</ol>



### My Submission

- Language: Python
- Runtime: 144 ms
- Completed time: 2019-10-14 14:57:43

```Python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = -1
        count = 0
        for i in range(len(nums)):
            while nums[i] >= 0:
                tmp_i, nums[i] = nums[i], -1
                i = tmp_i
                count += 1
            res = max(res, count)
            count = 0
        return res
```


### Related Problems
[Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) (Medium) <br>
[Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) (Medium) <br>
[Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii/) (Medium) <br>



### What a(n) Medium problem!
Among **110654** total submissions, **61930** are accepted, with an acceptance rate of **56.0%**. <br>

- Likes: 993
- Dislikes: 106

