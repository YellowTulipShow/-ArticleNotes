# coding: UTF-8

print(r'''
【程序31】题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。
''')

array_list = [i for i in range(1, 11)]
print("source: ", array_list)

result_list = [array_list[len(array_list) - 1 - i] for i in range(0, len(array_list))]
print("result: ", result_list)
