# coding: UTF-8

print(r'''
【程序27】题目：求100之内的素数
''')

# 取快速得到数列中素数的算法

# def FastWayToGetPrimes(num_list):
#     result_list = []
#     print(num_list)
#     for item in num_list:
#         result_list.append(item)
#     return result_list

print(FastWayToGetPrimes(x for x in range(1, 100 + 1)))
