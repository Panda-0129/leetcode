# [264] Ugly Number II (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/ugly-number-ii/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/ugly-number-ii/)  [![Heap_badge](https://img.shields.io/badge/topic-Heap-green.svg)](https://leetcode.com/problems/ugly-number-ii/) 

:+1: 2473 &nbsp; &nbsp; :thumbsdown: 155

---

### My Solution


### Description
<p>Given an integer <code>n</code>, return <em>the</em> <code>n<sup>th</sup></code> <em><strong>ugly number</strong></em>.</p>

<p><strong>Ugly number</strong> is a positive number whose prime factors only include <code>2</code>, <code>3</code>, and/or <code>5</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 12
<strong>Explanation:</strong> [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 is typically treated as an ugly number.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1690</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 152 ms
- Completed time: 2019-11-19 08:32:43

```Python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        index2, index3, index5 = 0, 0, 0

        while len(res) < n:
            multi2, multi3, multi5 = res[index2] * 2, res[index3] * 3, res[index5] * 5
            min_multi = min(multi2, multi3, multi5)
            if min_multi == multi2: index2 += 1
            if min_multi == multi3: index3 += 1
            if min_multi == multi5: index5 += 1
            res.append(min_multi)

        return res[-1]        
```


### Related Problems
[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) <br>
[Count Primes](https://leetcode.com/problems/count-primes/) (Easy) <br>
[Ugly Number](https://leetcode.com/problems/ugly-number/) (Easy) <br>
[Perfect Squares](https://leetcode.com/problems/perfect-squares/) (Medium) <br>
[Super Ugly Number](https://leetcode.com/problems/super-ugly-number/) (Medium) <br>
[Ugly Number III](https://leetcode.com/problems/ugly-number-iii/) (Medium) <br>



### What a(n) Medium problem!
Among **468656** total submissions, **201099** are accepted, with an acceptance rate of **42.9%**. <br>

- Likes: 2473
- Dislikes: 155

