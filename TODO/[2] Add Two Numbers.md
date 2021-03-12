# [2] Add Two Numbers (Medium)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/add-two-numbers/)  [![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/add-two-numbers/)  [![Recursion_badge](https://img.shields.io/badge/topic-Recursion-green.svg)](https://leetcode.com/problems/add-two-numbers/) 

:+1: 11070 &nbsp; &nbsp; :thumbsdown: 2655

---

### My Solution


### Description
<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 80 ms
- Completed time: 2019-10-17 09:35:12

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = point = ListNode(0)
        extra = 0
        
        while l1 != None or l2 != None:
            l1_ele = l1.val if l1 != None else 0
            l2_ele = l2.val if l2 != None else 0
            sum = l1_ele + l2_ele + extra
            extra = 1 if sum >= 10 else 0
            point.next = ListNode(int(sum%10))
            point = point.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        
        if extra == 1:
            point.next = ListNode(1)
        
        return res.next
```


### Related Problems
[Multiply Strings](https://leetcode.com/problems/multiply-strings/) (Medium) <br>
[Add Binary](https://leetcode.com/problems/add-binary/) (Easy) <br>
[Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) (Medium) <br>
[Add Strings](https://leetcode.com/problems/add-strings/) (Easy) <br>
[Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) (Medium) <br>
[Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) (Easy) <br>
[Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/) (Medium) <br>



### What a(n) Medium problem!
Among **5141900** total submissions, **1827270** are accepted, with an acceptance rate of **35.5%**. <br>

- Likes: 11070
- Dislikes: 2655

