# coding: UTF-8

print(r'''
【程序21】题目：求1+2!+3!+...+20!的和
程序分析：此程序只是把累加变成了累乘。
''')

# 1! + 2! + 3! + 4! + 5!
# 1*1 + 1*2 + 1*2*3 + 1*2*3*4 + 1*2*3*4*5

size_count = 20000
# size_count = 4

def method_1():
    def AccumulateMultiplication(number):
        sumnum = 1
        for num in range(1, number + 1):
            sumnum *= num
        return sumnum
    sumnum = 0
    for num in range(1, size_count + 1):
        sumnum += AccumulateMultiplication(num)
    print(sumnum)
    # 1.4s

def method_2():
    sumnum = 1
    multiple = 1
    for num in range(2, size_count + 1):
        multiple *= num
        sumnum += multiple
    print(sumnum)
    # 0.2s

# method_1()
method_2()


