# coding: UTF-8

print('''
【程序1】题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？1.程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
''')

print("输出数列: 100周的结果数列")

# def number_list(sequence):
#     for month in range(3, 1555+1):
#         program_sign_i = month - 1
#         one = sequence[program_sign_i - 2]
#         two = sequence[program_sign_i - 1]
#         result = one + two;
#         print(result)
#         sequence.append(result)
#         if len(str(result)) > 100:
#             break;
#     print(sequence)
#     print("len: ",len(sequence))
# number_list(sequence = [1, 1])

# def number_list(first_num, second_num):
#     result = first_num + second_num
#     print(result)
#     if len(str(result)) < 209:
#         number_list(second_num, result)
# number_list(1, 1)

# def number_list(first_num = 1, second_num = 1):
#     while len(str(second_num)) < 209:
#         result = first_num + second_num
#         first_num = second_num
#         second_num = result
#         print(result)
# number_list()

def number_list(first_num = 1, second_num = 1):
    array = [first_num, second_num]
    while len(str(second_num)) < 209:
        result = first_num + second_num
        first_num = second_num
        second_num = result
        array.append(result)
    print(array)
number_list()
