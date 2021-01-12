# [11] Container With Most Water (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/container-with-most-water/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/container-with-most-water/) 

:+1: 8028 &nbsp; &nbsp; :thumbsdown: 649

---

### My Solution


### Description
<p>Given <code>n</code> non-negative integers <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code><sub>&nbsp;</sub>, where each represents a point at coordinate <code>(i, a<sub>i</sub>)</code>. <code>n</code> vertical lines are drawn such that the two endpoints of the line <code>i</code> is at <code>(i, a<sub>i</sub>)</code> and <code>(i, 0)</code>. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.</p>

<p><strong>Notice</strong>&nbsp;that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" />
<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain&nbsp;is 49.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> height = [4,3,2,1,4]
<strong>Output:</strong> 16
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> height = [1,2,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 128 ms
- Completed time: 2019-12-10 22:02:42

```Python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index, right_index, width, res = 0, len(height) - 1, len(height) - 1, 0
        for index in range(width, 0, -1):
            if height[left_index] < height[right_index]:
                res = max(res, index * height[left_index])
                left_index += 1
            else:
                res = max(res, index * height[right_index])
                right_index -= 1
        return res
```


### Related Problems
[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) <br>



### What a(n) Medium problem!
Among **1565223** total submissions, **816367** are accepted, with an acceptance rate of **52.2%**. <br>

- Likes: 8028
- Dislikes: 649

