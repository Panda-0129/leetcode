def cal_sum(n, m):
    res = n
    for i in range(m - 1):
        n = n ** 0.5
        res += n

    return round(res, 2)


def run():
    while True:
        try:
            line = input()
            n, m = int(line.split()[0]), int(line.split()[1])
            print(cal_sum(n, m))
        except:
            break


if __name__ == '__main__':
    run()
