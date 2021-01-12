# [813] All Paths From Source to Target (Medium)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/all-paths-from-source-to-target/)  [![Depth-first%20Search_badge](https://img.shields.io/badge/topic-Depth-first%20Search-green.svg)](https://leetcode.com/problems/all-paths-from-source-to-target/)  [![Graph_badge](https://img.shields.io/badge/topic-Graph-green.svg)](https://leetcode.com/problems/all-paths-from-source-to-target/) 

:+1: 1505 &nbsp; &nbsp; :thumbsdown: 82

---

### My Solution


### Description
<p>Given a directed&nbsp;acyclic graph (<strong>DAG</strong>) of <code>n</code> nodes labeled from 0 to n - 1,&nbsp;find all possible paths from node <code>0</code> to node <code>n - 1</code>, and return them in any order.</p>

<p>The graph is given as follows:&nbsp;<code>graph[i]</code> is a list of all nodes you can visit from node <code>i</code>&nbsp;(i.e., there is a directed edge from node <code>i</code> to node <code>graph[i][j]</code>).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> graph = [[1,2],[3],[3],[]]
<strong>Output:</strong> [[0,1,3],[0,2,3]]
<strong>Explanation:</strong> There are two paths: 0 -&gt; 1 -&gt; 3 and 0 -&gt; 2 -&gt; 3.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg" style="width: 423px; height: 301px;" />
<pre>
<strong>Input:</strong> graph = [[4,3,1],[3,2,4],[3],[4],[]]
<strong>Output:</strong> [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> graph = [[1],[]]
<strong>Output:</strong> [[0,1]]
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> graph = [[1,2,3],[2],[3],[]]
<strong>Output:</strong> [[0,1,2,3],[0,2,3],[0,3]]
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> graph = [[1,3],[2],[3],[]]
<strong>Output:</strong> [[0,1,2,3],[0,3]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>2 &lt;= n &lt;= 15</code></li>
	<li><code>0 &lt;= graph[i][j] &lt; n</code></li>
	<li><code>graph[i][j] != i</code> (i.e., there will be no self-loops).</li>
	<li>The input graph is <strong>guaranteed</strong> to be a <strong>DAG</strong>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 84 ms
- Completed time: 2019-09-18 15:20:42

```Python
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(graph, res, position, path):
            if position == len(graph) - 1:
                res.append(path)
                return

            else:
                for n in graph[position]:
                    dfs(graph, res, n, path + [n])

        res = []
        dfs(graph, res, 0, [0])

        return res
```


### Related Problems




### What a(n) Medium problem!
Among **141515** total submissions, **110901** are accepted, with an acceptance rate of **78.4%**. <br>

- Likes: 1505
- Dislikes: 82

