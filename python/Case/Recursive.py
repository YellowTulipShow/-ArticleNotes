# coding: UTF-8

# 递归学习, 结果和执行路径

def fun(sign):
    if sign < 5:
        sign += 1
        print('*' * sign)
        spaceT = '\t' * sign
        spaceTJian = '\t' * (sign - 1)
        return 'fun: {}(\n{}{}\n{})'.format(sign, spaceT, fun(sign), spaceTJian)
    else:
        return 'result!: sign<5 !'

print(fun(0))
