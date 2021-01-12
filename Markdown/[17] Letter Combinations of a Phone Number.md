# [17] Letter Combinations of a Phone Number (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)  [![Recursion_badge](https://img.shields.io/badge/topic-Recursion-green.svg)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) 

:+1: 5118 &nbsp; &nbsp; :thumbsdown: 478

---

### My Solution


### Description
<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>

<p>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" style="width: 200px; height: 162px;" /></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;,&quot;ae&quot;,&quot;af&quot;,&quot;bd&quot;,&quot;be&quot;,&quot;bf&quot;,&quot;cd&quot;,&quot;ce&quot;,&quot;cf&quot;]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;&quot;
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;2&quot;
<strong>Output:</strong> [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> is a digit in the range <code>[&#39;2&#39;, &#39;9&#39;]</code>.</li>
</ul>


### My Submission

- Language: Python
- Runtime: 24 ms
- Completed time: 2019-12-12 08:54:48

```Python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [''] if digits else []

        for digit in digits:
            current_string = dict[digit]
            current_res = []
            for comb in res:
                for letter in current_string:
                    current_res.append(comb + letter)
            res = current_res

        return res
```


### Related Problems
[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium) <br>
[Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) <br>
[Binary Watch](https://leetcode.com/problems/binary-watch/) (Easy) <br>



### What a(n) Medium problem!
Among **1512619** total submissions, **735048** are accepted, with an acceptance rate of **48.6%**. <br>

- Likes: 5118
- Dislikes: 478

