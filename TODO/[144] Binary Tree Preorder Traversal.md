# [144] Binary Tree Preorder Traversal (Medium)

[![Stack_badge](https://img.shields.io/badge/topic-Stack-green.svg)](https://leetcode.com/problems/binary-tree-preorder-traversal/)  [![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/binary-tree-preorder-traversal/) 

:+1: 2113 &nbsp; &nbsp; :thumbsdown: 86

---

### My Solution


### Description
<p>Given the <code>root</code> of a binary tree, return <em>the preorder traversal of its nodes&#39; values</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 324px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p><strong>Example 4:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg" style="width: 202px; height: 202px;" />
<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p><strong>Example 5:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg" style="width: 202px; height: 202px;" />
<pre>
<strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-10-11 14:51:37

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        current_node = root
        stack = []
        res = []
        while current_node != None or len(stack) != 0:
            if current_node != None:
                stack.append(current_node)
                res.append(current_node.val)
                current_node = current_node.left
            else:
                current_node = stack.pop().right
        return res
```


### Related Problems
[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (Medium) <br>
[Verify Preorder Sequence in Binary Search Tree](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/) (Medium) <br>
[N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) (Easy) <br>



### What a(n) Medium problem!
Among **1054136** total submissions, **607176** are accepted, with an acceptance rate of **57.6%**. <br>

- Likes: 2113
- Dislikes: 86

