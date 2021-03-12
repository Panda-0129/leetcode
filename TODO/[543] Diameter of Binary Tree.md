# [543] Diameter of Binary Tree (Easy)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/diameter-of-binary-tree/) 

:+1: 4371 &nbsp; &nbsp; :thumbsdown: 275

---

### My Solution


### Description
<p>Given the <code>root</code> of a binary tree, return <em>the length of the <strong>diameter</strong> of the tree</em>.</p>

<p>The <strong>diameter</strong> of a binary tree is the <strong>length</strong> of the longest path between any two nodes in a tree. This path may or may not pass through the <code>root</code>.</p>

<p>The <strong>length</strong> of a path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>



### My Submission

- Language: Java
- Runtime: 4 ms
- Completed time: 2019-02-03 17:12:11

```Java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int dis = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        getHeight(root);
        return dis;
    }
    
    int getHeight (TreeNode root) {
         if (root == null) 
            return 0;
        int lHeight = getHeight(root.left);
        int rHeight = getHeight(root.right);
        dis = Math.max(dis, lHeight + rHeight);
        if (lHeight > rHeight)
                return lHeight + 1;
             else
                return rHeight + 1;
    }
    
}
```


### Related Problems
[Diameter of N-Ary Tree](https://leetcode.com/problems/diameter-of-n-ary-tree/) (Medium) <br>



### What a(n) Easy problem!
Among **908015** total submissions, **446841** are accepted, with an acceptance rate of **49.2%**. <br>

- Likes: 4371
- Dislikes: 275

