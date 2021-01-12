# [264] Ugly Number II (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/ugly-number-ii/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/ugly-number-ii/)  [![Heap_badge](https://img.shields.io/badge/topic-Heap-green.svg)](https://leetcode.com/problems/ugly-number-ii/) 

:+1: 2352 &nbsp; &nbsp; :thumbsdown: 148

---

### My Solution


### Description
<p>Write a program to find the <code>n</code>-th ugly number.</p>

<p>Ugly numbers are<strong> positive numbers</strong> whose prime factors only include <code>2, 3, 5</code>.&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 12
<strong>Explanation: </strong><code>1, 2, 3, 4, 5, 6, 8, 9, 10, 12</code> is the sequence of the first <code>10</code> ugly numbers.</pre>

<p><strong>Note: </strong>&nbsp;</p>

<ol>
	<li><code>1</code> is typically treated as an ugly number.</li>
	<li><code>n</code> <b>does not exceed 1690</b>.</li>
</ol>


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
Among **458897** total submissions, **195997** are accepted, with an acceptance rate of **42.7%**. <br>

- Likes: 2352
- Dislikes: 148

