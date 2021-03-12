# [670] Maximum Swap (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/maximum-swap/)  [![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/maximum-swap/) 

:+1: 1403 &nbsp; &nbsp; :thumbsdown: 88

---

### My Solution


### Description
<p>
Given a non-negative integer, you could swap two digits <b>at most</b> once to get the maximum valued number. Return the maximum valued number you could get.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 2736
<b>Output:</b> 7236
<b>Explanation:</b> Swap the number 2 and the number 7.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 9973
<b>Output:</b> 9973
<b>Explanation:</b> No swap.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The given number is in the range [0, 10<sup>8</sup>]</li>
</ol>
</p>


### My Submission

- Language: Python
- Runtime: 16 ms
- Completed time: 2019-09-10 15:32:27

```Python
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        tmpNum = list(str(num))
        currentMinPos = 0
        currentMaxPos = len(tmpNum) - 1
        leftMin, rightMax = 0, 0
        
        for i in reversed(range(len(tmpNum))):
            if tmpNum[i] < tmpNum[currentMaxPos]:
                leftMin, rightMax = i, currentMaxPos
            elif tmpNum[i] > tmpNum[currentMaxPos]:
                currentMaxPos = i

        tmpNum[leftMin], tmpNum[rightMax] = tmpNum[rightMax], tmpNum[leftMin]
    
        return int("".join(tmpNum))  
```


### Related Problems
[Create Maximum Number](https://leetcode.com/problems/create-maximum-number/) (Hard) <br>



### What a(n) Medium problem!
Among **207444** total submissions, **93712** are accepted, with an acceptance rate of **45.2%**. <br>

- Likes: 1403
- Dislikes: 88

