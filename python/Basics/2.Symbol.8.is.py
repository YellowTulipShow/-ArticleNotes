# coding: UTF-8

def PrintValue(a, b):
    print("\nprint => a: {} | b: {}".format(a, b), end='\n')

def IdentitySymbol(a, b):
    print("a is b : {}".format(a is b)) #is 是判断两个标识符是不是引用自一个对象
    print("a is not b : {}".format(a is not b)) #is not 是判断两个标识符是不是引用自不同对象

a = 10
b = 10
PrintValue(a, b)
IdentitySymbol(a, b)

a = 5
b = 50
PrintValue(a, b)
IdentitySymbol(a, b)


a = 'assss'
b = "assss"
PrintValue(a, b)
IdentitySymbol(a, b)


a = 'aij'
b = "assss"
PrintValue(a, b)
IdentitySymbol(a, b)


a = 5.00
b = 5
PrintValue(a, b)
IdentitySymbol(a, b)


a = 5
b = '5'
PrintValue(a, b)
IdentitySymbol(a, b)
