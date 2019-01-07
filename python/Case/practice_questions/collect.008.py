# coding: UTF-8

print(r'''
【程序8】题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
程序分析：关键是计算出每一项的值。
''')

a = "2"
index = 5
print("calc before value a: ", a)
print("calc before value index: ", index)

Sum = 0

''' method 1: '''
# for i in range(0, index):
#     str_val = a
#     for y in range(0, i):
#         str_val += a
#     print(str_val)
#     Sum += int(str_val);

''' method 2: '''
str_val = ""
for i in range(0, index):
    str_val += a
    print(str_val)
    Sum += int(str_val);

print("result Sum: ", Sum)
