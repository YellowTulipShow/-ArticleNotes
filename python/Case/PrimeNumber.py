# coding: UTF-8

def PrimeNumber(max_num):
    rlist = []
    i = 2
    while i < max_num:
        j = 2
        while j <= (i/j):
            if not i%j:
                break
            j += 1
        if j > i/j:
            rlist.append(i);
        i += 1
    return rlist

max_num = 2000
rlist = PrimeNumber(max_num)
print("{} 以内的素数列表: {}".format(max_num, rlist))
