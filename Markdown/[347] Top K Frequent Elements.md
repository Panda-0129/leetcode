# [347] Top K Frequent Elements (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/top-k-frequent-elements/)  [![Heap_badge](https://img.shields.io/badge/topic-Heap-green.svg)](https://leetcode.com/problems/top-k-frequent-elements/) 

:+1: 4269 &nbsp; &nbsp; :thumbsdown: 250

---

### My Solution


### Description
<p>Given a non-empty array of integers, return the <b><i>k</i></b> most frequent elements.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,1,1,2,2,3]</span>, k = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[1]</span>, k = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[1]</span></pre>
</div>

<p><b>Note: </b></p>

<ul>
	<li>You may assume <i>k</i> is always valid, 1 &le; <i>k</i> &le; number of unique elements.</li>
	<li>Your algorithm&#39;s time complexity <b>must be</b> better than O(<i>n</i> log <i>n</i>), where <i>n</i> is the array&#39;s size.</li>
	<li>It&#39;s guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.</li>
	<li>You can return the answer in any order.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 284 ms
- Completed time: 2019-03-24 22:10:00

```Python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            
        res = []            
        
        for i in range(0, k):
            res.append((max(dict, key=dict.get)))
            dict.pop(res[i])
        return res
```


### Related Problems
[Word Frequency](https://leetcode.com/problems/word-frequency/) (Medium) <br>
[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium) <br>
[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) (Medium) <br>
[Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) (Medium) <br>
[Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) (Medium) <br>
[K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (Medium) <br>



### What a(n) Medium problem!
Among **838052** total submissions, **521148** are accepted, with an acceptance rate of **62.2%**. <br>

- Likes: 4269
- Dislikes: 250

