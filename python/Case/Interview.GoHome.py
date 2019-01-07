# coding: UTF-8
print(r'''
百度2017春招笔试真题编程题：度度熊回家
    一个数轴上共有N个点，第一个点的坐标是度度熊现在位置，第N-1个点是度度熊的家。现在他需要依次的从0号坐标走到N-1号坐标。
    但是除了0号坐标和N-1号坐标，他可以在其余的N-2个坐标中选出一个点，并直接将这个点忽略掉，问度度熊回家至少走多少距离？
输入描述:
    输入一个正整数N, N
    接下来N个整数表示坐标，正数表示X轴的正方向，负数表示X轴的负方向。绝对值小于等于100
输出描述:
    输出一个整数表示度度熊最少需要走的距离。
输入例子:
    4
    1 4 -1 3
输出例子:
    4

疑似答案:
https://blog.csdn.net/wdays83892469/article/details/79275912
https://blog.csdn.net/Jeaforea/article/details/76152801
''')

import random
points = [int(random.uniform(-100, 100)) for i in range(1, 4+1)]
# points = [1, 4, -1, 3]
# points = [54, -82, 27, -59]
print("points:", points);

def go_home(points):
    def sum_length(points):
        sumlen = 0
        for i in range(1, len(points)):
            sumlen += abs(points[i] - points[i-1])
        return sumlen
    def eliminate(points, index):
        l = []
        for i in range(0, len(points)):
            if i == index:
                continue
            l.append(points[i])
        return l
    minsum = 0
    for i in range(1, len(points) - 1):
        el = eliminate(points, i)
        sumlen = sum_length(el)
        print("    el:", el, "sumlen:", sumlen)
        if sumlen < minsum or minsum == 0:
            minsum = sumlen
    return minsum

print("go_home min length: ", go_home(points))


