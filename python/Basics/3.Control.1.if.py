# coding: UTF-8

def p(value, name = 'value'):
    print('{} : {}'.format(name, value))

def switch_if_intvalue(intvalue):
    if intvalue == 0:
        p(0)
    elif intvalue == 1:
        p(1)
    elif intvalue == 2:
        p(2)
    elif intvalue == 3:
        p(3)
    elif intvalue == 4:
        p(4)
    elif intvalue == 5:
        p(5)
    else:
        p(999)

def bool_if(boolvalue):
    if boolvalue:
        p('exe if content ({})'.format(boolvalue), 'bool')
    else:
        p('exe else content ({})'.format(boolvalue), 'bool')

print("\nforeach switch_if_intvalue(range(0,7))")
for i in range(0,7):
    switch_if_intvalue(i)

print("\nif bool_if(True and False)")
bool_if(True)
bool_if(False)
