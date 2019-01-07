# coding: UTF-8

def wei():
    print("Hello world!")
    a = 1
    b = 23
    c = 898
    def nei():
        print("nei: ", a, b, c)
        return a
    return nei

var = wei()
var()
