# coding: UTF-8

print('''
【程序3】题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
''')

water_numbers = []
for three in range(0, 10):
    for two in range(0, 10):
        for one in range(0, 10):
            this_number = three*100 + two*10 + one
            square_number = three**3 + two**3 + one**3
            if this_number == square_number:
                if this_number > 99:
                    water_numbers.append(this_number)

print(water_numbers)
