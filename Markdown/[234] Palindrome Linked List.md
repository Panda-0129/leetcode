# [234] Palindrome Linked List (Easy)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/palindrome-linked-list/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/palindrome-linked-list/) 

:+1: 4421 &nbsp; &nbsp; :thumbsdown: 409

---

### My Solution


### Description
<p>Given a singly linked list, determine if it is a palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2
<strong>Output:</strong> false</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;2-&gt;1
<strong>Output:</strong> true</pre>

<p><b>Follow up:</b><br />
Could you do it in O(n) time and O(1) space?</p>



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
Among **1330580** total submissions, **534893** are accepted, with an acceptance rate of **40.2%**. <br>

- Likes: 4421
- Dislikes: 409

