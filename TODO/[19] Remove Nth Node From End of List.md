# [19] Remove Nth Node From End of List (Medium)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) 

:+1: 4881 &nbsp; &nbsp; :thumbsdown: 290

---

### My Solution


### Description
<p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p><strong>Follow up:</strong>&nbsp;Could you do this in one pass?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>sz</code>.</li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>



### My Submission

- Language: Python
- Runtime: 32 ms
- Completed time: 2019-12-13 15:23:19

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def reverseList(head):
            if head is None or head.next is None:
                return head;
            pre = None;
            cur = head;
            h = head;
            while cur:
                h = cur;
                tmp = cur.next;
                cur.next = pre;
                pre = cur;
                cur = tmp;
            return h
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        if n == 1:
            return reverseList(reverseList(head).next)
        if length == n:
            return head.next
        head = reverseList(head)
        count = 1
        tmp = head
        while count != n - 1:
            count += 1
            tmp = tmp.next
        tmp.next = tmp.next.next

        return reverseList(head)
```


### Related Problems
[Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) (Medium) <br>
[Delete N Nodes After M Nodes of a Linked List](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) (Easy) <br>



### What a(n) Medium problem!
Among **2263743** total submissions, **809704** are accepted, with an acceptance rate of **35.8%**. <br>

- Likes: 4881
- Dislikes: 290

