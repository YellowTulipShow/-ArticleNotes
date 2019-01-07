# coding: UTF-8

# 不使用递归的情况下, 遍历数组/嵌套数组的每一个值

mylist = [[1, 2], 3, 4, 5, 6, [7, 8, 9, [10, 11, 12, 13, 14, [15, 16, 17], 18], 19, 20], [[21, 22, 23], 24, 25], 26]
print(mylist)

resultList = []
while len(mylist) > 0:
    if 'list' in str(type(mylist[0])):
        while mylist[0]:
            mylist.append(mylist[0].pop(0))
        mylist.pop(0)
        continue
    # whlie must need conduct step
    resultList.append(mylist.pop(0))

print("Raw Result Data:")
print(resultList)

# Insertion Sort Method:
def Insertion_Sort(intList):
    for j in range(1, len(intList)):
        key = intList[j]
        i = j - 1
        while i >= 0 and intList[i] > key:
            intList[i + 1] = intList[i]
            i = i - 1
        intList[i + 1] = key
    return intList

print("Sort After:")
resultList = Insertion_Sort(resultList)
print("{} | len: {}".format(resultList, len(resultList)))
