import re

from lc_retriever import *

COOKIE = ''


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
         '\nJackZhao98[项目](https://github.com/JackZhao98/LeetCode-DataRetriever)基础上实现的自动获取LeetCode历史ac' \
         '\n + **retriever.py**: 获取所有ac，存入文件夹中' \
         '\n + **generate_readme.py**: 自动生成readme.md' \
         '---------\n' \
         '\n| #    | Title | Difficulty | runtime | memory |' \
         '\n| ---- | ----- | ---------- | ------- | ------ |\n'
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
