# [140] Word Break II (Hard)

[![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/word-break-ii/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/word-break-ii/) 

:+1: 2775 &nbsp; &nbsp; :thumbsdown: 431

---

### My Solution


### Description
<p>Given a <strong>non-empty</strong> string <em>s</em> and a dictionary <em>wordDict</em> containing a list of <strong>non-empty</strong> words, add spaces in <em>s</em> to construct a sentence where each word is a valid dictionary word.&nbsp;Return all such possible sentences.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The same word in the dictionary may be reused multiple times in the segmentation.</li>
	<li>You may assume the dictionary does not contain duplicate words.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong>s = &quot;<code>catsanddog</code>&quot;
wordDict = <code>[&quot;cat&quot;, &quot;cats&quot;, &quot;and&quot;, &quot;sand&quot;, &quot;dog&quot;]</code>
<strong>Output:
</strong><code>[
&nbsp; &quot;cats and dog&quot;,
&nbsp; &quot;cat sand dog&quot;
]</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong>s = &quot;pineapplepenapple&quot;
wordDict = [&quot;apple&quot;, &quot;pen&quot;, &quot;applepen&quot;, &quot;pine&quot;, &quot;pineapple&quot;]
<strong>Output:
</strong>[
&nbsp; &quot;pine apple pen apple&quot;,
&nbsp; &quot;pineapple pen apple&quot;,
&nbsp; &quot;pine applepen apple&quot;
]
<strong>Explanation:</strong> Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:
</strong>s = &quot;catsandog&quot;
wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
<strong>Output:
</strong>[]</pre>



### My Submission

- Language: Python
- Runtime: 120 ms
- Completed time: 2019-11-12 10:08:12

```Python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def wordBreak(s, wordDict):
            dp = [0] * (len(s) + 1)
            dp[0] = 1
            for i in range(len(s) + 1):
                for j in range(i):
                    tmp_str = s[j:i]
                    if dp[j] and tmp_str in wordDict:
                        dp[i] = 1
                        break

            return dp

        def helper(current_s, res, path, dp, wordDict):
            if dp[-1] == 1:
                if not current_s:
                    res.append(path.strip())
                for i in range(1, len(current_s) + 1):
                    if current_s[:i] in wordDict:
                        helper(current_s[i:], res, path + " " + current_s[:i], dp, wordDict)

        if not s:
            return [""]
        res = []
        dp = wordBreak(s, wordDict)
        helper(s, res, "", dp, wordDict)

        return res        
```


### Related Problems
[Word Break](https://leetcode.com/problems/word-break/) (Medium) <br>
[Concatenated Words](https://leetcode.com/problems/concatenated-words/) (Hard) <br>



### What a(n) Hard problem!
Among **859351** total submissions, **294121** are accepted, with an acceptance rate of **34.2%**. <br>

- Likes: 2775
- Dislikes: 431

