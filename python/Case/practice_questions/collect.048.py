# coding: UTF-8

print(r'''
【程序48】题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
''')

def calc_method(num_data, isEncrypthion):
    length = len(str(num_data))
    arr = []
    value = num_data
    for i in range(0, length):
        v = int(value % 10)
        if isEncrypthion:
            v += 5
        else:
            v -= 5
        v = int(v % 10)
        arr.append(v)
        value /= 10
    arr.reverse()
    value = 0
    for i in range(0, len(arr)):
        v = arr[i] * (10**(i))
        value += v
    return value

# 加密
def encryption(num_data):
    return calc_method(num_data, True)
# 解密
def decrypt(num_data):
    return calc_method(num_data, False)


import random
mylist = [i for i in range(1000, 1000000)]
mylist = random.sample(mylist, 6)
print(mylist)
for item in mylist:
    encry_val = encryption(item)
    decry_val = decrypt(encry_val)
    print('source: {} encryption(加密): {} decrypt(解密): {}'.format(item, encry_val, decry_val))
