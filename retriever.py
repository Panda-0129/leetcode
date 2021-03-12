from lc_retriever import *

COOKIE = ''
if __name__ == '__main__':
    d = LCDataRetriever(COOKIE)
    # for page in range()
    all_sub = d.retrieve_submissions(verbose=True)
    all_accepted_sub = []
    for sub in all_sub:
        if sub['status_display'] == 'Accepted':
            all_accepted_sub.append(sub)

    for sub in all_accepted_sub:
        w = LCDownloader(COOKIE, target_folder='TODO')
        w.write_to_md(sub)
    pass
