# [513] Find Bottom Left Tree Value (Medium)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/find-bottom-left-tree-value/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/find-bottom-left-tree-value/)  [![Breadth-first%20Search_badge](https://img.shields.io/badge/topic-Breadth-first%20Search-green.svg)](https://leetcode.com/problems/find-bottom-left-tree-value/) 

:+1: 1270 &nbsp; &nbsp; :thumbsdown: 169

---

### My Solution


### Description
<p>Given the <code>root</code> of a binary tree, return the leftmost value in the last row of the tree.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg" style="width: 432px; height: 421px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,null,5,6,null,null,7]
<strong>Output:</strong> 7
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 44 ms
- Completed time: 2019-09-16 09:27:00

```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.currentMaxVal = root.val
        self.currentMaxDepth = 0
        
        def helper(root, depth):
            if not root:
                return 0
            
            if depth > self.currentMaxDepth:
                self.currentMaxVal = root.val
                self.currentMaxDepth = depth
            
            if root.left:
                helper(root.left, depth + 1)
            
            if root.right:
                helper(root.right, depth + 1)
        
        helper(root, 1)
        
        return self.currentMaxVal
                
                
```


### Related Problems




### What a(n) Medium problem!
Among **200607** total submissions, **125718** are accepted, with an acceptance rate of **62.7%**. <br>

- Likes: 1270
- Dislikes: 169

