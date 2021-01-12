# [739] Daily Temperatures (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/daily-temperatures/)  [![Stack_badge](https://img.shields.io/badge/topic-Stack-green.svg)](https://leetcode.com/problems/daily-temperatures/) 

:+1: 3684 &nbsp; &nbsp; :thumbsdown: 114

---

### My Solution


### Description
<p>
Given a list of daily temperatures <code>T</code>, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put <code>0</code> instead.
</p><p>
For example, given the list of temperatures <code>T = [73, 74, 75, 71, 69, 72, 76, 73]</code>, your output should be <code>[1, 1, 4, 2, 1, 1, 0, 0]</code>.
</p>

<p><b>Note:</b>
The length of <code>temperatures</code> will be in the range <code>[1, 30000]</code>.
Each temperature will be an integer in the range <code>[30, 100]</code>.
</p>


### My Submission

- Language: Python
- Runtime: 436 ms
- Completed time: 2019-09-28 10:04:28

```Python
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(T)

        for index, value in enumerate(T):
            while stack and value > T[stack[-1]]:
                top = stack.pop()
                res[top] = index - top

            stack.append(index)

        return res
```


### Related Problems
[Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) (Easy) <br>



### What a(n) Medium problem!
Among **323501** total submissions, **208124** are accepted, with an acceptance rate of **64.3%**. <br>

- Likes: 3684
- Dislikes: 114

