# [768] Partition Labels (Medium)

[![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/partition-labels/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/partition-labels/) 

:+1: 4258 &nbsp; &nbsp; :thumbsdown: 181

---

### My Solution


### Description
<p>A string <code>S</code> of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> S = &quot;ababcbacadefegdehijhklij&quot;
<b>Output:</b> [9,7,8]
<b>Explanation:</b>
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits S into less parts.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>S</code> will have length in range <code>[1, 500]</code>.</li>
	<li><code>S</code> will consist of lowercase English&nbsp;letters (<code>&#39;a&#39;</code> to <code>&#39;z&#39;</code>) only.</li>
</ul>

<p>&nbsp;</p>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-03-30 22:47:57

```Python
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        dic = {}

        for i in range(0, len(S)):
            if S[i] not in dic:
                dic[S[i]] = [i, i]
            if S[i] in dic:
                dic[S[i]][1] = i

        dic = sorted(dic.values())
        tmp = []

        for element in dic:
            start, end = element
            if len(tmp) == 0:
                tmp.append(element)
            else:
                if tmp[-1][1] > start:
                    tmp[-1][1] = max(tmp[-1][1], end)
                else:
                    tmp.append(element)

        return [x[1] - x[0] + 1 for x in tmp]
            
        
```


### Related Problems
[Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) <br>



### What a(n) Medium problem!
Among **308677** total submissions, **241014** are accepted, with an acceptance rate of **78.1%**. <br>

- Likes: 4258
- Dislikes: 181

