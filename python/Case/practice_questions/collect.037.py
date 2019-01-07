# coding: UTF-8

print(r'''
【程序37】题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
''')

slist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import random
slist = slist[0:random.randint(5, len(slist))]


def play(slist):
    ERRV = '0'
    rlist = [i for i in slist]

    remaining_number = len(rlist)
    report = 0
    index = -1
    while remaining_number > 1:
        index += 1
        if index >= len(rlist):
            index = 0
        if rlist[index] == ERRV:
            continue
        report += 1
        if report == 3:
            report = 0
            remaining_number -= 1
            rlist[index] = ERRV
    for i in range(0, len(rlist)):
        if rlist[i] != ERRV:
            return i
    return 0

r_index = play(slist)
print(slist, r_index, slist[r_index])
