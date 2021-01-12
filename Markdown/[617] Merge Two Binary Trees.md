# [617] Merge Two Binary Trees (Easy)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/merge-two-binary-trees/) 

:+1: 3805 &nbsp; &nbsp; :thumbsdown: 187

---

### My Solution


### Description
<p>Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.</p>

<p>You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
<b>Output:</b> 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> The merging process must start from the root nodes of both trees.</p>



### My Submission

- Language: Java
- Runtime: 6 ms
- Completed time: 2019-02-03 15:33:27

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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 != null && t2 != null) {
            t1.val += t2.val;
            t1.left = mergeTrees(t1.left, t2.left);
            t1.right = mergeTrees(t1.right, t2.right);
            return t1;
        } else if (t1 != null) {
            return t1;
        } else {
            return t2;
        }
    }
    
}
```


### Related Problems




### What a(n) Easy problem!
Among **470929** total submissions, **353638** are accepted, with an acceptance rate of **75.1%**. <br>

- Likes: 3805
- Dislikes: 187

