# [525] Contiguous Array (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/contiguous-array/) 

:+1: 2581 &nbsp; &nbsp; :thumbsdown: 134

---

### My Solution


### Description
<p>Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. </p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [0,1]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [0,1,0]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Note:</b>
The length of the given binary array will not exceed 50,000.
</p>


### My Submission

- Language: Python
- Runtime: 808 ms
- Completed time: 2019-09-20 20:16:10

```Python
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0
        
        count = 0
        count_dict = {0: 0}
        max_length = 0
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 0:
                count += 1
            else:
                count -= 1
            if count in count_dict:
                max_length = max(max_length, i - count_dict[count])
            else:
                count_dict[count] = i
        
        return max_length
```


### Related Problems
[Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) (Medium) <br>



### What a(n) Medium problem!
Among **411158** total submissions, **178289** are accepted, with an acceptance rate of **43.4%**. <br>

- Likes: 2581
- Dislikes: 134

