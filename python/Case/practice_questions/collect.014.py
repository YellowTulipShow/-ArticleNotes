# coding: UTF-8

print(r'''
【程序14】  题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天。
''')

def calc_sum_daycount(year, month, day):
    month_dayCount = [31,28,31,30,31,30,31, 31,30,31,30,31]
    sumcount = 0
    for i in range(0, month - 1):
        sumcount += month_dayCount[i]

    if month_dayCount[month-1] >= day:
        sumcount += day
    elif year % 4 == 0 and month == 2:
        sumcount += month_dayCount[1] + 1
    else:
        sumcount += month_dayCount[month-1]

    if year % 4 == 0 and month > 2:
        sumcount += 1
    return sumcount

print("sum day count: ", calc_sum_daycount(2083, 5, 28))
print("sum day count: ", calc_sum_daycount(2001, 5, 28))
print("sum day count: ", calc_sum_daycount(2000, 5, 28))
print("sum day count: ", calc_sum_daycount(2000, 1, 28))
print("sum day count: ", calc_sum_daycount(2000, 2, 28))
print("sum day count: ", calc_sum_daycount(2000, 2, 29))
print("sum day count: ", calc_sum_daycount(2000, 3, 30))
print("sum day count: ", calc_sum_daycount(2000, 2, 27))
print("sum day count: ", calc_sum_daycount(2000, 2, 28))
print("sum day count: ", calc_sum_daycount(2000, 2, 29))
print("sum day count: ", calc_sum_daycount(2001, 2, 29))
print("sum day count: ", calc_sum_daycount(2000, 2, 30))
