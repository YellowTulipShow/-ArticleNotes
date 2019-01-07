# coding: UTF-8

print(r'''
【程序24】题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
''')


# 5134
# 4
# 4 3 1 5

number = 5134
print(number, len(str(number)), "位数")
for i in range(1, len(str(number)) + 1):
    print(number % 10)
    number = int(number / 10)




