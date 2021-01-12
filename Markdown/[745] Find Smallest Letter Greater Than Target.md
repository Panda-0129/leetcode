# [745] Find Smallest Letter Greater Than Target (Easy)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) 

:+1: 539 &nbsp; &nbsp; :thumbsdown: 645

---

### My Solution


### Description
<p>
Given a list of sorted characters <code>letters</code> containing only lowercase letters, and given a target letter <code>target</code>, find the smallest element in the list that is larger than the given target.
</p><p>
Letters also wrap around.  For example, if the target is <code>target = 'z'</code> and <code>letters = ['a', 'b']</code>, the answer is <code>'a'</code>.
</p>

<p><b>Examples:</b><br />
<pre>
<b>Input:</b>
letters = ["c", "f", "j"]
target = "a"
<b>Output:</b> "c"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "c"
<b>Output:</b> "f"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "d"
<b>Output:</b> "f"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "g"
<b>Output:</b> "j"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "j"
<b>Output:</b> "c"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "k"
<b>Output:</b> "c"
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>letters</code> has a length in range <code>[2, 10000]</code>.</li>
<li><code>letters</code> consists of lowercase letters, and contains at least 2 unique letters.</li>
<li><code>target</code> is a lowercase letter.</li>
</ol>
</p>


### My Submission

- Language: Python
- Runtime: 220 ms
- Completed time: 2019-03-31 23:43:07

```Python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for letter in letters:
            if letter > target:
                return letter
        
        return letters[0]
```


### Related Problems




### What a(n) Easy problem!
Among **201585** total submissions, **91958** are accepted, with an acceptance rate of **45.6%**. <br>

- Likes: 539
- Dislikes: 645

