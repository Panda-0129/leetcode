# [543] Diameter of Binary Tree (Easy)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/diameter-of-binary-tree/) 

:+1: 4075 &nbsp; &nbsp; :thumbsdown: 243

---

### My Solution


### Description
<p>
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the <b>longest</b> path between any two nodes in a tree. This path may or may not pass through the root.
</p>

<p>
<b>Example:</b><br />
Given a binary tree <br />
<pre>
          1
         / \
        2   3
       / \     
      4   5    
</pre>
</p>
<p>
Return <b>3</b>, which is the length of the path [4,2,1,3] or [5,2,1,3].
</p>

<p><b>Note:</b>
The length of path between two nodes is represented by the number of edges between them.
</p>


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
Among **857513** total submissions, **420471** are accepted, with an acceptance rate of **49.0%**. <br>

- Likes: 4075
- Dislikes: 243

