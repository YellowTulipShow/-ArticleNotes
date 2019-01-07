# coding: UTF-8

print(r'''
【程序39】题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n(利用指针函数)
''')

def calc_method(n):
    denominator = 1
    if n % 2 == 0:
        denominator += 1
    sum = 0.0
    while denominator <= n:
        sum += (1 / denominator)
        denominator += 2
    return sum

sum = calc_method(4)
print(sum)
