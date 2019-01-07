# coding: UTF-8

print(r'''
【程序13】题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足
''')

import math

def isCompleteSquareNumber(num):
    if num % 10 not in (0,1,4,5,6,9):
        return False
    for x in range(0, num + 1):
        if x * x == num:
            return True
    return False

for item in range(1, 10000):
    if isCompleteSquareNumber(item + 100):
        if isCompleteSquareNumber(item + 168):
            print(item)
