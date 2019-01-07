# coding: UTF-8

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}x{}={}\t".format(j, i, i*j), end="")
    print()

# """ 单词学习:
#     addition 加法
#     subtraction 减法
#     Multiplication 乘法
#     division 除法

#     Nine 九
# """
