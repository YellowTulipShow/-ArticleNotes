# coding: UTF-8

# print(r'''
# int(x)                  将x转换为一个整数  
# long(x)                 将x转换为一个长整数  
# float(x)                将x转换到一个浮点数  
# complex(x)              将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y)           将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。 
# str(x)                  将对象 x 转换为字符串  
# repr(x)                 将对象 x 转换为表达式字符串  
# eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象  
# tuple(s)                将序列 s 转换为一个元组  
# list(s)                 将序列 s 转换为一个列表  
# chr(x)                  将一个整数转换为一个字符  
# unichr(x)               将一个整数转换为Unicode字符  
# ord(x)                  将一个字符转换为它的整数值  
# hex(x)                  将一个整数转换为一个十六进制字符串  
# oct(x)                  将一个整数转换为一个八进制字符串  
# ''')

import math   # 导入 math 模块

# print ("math.modf(100.12) : ", math.modf(100.120))
# print ("math.modf(100.72) : ", math.modf(100.72))
# print ("math.modf(119) : ", math.modf(119))
# print ("math.modf(math.pi) : ", math.modf(math.pi))

print(15 % 4)

print(dir(math))
print(math.pi)
print(math.e)