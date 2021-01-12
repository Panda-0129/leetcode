# [127] Word Ladder (Hard)

[![Breadth-first%20Search_badge](https://img.shields.io/badge/topic-Breadth-first%20Search-green.svg)](https://leetcode.com/problems/word-ladder/) 

:+1: 4502 &nbsp; &nbsp; :thumbsdown: 1380

---

### My Solution


### Description
<p>Given two words <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>the length of the shortest transformation sequence from</em> <code>beginWord</code> <em>to</em> <code>endWord</code>, <em>such that</em>:</p>

<ul>
	<li>Only one letter can be changed at a time.</li>
	<li>Each transformed word must exist in the word list.</li>
</ul>

<p>Return <code>0</code> if there is no such transformation sequence.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> beginWord = &quot;hit&quot;, endWord = &quot;cog&quot;, wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]
<strong>Output:</strong> 5
<strong>Explanation:</strong> As one shortest transformation is &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;, return its length 5.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> beginWord = &quot;hit&quot;, endWord = &quot;cog&quot;, wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The endWord &quot;cog&quot; is not in wordList, therefore no possible transformation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;beginWord.length &lt;= 100</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 5000</code></li>
	<li><code>wordList[i].length ==&nbsp;beginWord.length</code></li>
	<li><code>beginWord</code>,&nbsp;<code>endWord</code>, and&nbsp;<code>wordList[i]</code> consist of lowercase English letters.</li>
	<li><code>beginWord !=&nbsp;endWord</code></li>
	<li>All the strings in&nbsp;<code>wordList</code> are <strong>unique</strong>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 536 ms
- Completed time: 2020-10-15 20:49:52

```Python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_dict = set(wordList)
        
        if endWord not in word_dict:
            return 0
        
        start_search = {beginWord}
        end_search = {endWord}
        length = len(beginWord)
        
        word_dict.remove(endWord)
        
        step = 0
        while len(start_search) > 0 and len(end_search) > 0:
            step += 1
            if len(start_search) < len(end_search):
                start_search, end_search = end_search, start_search
            
            tmp = set()
            for w in start_search:
                new_words = [
                    w[:i] + ch + w[i + 1:] for ch in string.ascii_lowercase for i in range(length)
                ]
                
                for new_word in new_words:
                    if new_word in end_search:
                        return step + 1
                    if new_word not in word_dict:
                        continue
                    word_dict.remove(new_word)
                    tmp.add(new_word)
                
                start_search = tmp
            
        
        return 0
            
```


### Related Problems
[Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) (Hard) <br>
[Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) (Medium) <br>



### What a(n) Hard problem!
Among **1687291** total submissions, **530276** are accepted, with an acceptance rate of **31.4%**. <br>

- Likes: 4502
- Dislikes: 1380

