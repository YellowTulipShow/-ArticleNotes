# coding: UTF-8

print('''
【程序2】题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
''')

prime_number = []
for number in range(101, 200+1):
    is_prime_number = True
    for i in range(2, number):
        if number % i == 0:
            is_prime_number = False
            break
    if is_prime_number:
        prime_number.append(number)
print(prime_number)
