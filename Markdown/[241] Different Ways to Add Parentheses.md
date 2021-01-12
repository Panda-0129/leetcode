# [241] Different Ways to Add Parentheses (Medium)

[![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/different-ways-to-add-parentheses/) 

:+1: 1985 &nbsp; &nbsp; :thumbsdown: 105

---

### My Solution


### Description
<p>Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are <code>+</code>, <code>-</code> and <code>*</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>&quot;2-1-1&quot;</code>
<b>Output:</b> <code>[0, 2]</code>
<strong>Explanation: </strong>
((2-1)-1) = 0 
(2-(1-1)) = 2</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input: </b><code>&quot;2*3-4*5&quot;</code>
<b>Output:</b> <code>[-34, -14, -10, -10, 10]</code>
<strong>Explanation: 
</strong>(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10<strong>
</strong></pre>


### My Submission

- Language: Python
- Runtime: 56 ms
- Completed time: 2020-10-21 10:38:12

```Python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        memo = {}
        res = []
        
        if '*' not in input and '+' not in input and '-' not in input:
            res.append(int(input))
        
        if input in memo:
            return memo[input]
        
        for i, ch in enumerate(input):
            if ch in "*+-":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])

                res.extend(eval(str(l) + ch + str(r)) for l in left for r in right)
            
        
        return res
```


### Related Problems
[Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) (Medium) <br>
[Basic Calculator](https://leetcode.com/problems/basic-calculator/) (Hard) <br>
[Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) (Hard) <br>



### What a(n) Medium problem!
Among **202186** total submissions, **115106** are accepted, with an acceptance rate of **56.9%**. <br>

- Likes: 1985
- Dislikes: 105

