# coding: UTF-8

print(r'''
【程序12】题目：企业发放的奖金根据利润提成。
利润低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成；
从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
''')

def calc_Commission(profit):
    wan = 10000
    if profit <= 10*wan:
        return profit * 0.10
    if profit < 20*wan:
        sum_val = 10*wan * 0.10
        return sum_val + (profit - 10*wan) * 0.075
    if profit < 40*wan:
        return (profit - 20*wan) * 0.05
    if profit < 60*wan:
        return (profit - 40*wan) * 0.03
    if profit <= 100*wan:
        return (profit - 60*wan) * 0.015
    return (profit - 100*wan) * 0.01

# =======================================================
array = [
    484354.52,
    1000000,
    999999,
    1154.548,
    24548.54,
    7484837384351.2,
]
for profit in array:
    print("profit:", profit)
    print("commission:", calc_Commission(profit))



