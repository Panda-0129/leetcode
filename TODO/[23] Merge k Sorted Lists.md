# [23] Merge k Sorted Lists (Hard)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/merge-k-sorted-lists/)  [![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/merge-k-sorted-lists/)  [![Heap_badge](https://img.shields.io/badge/topic-Heap-green.svg)](https://leetcode.com/problems/merge-k-sorted-lists/) 

:+1: 6719 &nbsp; &nbsp; :thumbsdown: 347

---

### My Solution


### Description
<p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>

<p><em>Merge all the linked-lists into one sorted linked-list and return it.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10^4</code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10^4 &lt;= lists[i][j] &lt;= 10^4</code></li>
	<li><code>lists[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>The sum of <code>lists[i].length</code> won&#39;t exceed <code>10^4</code>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 92 ms
- Completed time: 2021-03-09 12:59:48

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heappop
        res = head = ListNode(0)
        q = []
        for list_id, list_node in enumerate(lists):
            if list_node:
                heappush(q, (list_node.val, list_id, list_node))
        
        while q:
            cur_val, cur_id, head.next = heappop(q)
            
            head = head.next
            if head.next:
                heappush(q, (head.next.val, cur_id, head.next))
        
        return res.next
        
        
```


### Related Problems
[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) <br>
[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) (Medium) <br>



### What a(n) Hard problem!
Among **1959434** total submissions, **838523** are accepted, with an acceptance rate of **42.8%**. <br>

- Likes: 6719
- Dislikes: 347

