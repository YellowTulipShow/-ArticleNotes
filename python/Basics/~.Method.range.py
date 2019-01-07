# coding: UTF-8

numlist = range(0, 5)
print(numlist)
print(type(numlist))
print(list(numlist))

print("\nSet step number: ")
print(list(range(0, 5, -2)))
try:
    print(list(range(0, 5, 0)))
except Exception as e:
    print(e)
print(list(range(0, 5, 1)))
print(list(range(0, 5, 2)))
print(list(range(0, 5, 3)))
print(list(range(0, 5, 4)))
print(list(range(0, 5, 5)))

print('''
note region:
    for i in range(0, 5) == for (var i = 0; i < 5; i++)

    python 2.x 尽量使用 xrange() 生成数列生成器, 性能优异
    python 3.x range() 实现内容和 xrange() 是一样的了, 并且 xrange() 被移除了
''')
