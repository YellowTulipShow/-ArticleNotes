# coding: UTF-8

print(r'''
【程序22】题目：利用递归方法求5!。  程序分析：递归公式：fn=fn_1*4!
''')


def AccumulateMultiplication(multiple, index):
    if index <= 1:
        return multiple
    multiple *= index
    index -= 1
    return AccumulateMultiplication(multiple, index)

print(AccumulateMultiplication(1, 4))

