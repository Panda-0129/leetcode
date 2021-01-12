# [581] Shortest Unsorted Continuous Subarray (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) 

:+1: 3343 &nbsp; &nbsp; :thumbsdown: 162

---

### My Solution


### Description
<p>Given an integer array <code>nums</code>, you need to find one <b>continuous subarray</b> that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.</p>

<p>Return&nbsp;<em>the shortest such subarray and output its length</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,6,4,8,10,9,15]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>



### My Submission

- Language: Java
- Runtime: 22 ms
- Completed time: 2019-02-03 16:18:27

```Java
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int[] tmp = Arrays.copyOf(nums, nums.length);
        Arrays.sort(tmp);
        int startPos = 0, endPos = 0;
        if (Arrays.equals(nums, tmp)) {
            return 0;
        } else {
            int i = 0;
            for (; i < nums.length; i++) {
                if (tmp[i] != nums[i]) {
                    startPos = i;
                    break;
                }
            }
            for (; i < nums.length; i++) {
                if (tmp[i] != nums[i]) {
                    endPos = i;
                }
            }
            return Arrays.copyOfRange(nums, startPos, endPos + 1).length;
        }
    }
}
```


### Related Problems




### What a(n) Medium problem!
Among **469159** total submissions, **148359** are accepted, with an acceptance rate of **31.6%**. <br>

- Likes: 3343
- Dislikes: 162

