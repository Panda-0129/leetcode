import re

from lc_retriever import *

COOKIE = '_ga=GA1.2.1754550287.1598943501; __stripe_mid=e3f7598a-9434-4252-a7ab-b7' \
         '20561ce64da0bd13; __cfduid=dab973380fe547e1d950bc4ead455f21f1607849582; ' \
         '_gid=GA1.2.160726046.1610375693; csrftoken=razaQJXg1StTbaGyBUQuiPkqO5P78' \
         'FH5mqWeJNhZhiCQuHfovSTACGi7zq7Xxwv6; messages="372ec04fdcd7ee05eaa8c83cb' \
         '012e472586eca9e$[[\"__json_message\"\0540\05425\054\"Successfully signed' \
         ' in as Panda-0129.\"]]"; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz' \
         'I1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTY5NjU1NiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6I' \
         'mFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsI' \
         'l9hdXRoX3VzZXJfaGFzaCI6IjdkODNkMmM2MjRjYWM1YThjN2U4Zjk0YjUwNTYzMGZhNGJjZ' \
         'TZjNjAiLCJpZCI6MTY5NjU1NiwiZW1haWwiOiJib2owMTI5MTEyN0BnbWFpbC5jb20iLCJ1c' \
         '2VybmFtZSI6IlBhbmRhLTAxMjkiLCJ1c2VyX3NsdWciOiJQYW5kYS0wMTI5IiwiYXZhdGFyI' \
         'joiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL3BhbmRhLTAxMjkvYXZhdGFyX' \
         'zE1NDkxNzczMDUucG5nIiwicmVmcmVzaGVkX2F0IjoxNjEwMzc1OTE5LCJpcCI6IjguMjEwL' \
         'jM4LjE0MCIsImlkZW50aXR5IjoiOGQyYjQ3ZjYzMjBkZGUyNzRhNmQyYzg5NjZhOWZjZGMiL' \
         'CJzZXNzaW9uX2lkIjo1NjEwNDMxLCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.EQvcw1XP' \
         'KcaBJov5zUNJZW8vmKQ9VqmV1ZWxpR4iqVA; c_a_u="UGFuZGEtMDEyOQ==:1kyyvq:Jf4m' \
         'LZvlHHwvNf0lwwHeIN7AInE"; __atuvc=11%7C2; __cf_bm=6aa66dd88509068024960a' \
         '7e66d261fd0c70ed50-1610382681-1800-Aa3JvPkYpaNxnG5nWU4snM5c1VfexDAlUE+er' \
         'hzWnaEoHzzA0gHN0Z2LUcij4r6al2HYxVllsRH+ro7SvYs7n4Y=; _gat=1'


def embedded_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


if __name__ == '__main__':

    all_md_file = []
    all_accepted_title = []

    path = './Markdown'
    files = os.listdir(path)
    re_digits = re.compile(r'(\d+)')
    files = sorted(files, key=embedded_numbers)
    for file in files:
        all_md_file.append(file)
        file = file.replace(".md", "")
        tmp = file.split()[1:]
        file = " ".join(tmp)
        all_accepted_title.append(file)

    md = '# LeetCode 刷题统计' \
         '\nJackZhao98[项目](https://github.com/JackZhao98/LeetCode-DataRetriever)基础上实现的自动获取LeetCode提交' \
         '\n + **retriever.py**: 获取所有已通过的提交，存入TODO文件夹中' \
         '\n + **generate_readme.py**: 自动生成readme.md' \
         '\n| #    | Title | Difficulty | runtime | memory |' \
         '\n| ---- | ----- | ---------- | ------- | ------ |\n' \
         '---------\n'

    d = LCDataRetriever(COOKIE)
    all_sub = d.retrieve_submissions(verbose=True)
    sub_dict = {}

    for sub in all_sub:
        if sub['status_display'] == 'Accepted':
            sub_dict[d.naive_title_slug(sub['title'])] = sub

    for title, md_title in zip(all_accepted_title, all_md_file):
        try:
            d_ = LCDataRetriever(COOKIE)
            naive_title = d_.naive_title_slug(title)
            print(naive_title)
            question_info = d_.retrieve_question(naive_title)
            if question_info is not None:
                question_id = question_info['questionId']
                md_title = md_title.replace(" ", "%20")
                Title = f'[{title}](https://github.com/Panda-0129/leetcode/blob/master/Markdown/{md_title})'
                difficulty = question_info['difficulty']
                runtime = sub_dict[naive_title]['runtime']
                memory = sub_dict[naive_title]['memory']
                cur_status = f'|{question_id}|{Title}|{difficulty}|{runtime}|{memory}| \n'
                md += cur_status
        except Exception as e:
            continue

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(md)
    pass
