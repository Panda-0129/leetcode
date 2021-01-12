# [106] Construct Binary Tree from Inorder and Postorder Traversal (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)  [![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) 

:+1: 2338 &nbsp; &nbsp; :thumbsdown: 43

---

### My Solution


### Description
<p>Given inorder and postorder traversal of a tree, construct the binary tree.</p>

<p><strong>Note:</strong><br />
You may assume that duplicates do not exist in the tree.</p>

<p>For example, given</p>

<pre>
inorder =&nbsp;[9,3,15,20,7]
postorder = [9,15,7,20,3]</pre>

<p>Return the following binary tree:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7
</pre>



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
Among **557727** total submissions, **273907** are accepted, with an acceptance rate of **49.1%**. <br>

- Likes: 2338
- Dislikes: 43

