# [664] Strange Printer (Hard)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/strange-printer/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/strange-printer/) 

:+1: 530 &nbsp; &nbsp; :thumbsdown: 54

---

### My Solution


### Description
<p>
There is a strange printer with the following two special requirements:

<ol>
<li>The printer can only print a sequence of the same character each time.</li>
<li>At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.</li>
</ol>

</p>

<p>
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aaabbb"
<b>Output:</b> 2
<b>Explanation:</b> Print "aaa" first and then print "bbb".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "aba"
<b>Output:</b> 2
<b>Explanation:</b> Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
</pre>
</p>

<p><b>Hint</b>: Length of the given string will not exceed 100.</p>


### My Submission

- Language: Python
- Runtime: 656 ms
- Completed time: 2020-11-26 15:02:08

```Python
class Solution:
    def strangePrinter(self, s: str) -> int:
        length = len(s)
        if not length:
            return 0

        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        for i in range(length + 1):
            dp[i][i] = 1

        for interval in range(2, length + 1):
            for i in range(length):
                if i + interval - 1 >= length:
                    break
                j = i + interval - 1
                dp[i][j] = 1 + dp[i + 1][j]
                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])

        return dp[0][length - 1]
```


### Related Problems
[Remove Boxes](https://leetcode.com/problems/remove-boxes/) (Hard) <br>
[Strange Printer II](https://leetcode.com/problems/strange-printer-ii/) (Hard) <br>



### What a(n) Hard problem!
Among **40945** total submissions, **16882** are accepted, with an acceptance rate of **41.2%**. <br>

- Likes: 530
- Dislikes: 54

