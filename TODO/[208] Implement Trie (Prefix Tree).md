# [208] Implement Trie (Prefix Tree) (Medium)

[![Design_badge](https://img.shields.io/badge/topic-Design-green.svg)](https://leetcode.com/problems/implement-trie-prefix-tree/)  [![Trie_badge](https://img.shields.io/badge/topic-Trie-green.svg)](https://leetcode.com/problems/implement-trie-prefix-tree/) 

:+1: 4282 &nbsp; &nbsp; :thumbsdown: 67

---

### My Solution


### Description
<p>Trie (we pronounce &quot;try&quot;) or prefix tree is a tree data structure used to retrieve a key in a strings dataset. There are various applications of this very efficient data structure, such as autocomplete and spellchecker.</p>

<p>Implement the Trie class:</p>

<ul>
	<li><code>Trie()</code> initializes the trie object.</li>
	<li><code>void insert(String word)</code> inserts the string <code>word</code> to the trie.</li>
	<li><code>boolean search(String word)</code> returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
	<li><code>boolean startsWith(String prefix)</code> returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Trie&quot;, &quot;insert&quot;, &quot;search&quot;, &quot;search&quot;, &quot;startsWith&quot;, &quot;insert&quot;, &quot;search&quot;]
[[], [&quot;apple&quot;], [&quot;apple&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;]]
<strong>Output</strong>
[null, null, true, false, true, null, true]

<strong>Explanation</strong>
Trie trie = new Trie();
trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // return True
trie.search(&quot;app&quot;);     // return False
trie.startsWith(&quot;app&quot;); // return True
trie.insert(&quot;app&quot;);
trie.search(&quot;app&quot;);     // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> and <code>prefix</code> consist of lowercase English letters.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>insert</code>, <code>search</code>, and <code>startsWith</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 168 ms
- Completed time: 2020-10-13 10:18:54

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
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```


### Related Problems
[Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) (Medium) <br>
[Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) (Hard) <br>
[Replace Words](https://leetcode.com/problems/replace-words/) (Medium) <br>
[Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) (Medium) <br>



### What a(n) Medium problem!
Among **760449** total submissions, **397160** are accepted, with an acceptance rate of **52.2%**. <br>

- Likes: 4282
- Dislikes: 67

