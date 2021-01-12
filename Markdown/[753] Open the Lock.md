# [753] Open the Lock (Medium)

[![Breadth-first%20Search_badge](https://img.shields.io/badge/topic-Breadth-first%20Search-green.svg)](https://leetcode.com/problems/open-the-lock/) 

:+1: 1378 &nbsp; &nbsp; :thumbsdown: 53

---

### My Solution


### Description
<p>You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: <code>&#39;0&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;, &#39;9&#39;</code>. The wheels can rotate freely and wrap around: for example we can turn <code>&#39;9&#39;</code> to be <code>&#39;0&#39;</code>, or <code>&#39;0&#39;</code> to be <code>&#39;9&#39;</code>. Each move consists of turning one wheel one slot.</p>

<p>The lock initially starts at <code>&#39;0000&#39;</code>, a string representing the state of the 4 wheels.</p>

<p>You are given a list of <code>deadends</code> dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.</p>

<p>Given a <code>target</code> representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> deadends = [&quot;0201&quot;,&quot;0101&quot;,&quot;0102&quot;,&quot;1212&quot;,&quot;2002&quot;], target = &quot;0202&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong>
A sequence of valid moves would be &quot;0000&quot; -&gt; &quot;1000&quot; -&gt; &quot;1100&quot; -&gt; &quot;1200&quot; -&gt; &quot;1201&quot; -&gt; &quot;1202&quot; -&gt; &quot;0202&quot;.
Note that a sequence like &quot;0000&quot; -&gt; &quot;0001&quot; -&gt; &quot;0002&quot; -&gt; &quot;0102&quot; -&gt; &quot;0202&quot; would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end &quot;0102&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> deadends = [&quot;8888&quot;], target = &quot;0009&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong>
We can turn the last wheel in reverse to move from &quot;0000&quot; -&gt; &quot;0009&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> deadends = [&quot;8887&quot;,&quot;8889&quot;,&quot;8878&quot;,&quot;8898&quot;,&quot;8788&quot;,&quot;8988&quot;,&quot;7888&quot;,&quot;9888&quot;], target = &quot;8888&quot;
<strong>Output:</strong> -1
Explanation:
We can&#39;t reach the target without getting stuck.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> deadends = [&quot;0000&quot;], target = &quot;8888&quot;
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;deadends.length &lt;= 500</code></li>
	<li><code><font face="monospace">deadends[i].length == 4</font></code></li>
	<li><code><font face="monospace">target.length == 4</font></code></li>
	<li>target <strong>will not be</strong> in the list <code>deadends</code>.</li>
	<li><code>target</code> and <code>deadends[i]</code> consist of digits only.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 2928 ms
- Completed time: 2020-09-15 21:39:01

```Python
import queue

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def plus(s, j):
            s = list(s)
            if s[j] == '9':
                s[j] = '0'
            else:
                s[j] = chr(ord(s[j]) + 1)
            
            return ''.join(s)
        
        def minus(s, j):
            s = list(s)
            if s[j] == '0':
                s[j] = '9'
            else:
                s[j] = chr(ord(s[j]) - 1)
            
            return ''.join(s)
        
        q = queue.Queue()
        visited = set()
        step = 0
        q.put('0000')
        visited.add('0000')
        
        while q.qsize() != 0:
            length = q.qsize()
            
            for i in range(length):
                cur = q.get()
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                
                for j in range(4):
                    up = plus(cur, j)
                    if up not in visited:
                        q.put(up)
                        visited.add(up)
                    
                    down = minus(cur, j)
                    if down not in visited:
                        q.put(down)
                        visited.add(down)
                    
            step += 1
                
        return -1
        
```


### Related Problems




### What a(n) Medium problem!
Among **157911** total submissions, **82968** are accepted, with an acceptance rate of **52.5%**. <br>

- Likes: 1378
- Dislikes: 53

