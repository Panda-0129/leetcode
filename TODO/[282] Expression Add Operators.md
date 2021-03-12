# [282] Expression Add Operators (Hard)

[![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/expression-add-operators/) 

:+1: 1597 &nbsp; &nbsp; :thumbsdown: 268

---

### My Solution


### Description
<p>Given a string that contains only digits <code>0-9</code> and a target value, return all possibilities to add <b>binary</b> operators (not unary) <code>+</code>, <code>-</code>, or <code>*</code> between the digits so they evaluate to the target value.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;123&quot;, <em>target</em> = 6
<b>Output: </b>[&quot;1+2+3&quot;, &quot;1*2*3&quot;] 
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;232&quot;, <em>target</em> = 8
<b>Output: </b>[&quot;2*3+2&quot;, &quot;2+3*2&quot;]</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;105&quot;, <em>target</em> = 5
<b>Output: </b>[&quot;1*0+5&quot;,&quot;10-5&quot;]</pre>

<p><b>Example 4:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;00&quot;, <em>target</em> = 0
<b>Output: </b>[&quot;0+0&quot;, &quot;0-0&quot;, &quot;0*0&quot;]
</pre>

<p><b>Example 5:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;3456237490&quot;, <em>target</em> = 9191
<b>Output: </b>[]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num.length &lt;= 10</code></li>
	<li><code>num</code> only contain&nbsp;digits.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 1012 ms
- Completed time: 2020-10-21 11:49:47

```Python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def dfs(num, target, path, diff, cur_sum, res):
            if not num and cur_sum == target:
                res.append(path[:])
                return

            for i in range(1, len(num) + 1):
                if i == 1 or (i > 1 and num[0] != '0'):
                    dfs(num[i:], target, path + '+' + num[:i], int(num[:i]), cur_sum + int(num[:i]), res)
                    dfs(num[i:], target, path + '-' + num[:i], -int(num[:i]), cur_sum - int(num[:i]), res)
                    dfs(num[i:], target, path + '*' + num[:i], diff * int(num[:i]), cur_sum - diff + diff * int(num[:i]), res)

        res = []
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                dfs(num[i:], target, num[:i], int(num[:i]), int(num[:i]), res)
       
        return res
```


### Related Problems
[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (Medium) <br>
[Basic Calculator](https://leetcode.com/problems/basic-calculator/) (Hard) <br>
[Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) (Medium) <br>
[Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) (Medium) <br>
[Target Sum](https://leetcode.com/problems/target-sum/) (Medium) <br>



### What a(n) Hard problem!
Among **345300** total submissions, **127086** are accepted, with an acceptance rate of **36.8%**. <br>

- Likes: 1597
- Dislikes: 268

