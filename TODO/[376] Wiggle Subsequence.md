# [376] Wiggle Subsequence (Medium)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/wiggle-subsequence/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/wiggle-subsequence/) 

:+1: 1331 &nbsp; &nbsp; :thumbsdown: 67

---

### My Solution


### Description
<p>A sequence of numbers is called a <strong>wiggle sequence</strong> if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.</p>

<p>For example, <code>[1,7,4,9,2,5]</code> is a wiggle sequence because the differences <code>(6,-3,5,-7,3)</code> are alternately positive and negative. In contrast, <code>[1,4,7,2,5]</code> and <code>[1,7,4,5,5]</code> are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.</p>

<p>Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,7,4,9,2,5]</span>
<strong>Output: </strong><span id="example-output-1">6
<strong>Explanation:</strong> </span>The entire sequence is a wiggle sequence.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,17,5,10,13,15,10,5,16,8]</span>
<strong>Output: </strong><span id="example-output-2">7
</span><span id="example-output-1"><strong>Explanation: </strong></span>There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2,3,4,5,6,7,8,9]</span>
<strong>Output: </strong><span id="example-output-3">2</span></pre>

<p><b>Follow up:</b><br />
Can you do it in O(<i>n</i>) time?</p>
</div>
</div>



### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-10-23 09:40:40

```Python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i -1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1

        return min(len(nums), max(up, down))        
```


### Related Problems




### What a(n) Medium problem!
Among **204272** total submissions, **82222** are accepted, with an acceptance rate of **40.3%**. <br>

- Likes: 1331
- Dislikes: 67
