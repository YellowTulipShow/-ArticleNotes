# coding: UTF-8

print(r'''
【程序11】题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。
''')

Candidate_Array = ['1', '2', '3', '4']
Result_Array = []
for a in Candidate_Array:
    for b in Candidate_Array:
        for c in Candidate_Array:
            if a == b or b == c or c == a:
                continue
            val = int(a + b + c)
            Result_Array.append(val)
print("n:", len(Result_Array))
print(Result_Array)
