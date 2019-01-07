# coding: UTF-8

a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
c = 0
print("init value:")
print("a: {} | b: {}".format(a, b))
print("c: {}".format(c))

print("Bit Symbol:")
c = a & b # 12 = 0000 1100
print("c = a & b | result c: {}".format(c)) #按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0

c = a | b # 61 = 0011 1101
print("c = a | b | result c: {}".format(c)) #按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。

c = a ^ b # 49 = 0011 0001
print("c = a ^ b | result c: {}".format(c)) #按位异或运算符：当两对应的二进位相异时，结果为1 

c = ~a # -61 = 1100 0011
print("c = ~a | result c: {}".format(c)) #按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1

c = a << 2 # 240 = 1111 0000
print("c = a << 2 | result c: {}".format(c)) #左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。

c = a >> 2 # 15 = 0000 1111
print("c = a >> 2 | result c: {}".format(c)) #右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数 
