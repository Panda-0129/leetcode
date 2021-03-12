# [21] Merge Two Sorted Lists (Easy)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/merge-two-sorted-lists/)  [![Recursion_badge](https://img.shields.io/badge/topic-Recursion-green.svg)](https://leetcode.com/problems/merge-two-sorted-lists/) 

:+1: 6269 &nbsp; &nbsp; :thumbsdown: 737

---

### My Solution


### Description
<p>Merge two sorted linked lists and return it as a <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>Input:</strong> l1 = [1,2,4], l2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [], l2 = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both lists is in the range <code>[0, 50]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>Both <code>l1</code> and <code>l2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 36 ms
- Completed time: 2021-03-08 20:40:58

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = cur = ListNode()
        res.next = cur
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        cur.next = l1 or l2

        return res.next
```


### Related Problems
[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) <br>
[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy) <br>
[Sort List](https://leetcode.com/problems/sort-list/) (Medium) <br>
[Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii/) (Medium) <br>
[Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/) (Medium) <br>



### What a(n) Easy problem!
Among **2394505** total submissions, **1344909** are accepted, with an acceptance rate of **56.2%**. <br>

- Likes: 6269
- Dislikes: 737

