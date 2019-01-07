# coding: UTF-8

def Print_list(varlist):
    print("\nprint => varlist: {}".format(varlist))
def Print_a(a):
    print("\nprint => a: {}".format(a))

def MemberSymbol(a, varlist):
    print("a in varlist : {}".format(a in varlist)) #如果在指定的序列中找到值返回 True，否则返回 False。
    print("a not in varlist : {}".format(a not in varlist)) #如果在指定的序列中没有找到值返回 True，否则返回 False。

varlist = [1, 2, 3, 4, 5]
Print_list(varlist)

a = 10
Print_a(a)
MemberSymbol(a, varlist)

a = 3
Print_a(a)
MemberSymbol(a, varlist)

a = 'str'
Print_a(a)
MemberSymbol(a, varlist)
