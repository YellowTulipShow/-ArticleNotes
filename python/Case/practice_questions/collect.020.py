# coding: UTF-8

print(r'''
【程序20】题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
''')

den = 2 # denominator
mol = 1 # molecular

sumnum = 0.0

for i in range(0, 20):
    itemval = den / mol
    print('{}/{} : {}'.format(den, mol, itemval))
    sumnum += itemval

    l_den = den + mol
    mol = den
    den = l_den

print("sumnum: ", sumnum)

