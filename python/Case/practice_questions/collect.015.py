# coding: UTF-8

print(r'''
【程序15】题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x  与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
''')

import random

def get_int_value():
    return random.randint(0, 50)
x = get_int_value()
y = get_int_value()
z = get_int_value()
print(x, y, z)


