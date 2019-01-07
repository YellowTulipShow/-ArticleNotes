# coding: UTF-8

print(r'''
【程序18】题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
''')

import random
# random.randint(0, 2)

def isCanGame(Jname, Yname):
    if Jname == 'a' and Yname == 'x':
        return False
    if Jname == 'c' and Yname == 'x':
        return False
    if Jname == 'c' and Yname == 'z':
        return False
    return True

JTeam = ['a','b','c']
YTeam = ['x','y','z']

# while len(JTeam) > 0:
#     Jindex = random.randint(0, len(JTeam) - 1)
#     Yindex = random.randint(0, len(YTeam) - 1)
#     print(JTeam[Jindex], YTeam[Yindex])
#     if isCanGame(JTeam[Jindex], YTeam[Yindex]):
#         print('名单: {} vs {}'.format(JTeam[Jindex], YTeam[Yindex]))
#         del JTeam[Jindex]
#         del YTeam[Yindex]
#     if len(JTeam) == len(YTeam) == 1:
#         print("死循环: ", JTeam[0], YTeam[0])
#         break

# 唯一答案:
#     'c' vs 'y'
#     'a' vs 'z'
#     'b' vs 'x'
# 如果要解答这种题目, 需要以每个人的条件的数目大小排序依次匹配执行, 从多到少


