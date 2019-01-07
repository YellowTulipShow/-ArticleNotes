# coding: UTF-8

def wai(obj):
    def nei(intvalue):
        print("world hello")
        var = obj(intvalue)
        intvalue = 846
        print("intvalue: ", intvalue)
        return var
    return nei

@wai # @wai => wai(func)()
def func(intvalue):
    print("Hello World, ", intvalue)

func(3)
