# [278] First Bad Version (Easy)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/first-bad-version/) 

:+1: 1877 &nbsp; &nbsp; :thumbsdown: 777

---

### My Solution


### Description
<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which returns whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5, bad = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
call isBadVersion(3) -&gt; false
call isBadVersion(5)&nbsp;-&gt; true
call isBadVersion(4)&nbsp;-&gt; true
Then 4 is the first bad version.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, bad = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bad &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 20 ms
- Completed time: 2019-04-01 20:58:45

```Python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid - 1
            elif not isBadVersion(mid):
                low = mid + 1
            
        return low
```


### Related Problems
[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium) <br>
[Search Insert Position](https://leetcode.com/problems/search-insert-position/) (Easy) <br>
[Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) (Easy) <br>



### What a(n) Easy problem!
Among **1384047** total submissions, **513897** are accepted, with an acceptance rate of **37.1%**. <br>

- Likes: 1877
- Dislikes: 777

