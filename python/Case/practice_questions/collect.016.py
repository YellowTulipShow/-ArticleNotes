# coding: UTF-8

print(r'''
【程序16】题目：输出9*9口诀。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
''')

for x in range(1, 10):
    for y in range(1, x + 1):
        print("{}x{}={}\t".format(x, y, x*y), end='')
    print('')
