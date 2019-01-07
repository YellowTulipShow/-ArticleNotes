# coding: UTF-8

print('''
【程序5】题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：(a>b)?a:b这是条件运算符的基本例子。
''')

def print_result(value):
    # char_sign = value >= 90 ? 'A' : 90 > value >= 60 ? 'B' : 'C'
    char_sign = ''
    if value >= 90:
        char_sign = 'A'
    if 90 > value >= 60:
        char_sign = 'B'
    if 60 > value:
        char_sign = 'C'
    print("value: {} 结果字符: {}".format(value, char_sign))

number_list = [90, 91, 85, 55, 48, 60, 65, 100]
for num in number_list:
    print_result(num)
