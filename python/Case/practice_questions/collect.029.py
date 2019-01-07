# coding: UTF-8

print(r'''
【程序29】题目：求一个3*3矩阵对角线元素之和  程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
''')

digital_matrix = [
    [1, 2, 1, 8],
    [6, 5, 4, 7],
    [4, 1, 8, 6],
    [4, 1, 8, 4],
]

row_num = 4
column_num = row_num

sum_one = 0
sum_two = 0
for r in range(0, row_num):
    sum_one += digital_matrix[r][r]
    sum_two += digital_matrix[r][column_num - 1 - r]
print(sum_one)
print(sum_two)
