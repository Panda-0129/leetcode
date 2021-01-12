# [445] Add Two Numbers II (Medium)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/add-two-numbers-ii/) 

:+1: 2056 &nbsp; &nbsp; :thumbsdown: 190

---

### My Solution


### Description
<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><b>Follow up:</b><br />
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
</p>

<p>
<b>Example:</b>
<pre>
<b>Input:</b> (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
<b>Output:</b> 7 -> 8 -> 0 -> 7
</pre>
</p>


### My Submission

- Language: Python
- Runtime: 84 ms
- Completed time: 2019-10-18 14:20:29

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_node(l):
            if not l or not l.next:
                return l
            pre = None
            while l:
                tmp = l.next
                l.next = pre
                pre = l
                l = tmp
            return pre
        res = point = ListNode(0)
        extra = 0
        l1 = reverse_node(l1)
        l2 = reverse_node(l2)

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

        return reverse_node(res.next) 
```


### Related Problems
[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (Medium) <br>
[Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/) (Medium) <br>



### What a(n) Medium problem!
Among **381111** total submissions, **213414** are accepted, with an acceptance rate of **56.0%**. <br>

- Likes: 2056
- Dislikes: 190

