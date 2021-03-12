# [93] Restore IP Addresses (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/restore-ip-addresses/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/restore-ip-addresses/) 

:+1: 1682 &nbsp; &nbsp; :thumbsdown: 553

---

### My Solution


### Description
<p>Given a string <code>s</code> containing only digits, return all possible valid IP addresses that can be obtained from <code>s</code>. You can return them in <strong>any</strong> order.</p>

<p>A <strong>valid IP address</strong> consists of exactly four integers, each integer is between <code>0</code> and <code>255</code>, separated by single dots and cannot have leading zeros. For example, &quot;0.1.2.201&quot; and &quot;192.168.1.1&quot; are <strong>valid</strong> IP addresses and &quot;0.011.255.245&quot;, &quot;192.168.1.312&quot; and &quot;192.168@1.1&quot; are <strong>invalid</strong> IP addresses.&nbsp;</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "25525511135"
<strong>Output:</strong> ["255.255.11.135","255.255.111.35"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "0000"
<strong>Output:</strong> ["0.0.0.0"]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "1111"
<strong>Output:</strong> ["1.1.1.1"]
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> s = "010010"
<strong>Output:</strong> ["0.10.0.10","0.100.1.0"]
</pre><p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> s = "101023"
<strong>Output:</strong> ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code> consists of digits only.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 332 ms
- Completed time: 2020-10-16 10:50:42

```Python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def dfs(s, idx, path, res):
            if idx > 4:
                return
            if idx == 4 and not s:
                res.append(path[:-1])
                return
            
            for i in range(1, len(s) + 1):
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                    dfs(s[i:], idx + 1, path + s[:i] + ".", res)
            
        res = []
        
        dfs(s, 0, "", res)
        
        return res
```


### Related Problems
[IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) (Medium) <br>



### What a(n) Medium problem!
Among **605355** total submissions, **227990** are accepted, with an acceptance rate of **37.7%**. <br>

- Likes: 1682
- Dislikes: 553

