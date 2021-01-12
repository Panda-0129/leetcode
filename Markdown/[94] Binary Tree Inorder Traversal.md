# [94] Binary Tree Inorder Traversal (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/binary-tree-inorder-traversal/)  [![Stack_badge](https://img.shields.io/badge/topic-Stack-green.svg)](https://leetcode.com/problems/binary-tree-inorder-traversal/)  [![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/binary-tree-inorder-traversal/) 

:+1: 4107 &nbsp; &nbsp; :thumbsdown: 181

---

### My Solution


### Description
<p>Given the <code>root</code> of a binary tree, return <em>the inorder traversal of its nodes&#39; values</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 324px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,3,2]
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
<strong>Output:</strong> [2,1]
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

<p><strong>Follow up:</strong></p>

<p>Recursive solution is trivial, could you do it iteratively?</p>

<p>&nbsp;</p>



### My Submission

- Language: Python
- Runtime: 32 ms
- Completed time: 2019-10-22 10:17:11

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(root, res):
            if root:
                traversal(root.left, res)
                res.append(root.val)
                traversal(root.right, res)
                
        res = []
        traversal(root, res)
        return res
```


### Related Problems
[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Medium) <br>
[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) (Medium) <br>
[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) (Medium) <br>
[Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) (Medium) <br>
[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (Medium) <br>
[Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) (Hard) <br>
[Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) (Medium) <br>
[Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) (Medium) <br>
[Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) (Easy) <br>



### What a(n) Medium problem!
Among **1353924** total submissions, **884965** are accepted, with an acceptance rate of **65.4%**. <br>

- Likes: 4107
- Dislikes: 181

