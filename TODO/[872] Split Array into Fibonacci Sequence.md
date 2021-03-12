# [872] Split Array into Fibonacci Sequence (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) 

:+1: 604 &nbsp; &nbsp; :thumbsdown: 199

---

### My Solution


### Description
<p>Given a string <code>S</code>&nbsp;of digits, such as <code>S = &quot;123456579&quot;</code>, we can split it into a <em>Fibonacci-like sequence</em>&nbsp;<code>[123, 456, 579].</code></p>

<p>Formally, a Fibonacci-like sequence is a list&nbsp;<code>F</code> of non-negative integers such that:</p>

<ul>
	<li><code>0 &lt;= F[i] &lt;= 2^31 - 1</code>, (that is,&nbsp;each integer fits a 32-bit signed integer type);</li>
	<li><code>F.length &gt;= 3</code>;</li>
	<li>and<code> F[i] + F[i+1] = F[i+2] </code>for all <code>0 &lt;= i &lt; F.length - 2</code>.</li>
</ul>

<p>Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.</p>

<p>Return any Fibonacci-like sequence split from <code>S</code>, or return <code>[]</code> if it cannot be done.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;123456579&quot;
<strong>Output: </strong>[123,456,579]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;11235813&quot;
<strong>Output: </strong>[1,1,2,3,5,8,13]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;112358130&quot;
<strong>Output: </strong>[]
<strong>Explanation: </strong>The task is impossible.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>&quot;0123&quot;
<strong>Output: </strong>[]
<strong>Explanation: </strong>Leading zeroes are not allowed, so &quot;01&quot;, &quot;2&quot;, &quot;3&quot; is not valid.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong>&quot;1101111&quot;
<strong>Output: </strong>[110, 1, 111]
<strong>Explanation: </strong>The output [11, 0, 11, 11] would also be accepted.
</pre>

<p><strong>Note: </strong></p>

<ol>
	<li><code>1 &lt;= S.length&nbsp;&lt;= 200</code></li>
	<li><code>S</code> contains only digits.</li>
</ol>



### My Submission

- Language: Python
- Runtime: 32 ms
- Completed time: 2020-10-28 10:53:07

```Python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def helper(idx, cur_res):
            if idx == len(S) and len(cur_res) >= 3:
                res.append(cur_res)
                return

            if len(cur_res) < 2:
                for index in range(idx, len(S)):
                    cur_string = S[idx:index + 1]
                    if (cur_string[0] == '0' and len(cur_string) > 1) or int(cur_string) > 2 ** 31 - 1:
                        return
                    helper(index + 1, cur_res + [int(cur_string)])

            else:
                former_sum = cur_res[-1] + cur_res[-2]
                if S[idx: idx + len(str(former_sum))] == str(former_sum) and former_sum < 2 ** 31 - 1:
                    helper(idx + len(str(former_sum)), cur_res + [former_sum])
                else:
                    return

        res = []
        helper(0, [])

        return res[0] if res else res
```


### Related Problems
[Additive Number](https://leetcode.com/problems/additive-number/) (Medium) <br>
[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (Easy) <br>



### What a(n) Medium problem!
Among **66554** total submissions, **24592** are accepted, with an acceptance rate of **37.0%**. <br>

- Likes: 604
- Dislikes: 199

