# coding: UTF-8

print(r'''
【程序10】题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
''')

height = 100
sum_distance = 0.0
for index in range(1, 10+1):
    sum_distance += height
    rebound = height / 2
    sum_distance += rebound
    height = rebound
    print("index:", index, " rebound:", rebound)
print("sum_distance:", sum_distance)
