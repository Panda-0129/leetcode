# [451] Sort Characters By Frequency (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/sort-characters-by-frequency/)  [![Heap_badge](https://img.shields.io/badge/topic-Heap-green.svg)](https://leetcode.com/problems/sort-characters-by-frequency/) 

:+1: 2195 &nbsp; &nbsp; :thumbsdown: 145

---

### My Solution


### Description
<p>Given a string, sort it in decreasing order based on the frequency of characters.</p>

<p><b>Example 1:</b>
<pre>
<b>Input:</b>
"tree"

<b>Output:</b>
"eert"

<b>Explanation:</b>
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
<b>Input:</b>
"cccaaa"

<b>Output:</b>
"cccaaa"

<b>Explanation:</b>
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
</pre>
</p>

<p><b>Example 3:</b>
<pre>
<b>Input:</b>
"Aabb"

<b>Output:</b>
"bbAa"

<b>Explanation:</b>
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
</pre>
</p>


### My Submission

- Language: Python
- Runtime: 68 ms
- Completed time: 2019-03-25 00:19:03

```Python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        res = []
        for ch in s:
            dict[ch] = dict.get(ch, 0) + 1

        sorted_x = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

        for ch, num in sorted_x:
            for i in range(0, num):
                res.append(ch)
        
        return "".join(res)
```


### Related Problems
[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) <br>
[First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (Easy) <br>
[Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) (Easy) <br>



### What a(n) Medium problem!
Among **378385** total submissions, **243875** are accepted, with an acceptance rate of **64.5%**. <br>

- Likes: 2195
- Dislikes: 145

