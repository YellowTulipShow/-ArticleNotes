# coding: UTF-8

import random

def show_name(name):
    print("\n" + name)

show_name("随机整数:")
print(random.randint(0, 50))

show_name("随机选取0到100之间的偶数:")
print(random.randrange(0, 100, 2))

show_name("随机浮点数:")
print(random.random())
print(random.uniform(1, 10))

show_name("随机字符")
print(random.choice("zxcvbnmasdf,./;'[]-=\|+_{}:"))
show_name("随机选取字符串:")
print(random.choice(['apple', 'pear', 'peach', 'orange', 'lemon']))


show_name("多个字符中选取特定数量的字符: ")
string_source = "qwertyuiopasdf"
chars_source = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f']
print(random.sample(string_source, 3))
print(random.sample(chars_source, 3))

int_sour = [x for x in range(0, 10)]
print(random.sample(int_sour, 3))

show_name("多个字符中选取特定数量的字符组成新的字符串:")
join_chars = random.sample(chars_source, 3)
print(join_chars)
print("".join(join_chars))

show_name("洗牌:")
print(int_sour)
random.shuffle(int_sour)
print(int_sour)
