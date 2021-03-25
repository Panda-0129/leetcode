# [648] Replace Words (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/replace-words/)  [![Trie_badge](https://img.shields.io/badge/topic-Trie-green.svg)](https://leetcode.com/problems/replace-words/) 

:+1: 944 &nbsp; &nbsp; :thumbsdown: 143

---

### My Solution


### Description
<p>In English, we have a concept called <strong>root</strong>, which can be followed by some other word&nbsp;to form another longer word - let&#39;s call this word <strong>successor</strong>. For example, when the <strong>root</strong> <code>&quot;an&quot;</code> is&nbsp;followed by the <strong>successor</strong>&nbsp;word&nbsp;<code>&quot;other&quot;</code>, we&nbsp;can form a new word <code>&quot;another&quot;</code>.</p>

<p>Given a <code>dictionary</code> consisting of many <strong>roots</strong> and a <code>sentence</code>&nbsp;consisting of words separated by spaces, replace all the <strong>successors</strong> in the sentence with the <strong>root</strong> forming it. If a <strong>successor</strong> can be replaced by more than one <strong>root</strong>,&nbsp;replace it with the <strong>root</strong> that has&nbsp;<strong>the shortest length</strong>.</p>

<p>Return <em>the <code>sentence</code></em> after the replacement.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
<strong>Output:</strong> "the cat was rat by the bat"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
<strong>Output:</strong> "a a b c"
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
<strong>Output:</strong> "a a a a a a a a bbb baba a"
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
<strong>Output:</strong> "the cat was rat by the bat"
</pre><p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
<strong>Output:</strong> "it is ab that this solution is ac"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= dictionary.length&nbsp;&lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li><code>dictionary[i]</code>&nbsp;consists of only lower-case letters.</li>
	<li><code>1 &lt;= sentence.length &lt;= 10^6</code></li>
	<li><code>sentence</code>&nbsp;consists of only lower-case letters and spaces.</li>
	<li>The number of words in&nbsp;<code>sentence</code>&nbsp;is in the range <code>[1, 1000]</code></li>
	<li>The length of each word in&nbsp;<code>sentence</code>&nbsp;is in the range <code>[1, 1000]</code></li>
	<li>Each two consecutive words in&nbsp;<code>sentence</code>&nbsp;will be separated by exactly one space.</li>
	<li><code>sentence</code>&nbsp;does not have leading or trailing spaces.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 288 ms
- Completed time: 2019-09-23 15:21:37

```Python
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        prefixSet = set(dict)
        
        def successorWord(word):
            for i in range(1, len(word)):
                if word[:i] in prefixSet:
                    return word[:i]
            return word

        return ' '.join(successorWord(word) for word in sentence.split(' '))
```


### Related Problems
[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) (Medium) <br>



### What a(n) Medium problem!
Among **115991** total submissions, **68083** are accepted, with an acceptance rate of **58.7%**. <br>

- Likes: 944
- Dislikes: 143
