# [878] Shifting Letters (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/shifting-letters/) 

:+1: 337 &nbsp; &nbsp; :thumbsdown: 64

---

### My Solution


### Description
<p>We have a string <code>S</code> of lowercase letters, and an integer array <code>shifts</code>.</p>

<p>Call the <em>shift</em> of a letter, the next letter in the alphabet, (wrapping around so that <code>&#39;z&#39;</code> becomes <code>&#39;a&#39;</code>).&nbsp;</p>

<p>For example, <code>shift(&#39;a&#39;) = &#39;b&#39;</code>, <code>shift(&#39;t&#39;) = &#39;u&#39;</code>, and <code>shift(&#39;z&#39;) = &#39;a&#39;</code>.</p>

<p>Now for each <code>shifts[i] = x</code>, we want to shift the first <code>i+1</code>&nbsp;letters of <code>S</code>, <code>x</code> times.</p>

<p>Return the final string&nbsp;after all such shifts to <code>S</code> are applied.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = &quot;abc&quot;, shifts = [3,5,9]
<strong>Output: </strong>&quot;rpl&quot;
<strong>Explanation: </strong>
We start with &quot;abc&quot;.
After shifting the first 1 letters of S by 3, we have &quot;dbc&quot;.
After shifting the first 2 letters of S by 5, we have &quot;igc&quot;.
After shifting the first 3 letters of S by 9, we have &quot;rpl&quot;, the answer.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length = shifts.length &lt;= 20000</code></li>
	<li><code>0 &lt;= shifts[i] &lt;= 10 ^ 9</code></li>
</ol>



### My Submission

- Language: Python
- Runtime: 168 ms
- Completed time: 2019-09-26 19:42:54

```Python
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        current_sum = sum(shifts)
        start = ord('a')
        res = ""

        for index in range(len(shifts)):
            res += chr((ord(S[index]) + current_sum - start) % 26 + start)
            current_sum -= shifts[index]

        return res
```


### Related Problems




### What a(n) Medium problem!
Among **60975** total submissions, **27484** are accepted, with an acceptance rate of **45.1%**. <br>

- Likes: 337
- Dislikes: 64

