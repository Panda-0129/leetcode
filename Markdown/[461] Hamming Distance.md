# [461] Hamming Distance (Easy)

[![Bit%20Manipulation_badge](https://img.shields.io/badge/topic-Bit%20Manipulation-green.svg)](https://leetcode.com/problems/hamming-distance/) 

:+1: 2060 &nbsp; &nbsp; :thumbsdown: 174

---

### My Solution


### Description
<p>The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.</p>

<p>Given two integers <code>x</code> and <code>y</code>, calculate the Hamming distance.</p>

<p><b>Note:</b><br />
0 &le; <code>x</code>, <code>y</code> &lt; 2<sup>31</sup>.
</p>

<p><b>Example:</b>
<pre>
<b>Input:</b> x = 1, y = 4

<b>Output:</b> 2

<b>Explanation:</b>
1   (0 0 0 1)
4   (0 1 0 0)
       &uarr;   &uarr;

The above arrows point to positions where the corresponding bits are different.
</pre>
</p>


### My Submission

- Language: Java
- Runtime: 8 ms
- Completed time: 2019-02-04 14:16:05

```Java
class Solution {
    public int hammingDistance(int x, int y) {
        return getNum(Integer.toBinaryString(x^y));
    }

    int getNum (String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1')
                count++;
        }
        return count;
    }
}
```


### Related Problems
[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) (Easy) <br>
[Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/) (Medium) <br>



### What a(n) Easy problem!
Among **518516** total submissions, **379046** are accepted, with an acceptance rate of **73.1%**. <br>

- Likes: 2060
- Dislikes: 174

