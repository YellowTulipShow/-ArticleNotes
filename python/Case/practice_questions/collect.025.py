# coding: UTF-8

print(r'''
【程序25】题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
''')

number_length = 5

def isNumberOfPalindromes(number):
    copy_val = number
    vlist = []
    for x in range(1, len(str(copy_val)) + 1):
        vlist.append(copy_val % 10)
        copy_val = int(copy_val / 10)

    for i in range(0, len(vlist)):
        if vlist[i] != vlist[len(vlist) - 1 - i]:
            return False
    return True

# test dev:
upper_limit = 12320
lower_limit = 12322

upper_limit = 10000
lower_limit = 99999

nof_size = 0
for number in range(upper_limit, lower_limit + 1):
    isNOF = isNumberOfPalindromes(number)
    if isNOF:
        nof_size += 1
        print('数值:', number, '是否回文数:', isNOF)
print('范围:', upper_limit, '-', lower_limit, '回文数共:', nof_size)
