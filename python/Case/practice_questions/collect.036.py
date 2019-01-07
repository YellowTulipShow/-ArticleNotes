# coding: UTF-8

print(r'''
【程序36】题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
''')

import random

def init_list():
    return
def exchange(a, b):
    return b, a


slist = [i for i in range(1, 9+1)]
print(slist)
# 列表顺序倒序
def ReverseSort(slist):
    for i in range(0, int(len(slist)/2)):
        a = i;
        b = len(slist) - 1 - i
        slist[a], slist[b] = exchange(slist[a], slist[b])
    return slist;
ReverseSort(slist)
print(slist)



slist = [y for y in range(0, 9+1)]
print(slist)
# 将列表中各数位置的index向后推移 m 位
def mobileSort_1(slist, m):
    ssize = len(slist)
    rlist = [0] * ssize
    for i in range(0, ssize):
        si = i + m
        if si >= ssize:
            si = si - ssize
        rlist[si] = slist[i]
    return rlist
# 从列表开头选取 m 个,整体放倒最后
def mobileSort_2(slist, m):
    ssize = len(slist)
    rlist = [0] * ssize
    for i in range(0, ssize):
        si = i + m
        if si >= ssize:
            si = si - ssize
        rlist[i] = slist[si]
    return rlist
print(mobileSort_1(slist, 3))
print(mobileSort_2(slist, 3))
# 两个算法的区别只在于 最后一步 si 和 i 的使用
