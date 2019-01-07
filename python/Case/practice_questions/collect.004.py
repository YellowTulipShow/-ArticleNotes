# coding: UTF-8

print('''
【程序4】题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
note: 质数==素数
''')

import random
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def get_new_prime_number_array(prime_list, max_number):
    if 'list' not in str(type(prime_list)) or len(prime_list) < 1:
        prime_list = [2,]
    min_number = prime_list[len(prime_list)-1]
    max_number = max_number + 10
    if min_number > max_number:
        return prime_list
    for number in range(min_number + 1, max_number + 1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

prime_list = []

request_size = 9999
request_size = 99
value_list = random.sample([x for x in range(0, request_size+1)], int(request_size/10))
for item in value_list:
    prime_list = get_new_prime_number_array(prime_list, item)
    rlist = []
    positive = item
    while positive > 1:
        for prime in prime_list:
            if positive % prime == 0:
                positive /= prime
                rlist.append(str(prime))
                break
    print(item, '=', ' * '.join(rlist))
    print('prime_list.size: ', len(prime_list), end = '\n\n')
print('prime_list', prime_list)
