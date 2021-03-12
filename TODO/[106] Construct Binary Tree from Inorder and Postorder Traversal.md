# [106] Construct Binary Tree from Inorder and Postorder Traversal (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)  [![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) 

:+1: 2493 &nbsp; &nbsp; :thumbsdown: 49

---

### My Solution


### Description
<p>Given two integer arrays <code>inorder</code> and <code>postorder</code> where <code>inorder</code> is the inorder traversal of a binary tree and <code>postorder</code> is the postorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> inorder = [-1], postorder = [-1]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= inorder.length &lt;= 3000</code></li>
	<li><code>postorder.length == inorder.length</code></li>
	<li><code>-3000 &lt;= inorder[i], postorder[i] &lt;= 3000</code></li>
	<li><code>inorder</code> and <code>postorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>postorder</code> also appears in <code>inorder</code>.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
	<li><code>postorder</code> is <strong>guaranteed</strong> to be the postorder traversal of the tree.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 364 ms
- Completed time: 2019-10-21 10:32:42

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def restoreTree(inorder, in_start, in_end, postorder, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None
            
            treeNode = TreeNode(postorder[post_end])
            
            for i in range(in_end + 1):
                if inorder[i] == postorder[post_end]:
                    treeNode.left = restoreTree(inorder, in_start, i - 1, postorder, post_start, post_start + i - in_start - 1)
                    treeNode.right = restoreTree(inorder, i + 1, in_end, postorder, post_start + i - in_start, post_end - 1)

            return treeNode

        tree = restoreTree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

        return tree
```


### Related Problems
[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (Medium) <br>



### What a(n) Medium problem!
Among **572707** total submissions, **285298** are accepted, with an acceptance rate of **49.8%**. <br>

- Likes: 2493
- Dislikes: 49

