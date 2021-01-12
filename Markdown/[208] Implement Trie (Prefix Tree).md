# [208] Implement Trie (Prefix Tree) (Medium)

[![Design_badge](https://img.shields.io/badge/topic-Design-green.svg)](https://leetcode.com/problems/implement-trie-prefix-tree/)  [![Trie_badge](https://img.shields.io/badge/topic-Trie-green.svg)](https://leetcode.com/problems/implement-trie-prefix-tree/) 

:+1: 4078 &nbsp; &nbsp; :thumbsdown: 64

---

### My Solution


### Description
<p>Implement a trie with <code>insert</code>, <code>search</code>, and <code>startsWith</code> methods.</p>

<p><b>Example:</b></p>

<pre>
Trie trie = new Trie();

trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // returns true
trie.search(&quot;app&quot;);     // returns false
trie.startsWith(&quot;app&quot;); // returns true
trie.insert(&quot;app&quot;);   
trie.search(&quot;app&quot;);     // returns true
</pre>

<p><b>Note:</b></p>

<ul>
	<li>You may assume that all inputs are consist of lowercase letters <code>a-z</code>.</li>
	<li>All inputs are guaranteed to be non-empty strings.</li>
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
Among **737169** total submissions, **379589** are accepted, with an acceptance rate of **51.5%**. <br>

- Likes: 4078
- Dislikes: 64

