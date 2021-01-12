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

if __name__ == '__main__':
    d = LCDataRetriever(COOKIE)
    # for page in range()
    all_sub = d.retrieve_submissions(verbose=True)
    all_accepted_sub = []
    for sub in all_sub:
        if sub['status_display'] == 'Accepted' and sub['lang'] == 'python3':
            all_accepted_sub.append(sub)

    md = '| #    | Title | Difficulty | runtime | memory | \n | ---- | ----- | ---------- | ------- | ------ | \n '
    for sub in all_accepted_sub[0:10]:
        question_info = d.retrieve_question(d.naive_title_slug(sub['title']))
        question_id = question_info['questionId']
        Title =
        cur_status = f'|{question_id}||||'
    pass