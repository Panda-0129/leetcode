# [435] Non-overlapping Intervals (Medium)

[![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/non-overlapping-intervals/) 

:+1: 1786 &nbsp; &nbsp; :thumbsdown: 48

---

### My Solution


### Description
<p>Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.</p>

<ol>
</ol>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [[1,2],[2,3],[3,4],[1,3]]
<b>Output:</b> 1
<b>Explanation:</b> [1,3] can be removed and the rest of intervals are non-overlapping.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [[1,2],[1,2],[1,2]]
<b>Output:</b> 2
<b>Explanation:</b> You need to remove two [1,2] to make the rest of intervals non-overlapping.
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> [[1,2],[2,3]]
<b>Output:</b> 0
<b>Explanation:</b> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>You may assume the interval&#39;s end point is always bigger than its start point.</li>
	<li>Intervals like [1,2] and [2,3] have borders &quot;touching&quot; but they don&#39;t overlap each other.</li>
</ol>



### My Submission

- Language: Python
- Runtime: 72 ms
- Completed time: 2019-03-26 23:42:58

```Python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x.end)
        count = 1
        end = intervals[0].end
        for interval in intervals:
            if interval.start < end:
                continue
            end = interval.end
            count+=1
        
        return len(intervals) - count
```


### Related Problems
[Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium) <br>



### What a(n) Medium problem!
Among **282574** total submissions, **123818** are accepted, with an acceptance rate of **43.8%**. <br>

- Likes: 1786
- Dislikes: 48

