# coding: UTF-8

print(r'''
【程序51】题目：随机循环
当时接到的业务是实际显示客户的信息, 感觉有点像音乐播放器的随机循环
要求:
    一个提示列表里面, 提示的信息每隔500ms随机展示
    同一轮循环里面, 一个提示信息只能显示一次
    列表的提示信息全部展示完了, 进行下一轮展示
''')

import random

init_list = [i for i in range(0, 10)]
print('    init_list:', init_list, len(init_list))

sample_list = random.sample(init_list, len(init_list))
print('random.sample:', sample_list, len(sample_list))

def exchange(a, b):
    return b, a

def customize_sample(slist, need_num = 0):
    rlist = []
    slen_size = len(slist)
    if need_num <= 0:
        need_num = slen_size;
    if need_num > slen_size:
        rlist.extend(customize_sample(slist, need_num - slen_size))
        need_num = slen_size
    while need_num > 0:
        need_num -= 1
        index = random.randint(0, need_num)
        rlist.append(slist[index])
        slist[index], slist[need_num] = exchange(slist[index], slist[need_num])
    return rlist

rlist = customize_sample(init_list)
print('        rlist:', rlist, len(rlist))
need_num = 15
rlist = customize_sample(init_list, need_num)
print('        rlist:', rlist, len(rlist), need_num)
