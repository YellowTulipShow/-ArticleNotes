# coding: UTF-8

a = 21
b = 10
c = 0
print("init value:")
print("a: {} | b: {}".format(a, b))
print("c: {}".format(c))

print("Assignment Symbol:")
c = a+b
print("c = a+b | c: {}".format(c)) #简单的赋值运算符

c += a
print("c += a | c: {}".format(c)) #加法赋值运算符

c -= a
print("c -= a | c: {}".format(c)) #减法赋值运算符

c *= a
print("c *= a | c: {}".format(c)) #乘法赋值运算符

c /= a
print("c /= a | c: {}".format(c)) #除法赋值运算符

c = 2
print("re Assignment c: {}".format(c))

c %= a
print("c %= a | c: {}".format(c)) #取模赋值运算符

c **= a
print("c **= a | c: {}".format(c)) #幂赋值运算符

c //= a
print("c //= a | c: {}".format(c)) #取整除赋值运算符
