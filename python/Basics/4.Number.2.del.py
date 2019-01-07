# coding: UTF-8

val_1 = 24
val_2 = 67
val_3 = 88
val_4 = 89

def p():
    
    try:
        print("\tval_1: {}".format(val_1))
    except Exception as e:
        print(e)

    try:
        print("\tval_2: {}".format(val_2))
    except Exception as e:
        print(e)

    try:
        print("\tval_3: {}".format(val_3))
    except Exception as e:
        print(e)

    try:
        print("\tval_4: {}".format(val_4))
    except Exception as e:
        print(e)

print("\ninit value:")
p()

print("\nexe: del val_1!")
del val_1
p()

print("\nexe: del val_2 and val_3!")
del val_2, val_3
p()

print("\nat last result: ")
p()
