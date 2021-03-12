# [337] House Robber III (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/house-robber-iii/)  [![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/house-robber-iii/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/house-robber-iii/) 

:+1: 3821 &nbsp; &nbsp; :thumbsdown: 65

---

### My Solution


### Description
<p>The thief has found himself a new place for his thievery again. There is only one entrance to this area, called <code>root</code>.</p>

<p>Besides the <code>root</code>, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if <strong>two directly-linked houses were broken into on the same night</strong>.</p>

<p>Given the <code>root</code> of the binary tree, return <em>the maximum amount of money the thief can rob <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg" style="width: 277px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [3,2,3,null,3,null,1]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg" style="width: 357px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,3,null,1]
<strong>Output:</strong> 9
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 4 + 5 = 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 56 ms
- Completed time: 2020-09-22 15:39:49

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def help(root):
            if root == None:
                return [0] * 2
            
            left = help(root.left)
            right = help(root.right)
            
            res = [0] * 2
            
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = root.val + left[0] + right[0]
            
            return res
        
        res = help(root)
        
        return max(res)
        
        
```


### Related Problems
[House Robber](https://leetcode.com/problems/house-robber/) (Medium) <br>
[House Robber II](https://leetcode.com/problems/house-robber-ii/) (Medium) <br>



### What a(n) Medium problem!
Among **392394** total submissions, **203794** are accepted, with an acceptance rate of **51.9%**. <br>

- Likes: 3821
- Dislikes: 65

