# [687] Longest Univalue Path (Medium)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/longest-univalue-path/)  [![Recursion_badge](https://img.shields.io/badge/topic-Recursion-green.svg)](https://leetcode.com/problems/longest-univalue-path/) 

:+1: 2192 &nbsp; &nbsp; :thumbsdown: 547

---

### My Solution


### Description
<p>Given the <code>root</code> of a binary tree, return <em>the length of the longest path, where each node in the path has the same value</em>. This path may or may not pass through the root.</p>

<p><strong>The length of the path</strong> between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg" style="width: 571px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [5,4,5,1,1,5]
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg" style="width: 571px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,4,5,4,4,5]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li>The depth of the tree will not exceed <code>1000</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 412 ms
- Completed time: 2019-09-05 12:23:49

```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def traversePath(root, rootValue):
            if not root:
                return 0;
            left, right = traversePath(root.left, root.val), traversePath(root.right, root.val)
            self.res = max(self.res, left + right)

            return 1 + max(left, right) if root.val == rootValue else 0
        
        traversePath(root, None)
        
        return self.res
    
```


### Related Problems
[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (Hard) <br>
[Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/) (Medium) <br>
[Path Sum III](https://leetcode.com/problems/path-sum-iii/) (Medium) <br>



### What a(n) Medium problem!
Among **295575** total submissions, **110304** are accepted, with an acceptance rate of **37.3%**. <br>

- Likes: 2192
- Dislikes: 547

