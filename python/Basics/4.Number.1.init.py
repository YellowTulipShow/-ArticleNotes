# coding: UTF-8

print('''
Python 三种数值类型: 
    Int: (整形)
        通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
        Long integers(长整型)
            无限大小的整数，整数最后是一个大写或小写的L。
    float: (浮点型)
        浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
    complex: (复数)
        复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
''')

intvalue = 9983428093840928349820340982042340
print("intvalue: {}".format(intvalue))
