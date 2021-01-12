from random import randint

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]

lc_headers = {
    "User-Agent": random_agent,
    "authority": "leetcode.com",
}

lc_all = "https://leetcode.com/api/problems/all/"
lc_submissions = "https://leetcode.com/api/submissions/?offset=%(offset)s&limit=%(limit)s&lastkey=%(lastkey)s"
lc_graphql = "https://leetcode.com/graphql"

query_string = 'query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      paidOnly\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    enableDebugger\n    envInfo\n    libraryUrl\n    adminUrl\n    __typename\n  }\n}\n'

md_template = '''# [%(id)s] %(title)s (%(difficulty)s)

%(small_tags)s

:+1: %(likes)s &nbsp; &nbsp; :thumbsdown: %(dislikes)s

---

### My Solution


### Description
%(contents)s


### My Submission

- Language: %(lang)s
- Runtime: %(runtime)s
- Completed time: %(time)s

```%(lang)s
%(code)s
```


### Related Problems
%(related_problems)s



### What a(n) %(difficulty)s problem!
Among **%(submission)s** total submissions, **%(accepted)s** are accepted, with an acceptance rate of **%(acc_rate)s**. <br>

- Likes: %(likes)s
- Dislikes: %(dislikes)s

'''

related_template = "[%(related_title)s](%(link)s) (%(related_difficulty)s) <br>"

tag_template = "[![%(tag)s_badge](https://img.shields.io/badge/topic-%(tag)s-%(color)s.svg)](%(URL)s) "

raw_md_template = '''## [%(id)s] %(title)s (%(difficulty)s)

%(small_tags)s

👍  %(likes)s &nbsp; &nbsp; 👎  %(dislikes)s

---

## My Submission

- Language: %(lang)s
- Runtime: %(runtime)s
- Completed time: %(time)s

```%(lang)s
%(code)s
```

## Related Problems
%(related_problems)s

## What a(n) %(difficulty)s problem!
Among **%(submission)s** total submissions, **%(accepted)s** are accepted, with an acceptance rate of **%(acc_rate)s**.

- Likes: %(likes)s
- Dislikes: %(dislikes)s

'''
