# [174] Dungeon Game (Hard)

[![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/dungeon-game/)  [![Dynamic%20Programming_badge](https://img.shields.io/badge/topic-Dynamic%20Programming-green.svg)](https://leetcode.com/problems/dungeon-game/) 

:+1: 2103 &nbsp; &nbsp; :thumbsdown: 46

---

### My Solution


### Description
<style type="text/css">table.dungeon, .dungeon th, .dungeon td {
  border:3px solid black;
}

 .dungeon th, .dungeon td {
    text-align: center;
    height: 70px;
    width: 70px;
}
</style>
<p>The demons had captured the princess (<strong>P</strong>) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (<strong>K</strong>) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.</p>

<p>The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.</p>

<p>Some of the rooms are guarded by demons, so the knight loses health (<em>negative</em> integers) upon entering these rooms; other rooms are either empty (<em>0&#39;s</em>) or contain magic orbs that increase the knight&#39;s health (<em>positive</em> integers).</p>

<p>In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.</p>

<p>&nbsp;</p>

<p><strong>Write a function to determine the knight&#39;s minimum initial health so that he is able to rescue the princess.</strong></p>

<p>For example, given the dungeon below, the initial health of the knight must be at least <strong>7</strong> if he follows the optimal path <code>RIGHT-&gt; RIGHT -&gt; DOWN -&gt; DOWN</code>.</p>

<table class="dungeon">
	<tbody>
		<tr>
			<td>-2 (K)</td>
			<td>-3</td>
			<td>3</td>
		</tr>
		<tr>
			<td>-5</td>
			<td>-10</td>
			<td>1</td>
		</tr>
		<tr>
			<td>10</td>
			<td>30</td>
			<td>-5 (P)</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The knight&#39;s health has no upper bound.</li>
	<li>Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 72 ms
- Completed time: 2020-11-17 10:25:58

```Python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        len_row = len(dungeon)
        len_col = len(dungeon[0])

        for row in range(len_row - 1, -1, -1):
            for col in range(len_col - 1, -1, -1):
                if row == len_row - 1 and col == len_col - 1:
                    dungeon[row][col] = min(0, dungeon[row][col])
                elif row == len_row - 1:
                    dungeon[row][col] = min(0, dungeon[row][col + 1] + dungeon[row][col])
                elif col == len_col - 1:
                    dungeon[row][col] = min(0, dungeon[row + 1][col] + dungeon[row][col])
                else:
                    dungeon[row][col] = min(0, dungeon[row][col] + max(dungeon[row + 1][col], dungeon[row][col + 1]))

        return -dungeon[0][0] + 1
```


### Related Problems
[Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium) <br>
[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) (Medium) <br>
[Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) (Hard) <br>



### What a(n) Hard problem!
Among **360929** total submissions, **119592** are accepted, with an acceptance rate of **33.1%**. <br>

- Likes: 2103
- Dislikes: 46

