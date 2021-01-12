# [337] House Robber III (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/house-robber-iii/)  [![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/house-robber-iii/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/house-robber-iii/) 

:+1: 3620 &nbsp; &nbsp; :thumbsdown: 63

---

### My Solution


### Description
<p>The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the &quot;root.&quot; Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that &quot;all houses in this place forms a binary tree&quot;. It will automatically contact the police if two directly-linked houses were broken into on the same night.</p>

<p>Determine the maximum amount of money the thief can rob tonight without alerting the police.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong>[3,2,3,null,3,null,1]

     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1
</font>
<strong>Output:</strong> 7 
<strong>Explanation:</strong>&nbsp;Maximum amount of money the thief can rob = <font color="red" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">3</font><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> + </span><font color="red" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">3</font><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> + </span><font color="red" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">1</font><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> = </span><b style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">7</b><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong>[3,4,5,1,3,null,1]

&nbsp;    3
    / \
   <font color="red">4</font>   <font color="red">5</font>
  / \   \ 
 1   3   1

<strong>Output:</strong> 9
<strong>Explanation:</strong>&nbsp;Maximum amount of money the thief can rob = <font color="red">4</font> + <font color="red">5</font> = <b>9</b>.
</pre>


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
Among **379755** total submissions, **196281** are accepted, with an acceptance rate of **51.7%**. <br>

- Likes: 3620
- Dislikes: 63

