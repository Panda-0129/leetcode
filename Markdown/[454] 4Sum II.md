# [454] 4Sum II (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/4sum-ii/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/4sum-ii/) 

:+1: 1694 &nbsp; &nbsp; :thumbsdown: 82

---

### My Solution


### Description
<p>Given four lists A, B, C, D of integer values, compute how many tuples <code>(i, j, k, l)</code> there are such that <code>A[i] + B[j] + C[k] + D[l]</code> is zero.</p>

<p>To make problem a bit easier, all A, B, C, D have same length of N where 0 &le; N &le; 500. All integers are in the range of -2<sup>28</sup> to 2<sup>28</sup> - 1 and the result is guaranteed to be at most 2<sup>31</sup> - 1.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

<b>Output:</b>
2

<b>Explanation:</b>
The two tuples are:
1. (0, 0, 0, 1) -&gt; A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -&gt; A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
</pre>

<p>&nbsp;</p>



### My Submission

- Language: Python
- Runtime: 296 ms
- Completed time: 2019-04-03 21:29:41

```Python
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        count = 0
        
        for a in A:
            for b in B:
                if a+b not in dic:
                    dic[a+b] = 1
                elif a+b in dic:
                    dic[a+b] += 1
        
        for c in C:
            for d in D:
                if -c-d in dic:
                    count += dic[-c-d]
        
        return count
```


### Related Problems
[4Sum](https://leetcode.com/problems/4sum/) (Medium) <br>



### What a(n) Medium problem!
Among **272818** total submissions, **148758** are accepted, with an acceptance rate of **54.5%**. <br>

- Likes: 1694
- Dislikes: 82

