# coding: UTF-8

print('''
【程序6】题目：输入两个正整数m和n，求其最大公约数和最小公倍数。
程序分析：利用辗除法。

如 a:4 b:6
最大公约数: "记为 (a, b)"
    a约数: 1, 2, 4
    b约束: 1, 2, 3, 6
    其中 2 为 公约数

最小公倍数:"记为 [a, b]"
    a倍数: 4, 8,  12, 16, 20, 24, ...
    b倍数: 6, 12, 18, 24, 30, 36, ...
    其中 12, 24 为公倍数 12 为最小公倍数
''')

# a = input("输入第一个数 a:")
a = 4
# b = input("输入第一个数 b:")
b = 6

a = int(a);
b = int(b);

def Greatest_Common_Divisor(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a;

def Least_Common_Multiple(a, b):
    return (a * b) / Greatest_Common_Divisor(a, b)

print("最大公约数: ", Greatest_Common_Divisor(a, b))
print("最小公倍数: ", Least_Common_Multiple(a, b))
