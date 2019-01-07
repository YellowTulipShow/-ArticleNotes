# coding: UTF-8

print(r'''
【程序47】题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
''')

import random
mylist = [i for i in range(1, 51)]
mylist = random.sample(mylist, 7)
print(mylist)

for item in mylist:
    # method 1:
    for i in range(0, item):
        print('*', end='')
    print(' ' + str(item))

    # python method:
    print('*'*item, str(item))
