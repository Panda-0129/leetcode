# [212] Word Search II (Hard)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/word-search-ii/)  [![Trie_badge](https://img.shields.io/badge/topic-Trie-green.svg)](https://leetcode.com/problems/word-search-ii/) 

:+1: 3294 &nbsp; &nbsp; :thumbsdown: 140

---

### My Solution


### Description
<p>Given an <code>m x n</code> <code>board</code>&nbsp;of characters and a list of strings <code>words</code>, return <em>all words on the board</em>.</p>

<p>Each word must be constructed from letters of sequentially adjacent cells, where <strong>adjacent cells</strong> are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" style="width: 322px; height: 322px;" />
<pre>
<strong>Input:</strong> board = [[&quot;o&quot;,&quot;a&quot;,&quot;a&quot;,&quot;n&quot;],[&quot;e&quot;,&quot;t&quot;,&quot;a&quot;,&quot;e&quot;],[&quot;i&quot;,&quot;h&quot;,&quot;k&quot;,&quot;r&quot;],[&quot;i&quot;,&quot;f&quot;,&quot;l&quot;,&quot;v&quot;]], words = [&quot;oath&quot;,&quot;pea&quot;,&quot;eat&quot;,&quot;rain&quot;]
<strong>Output:</strong> [&quot;eat&quot;,&quot;oath&quot;]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> board = [[&quot;a&quot;,&quot;b&quot;],[&quot;c&quot;,&quot;d&quot;]], words = [&quot;abcb&quot;]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 12</code></li>
	<li><code>board[i][j]</code> is a lowercase English letter.</li>
	<li><code>1 &lt;= words.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
	<li>All the strings of <code>words</code> are unique.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 380 ms
- Completed time: 2020-10-13 10:37:16

```Python
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
                node = new_node
        
        node.is_end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        
        for ch in word:
            current_node = current_node.children.get(ch)
            if not current_node:
                return False
        
        return current_node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        
        for ch in prefix:
            current_node = current_node.children.get(ch)
            if not current_node:
                return False
            
        return True
    

class Solution:
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, node, i, j, path, res):
            if node.is_end == True:
                res.append(path)
                node.is_end = False

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            tmp = board[i][j]
            node = node.children.get(tmp)

            if not node:
                return

            board[i][j] = '*'

            dfs(board, node, i - 1, j, path + tmp, res)
            dfs(board, node, i + 1, j, path + tmp, res)
            dfs(board, node, i, j - 1, path + tmp, res)
            dfs(board, node, i, j + 1, path + tmp, res)

            board[i][j] = tmp
            
        trie = Trie()
        res = []
        root = trie.root
        
        for word in words:
            trie.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, root, i, j, "", res)
        
        return res
        

```


### Related Problems
[Word Search](https://leetcode.com/problems/word-search/) (Medium) <br>
[Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) (Hard) <br>



### What a(n) Hard problem!
Among **730412** total submissions, **266454** are accepted, with an acceptance rate of **36.5%**. <br>

- Likes: 3294
- Dislikes: 140

