# coding: UTF-8

print(r'''
【程序19】题目：打印出如下图案（菱形）

7 * 8:

    *
   ***
 ******
********
 ******
  ***
   *

    *       4s 1
   ***      3s 3
 ******     1s 5
********    0s 8
 ******     1s 5
  ***       2s 3
   *        3s 1


7 * 9:

    *
   ***
 *******
*********
 *******
   ***
    *

程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重 for循环，第一层控制行，第二层控制列。
''')

row_num = 7
row_diff = 1

column_num = 8
col_diff = 2


def intval(sum_num):
    z = 0
    if sum_num % 2 == 1:
      z = 1
    return int(sum_num / 2) + z

for l in range(0, row_num + 1):
    space_num = 1
    star_num = 1
    space_num = (intval(row_num) - l) * row_diff
    star_num = (l + 1) * 2 - 1
    print(' '*space_num + '*'*star_num)


