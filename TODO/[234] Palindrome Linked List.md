# [234] Palindrome Linked List (Easy)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/palindrome-linked-list/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/palindrome-linked-list/) 

:+1: 4783 &nbsp; &nbsp; :thumbsdown: 429

---

### My Solution


### Description
<p>Given the <code>head</code> of a singly linked list, return <code>true</code> if it is a palindrome.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2,2,1]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in <code>O(n)</code> time and <code>O(1)</code> space?


### My Submission

- Language: Python
- Runtime: 64 ms
- Completed time: 2019-09-06 12:57:39

```Python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        length = 0
        tmp, half = head, head
        stack = []
        
        while tmp:
            length+=1
            tmp = tmp.next
            
        halfLength = length / 2
        
        for i in range(halfLength):
            stack.append(half.val)
            half = half.next
        
        if length % 2 != 0:
            half = half.next
            
        while half:
            current = stack[halfLength - 1]
            if half.val != current:
                return False
            half = half.next
            halfLength-=1
        
        return True
```


### Related Problems
[Palindrome Number](https://leetcode.com/problems/palindrome-number/) (Easy) <br>
[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy) <br>
[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) <br>



### What a(n) Easy problem!
Among **1413096** total submissions, **574414** are accepted, with an acceptance rate of **40.6%**. <br>

- Likes: 4783
- Dislikes: 429

