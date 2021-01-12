# [448] Find All Numbers Disappeared in an Array (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) 

:+1: 3685 &nbsp; &nbsp; :thumbsdown: 276

---

### My Solution


### Description
<p>Given an array of integers where 1 &le; a[i] &le; <i>n</i> (<i>n</i> = size of array), some elements appear twice and others appear once.</p>

<p>Find all the elements of [1, <i>n</i>] inclusive that do not appear in this array.</p>

<p>Could you do it without extra space and in O(<i>n</i>) runtime? You may assume the returned list does not count as extra space.</p>

<p><b>Example:</b>
<pre>
<b>Input:</b>
[4,3,2,7,8,2,3,1]

<b>Output:</b>
[5,6]
</pre>
</p>


### My Submission

- Language: Java
- Runtime: 13043 ms
- Completed time: 2019-02-04 14:56:01

```Java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != (i + 1)) {
                res.add(i + 1);
            }
        }

        for (int num : nums) {
            for (int i = 0; i < res.size(); i++) {
                if (num == res.get(i))
                    res.remove(i);
            }
        }

        return res;
    }
}
```


### Related Problems
[First Missing Positive](https://leetcode.com/problems/first-missing-positive/) (Hard) <br>
[Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) (Medium) <br>



### What a(n) Easy problem!
Among **586210** total submissions, **328963** are accepted, with an acceptance rate of **56.1%**. <br>

- Likes: 3685
- Dislikes: 276

