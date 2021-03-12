# [42] Trapping Rain Water (Hard)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/trapping-rain-water/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/trapping-rain-water/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/trapping-rain-water/)  [![Stack_badge](https://img.shields.io/badge/topic-Stack-green.svg)](https://leetcode.com/problems/trapping-rain-water/) 

:+1: 10291 &nbsp; &nbsp; :thumbsdown: 155

---

### My Solution


### Description
<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" />
<pre>
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>0 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 1760 ms
- Completed time: 2021-03-11 15:13:02

```Python
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height)):
            max_left = max(height[:i])
            max_right = max(height[i:])
            cur_min = min(max_left, max_right)
            if cur_min > height[i]:
                res += (cur_min - height[i])
        
        return res
```


### Related Problems
[Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium) <br>
[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) <br>
[Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) (Hard) <br>
[Pour Water](https://leetcode.com/problems/pour-water/) (Medium) <br>



### What a(n) Hard problem!
Among **1352382** total submissions, **694139** are accepted, with an acceptance rate of **51.3%**. <br>

- Likes: 10291
- Dislikes: 155

