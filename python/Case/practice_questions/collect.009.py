# coding: UTF-8

print(r'''
【程序9】题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
''')

Complete_number = []
for num in range(1, 1000 + 1):
    factor = []
    for f in range(1, num):
        if num % f == 0:
            factor.append(f)
    sum_val = 0
    for item in factor:
        sum_val += item
    if sum_val == num:
        print(num, factor)