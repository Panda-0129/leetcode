# [599] Minimum Index Sum of Two Lists (Easy)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) 

:+1: 759 &nbsp; &nbsp; :thumbsdown: 235

---

### My Solution


### Description
<p>Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.</p>

<p>You need to help them find out their <b>common interest</b> with the <b>least list index sum</b>. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;Piatti&quot;,&quot;The Grill at Torrey Pines&quot;,&quot;Hungry Hunter Steakhouse&quot;,&quot;Shogun&quot;]
<strong>Output:</strong> [&quot;Shogun&quot;]
<strong>Explanation:</strong> The only restaurant they both like is &quot;Shogun&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;KFC&quot;,&quot;Shogun&quot;,&quot;Burger King&quot;]
<strong>Output:</strong> [&quot;Shogun&quot;]
<strong>Explanation:</strong> The restaurant they both like and have the least index sum is &quot;Shogun&quot; with index sum 1 (0+1).
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;KFC&quot;,&quot;Burger King&quot;,&quot;Tapioca Express&quot;,&quot;Shogun&quot;]
<strong>Output:</strong> [&quot;KFC&quot;,&quot;Burger King&quot;,&quot;Tapioca Express&quot;,&quot;Shogun&quot;]
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;KNN&quot;,&quot;KFC&quot;,&quot;Burger King&quot;,&quot;Tapioca Express&quot;,&quot;Shogun&quot;]
<strong>Output:</strong> [&quot;KFC&quot;,&quot;Burger King&quot;,&quot;Tapioca Express&quot;,&quot;Shogun&quot;]
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;KFC&quot;], list2 = [&quot;KFC&quot;]
<strong>Output:</strong> [&quot;KFC&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= list1.length, list2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= list1[i].length, list2[i].length &lt;= 30</code></li>
	<li><code>list1[i]</code> and <code>list2[i]</code> consist of spaces <code>&#39; &#39;</code> and English letters.</li>
	<li>All the stings of <code>list1</code> are <strong>unique</strong>.</li>
	<li>All the stings of <code>list2</code>&nbsp;are <strong>unique</strong>.</li>
</ul>



### My Submission

- Language: Python
- Runtime: 112 ms
- Completed time: 2019-09-21 22:33:02

```Python
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_interest_sum = 999999
        Doris_dict = {}
        res = []
        Andy_dict = {restaurant: index for index, restaurant in enumerate(list1)}

        for index, restaurant in enumerate(list2):
            if restaurant in Andy_dict:
                current_interest_sum = index + Andy_dict[restaurant]
                if current_interest_sum < min_interest_sum:
                    min_interest_sum = current_interest_sum
                    res = []
                if current_interest_sum == min_interest_sum:
                    res.append(restaurant)

        return res
```


### Related Problems
[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (Easy) <br>



### What a(n) Easy problem!
Among **211249** total submissions, **109351** are accepted, with an acceptance rate of **51.8%**. <br>

- Likes: 759
- Dislikes: 235

