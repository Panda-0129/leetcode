# [412] Fizz Buzz (Easy)



:+1: 1156 &nbsp; &nbsp; :thumbsdown: 1438

---

### My Solution


### Description
<p>Write a program that outputs the string representation of numbers from 1 to <i>n</i>.</p>

<p>But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.</p>

<p><b>Example:</b>
<pre>
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
</pre>
</p>


### My Submission

- Language: Python
- Runtime: 40 ms
- Completed time: 2019-04-03 21:44:05

```Python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        i = 1
        while i <= n:
            if i%3 == 0 and i%5 == 0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
            i+=1  
        return res
```


### Related Problems
[Fizz Buzz Multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded/) (Medium) <br>



### What a(n) Easy problem!
Among **668046** total submissions, **424111** are accepted, with an acceptance rate of **63.5%**. <br>

- Likes: 1156
- Dislikes: 1438

