# [605] Can Place Flowers (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/can-place-flowers/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/can-place-flowers/) 

:+1: 1326 &nbsp; &nbsp; :thumbsdown: 448

---

### My Solution


### Description
<p>You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in <strong>adjacent</strong> plots.</p>

<p>Given an integer array&nbsp;<code>flowerbed</code>&nbsp;containing <code>0</code>&#39;s and <code>1</code>&#39;s, where <code>0</code> means empty and <code>1</code> means not empty,&nbsp;and an integer <code>n</code>, return <em>if</em> <code>n</code> new flowers can be planted in the <code>flowerbed</code>&nbsp;without violating the no-adjacent-flowers rule.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 1
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 2
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= flowerbed.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>flowerbed[i]</code> is <code>0</code> or <code>1</code>.</li>
	<li>There are no two adjacent flowers in <code>flowerbed</code>.</li>
	<li><code>0 &lt;= n &lt;= flowerbed.length</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 328 ms
- Completed time: 2019-03-31 21:06:35

```Python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = 0

        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                next = 0
                prev = 0
                if i != len(flowerbed) - 1:
                    next = flowerbed[i+1]
                if i != 0:
                    prev = flowerbed[i-1]
                if next == 0 and prev == 0:
                    flowerbed[i] = 1
                    count+=1
        return count >= n
```


### Related Problems
[Teemo Attacking](https://leetcode.com/problems/teemo-attacking/) (Medium) <br>
[Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) (Medium) <br>



### What a(n) Easy problem!
Among **500224** total submissions, **158951** are accepted, with an acceptance rate of **31.8%**. <br>

- Likes: 1326
- Dislikes: 448

