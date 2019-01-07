# coding: UTF-8

print(r'''
【程序7】题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'.
''')

input_str = ''
# input_str = input("输入一行字符:")
input_str = '''hfu3rh2-3kj
xcpvm243-0t2-34.  mcvokpe4ot/sdlg57-*216s4dgmlodf
jgw'''

import re
ChineseEnglish_Count = Space_Count = Number_Count = Other_Count = 0

index = 0
print("calc before sum count: ", len(input_str));
while index < len(input_str):
    char = input_str[index]
    index += 1
    if char == '\n':
        break
    if re.search(r'[a-zA-Z\u4e00-\u9fa5]', char):
        ChineseEnglish_Count += 1
        continue
    if re.search(r'\s', char):
        Space_Count += 1
        continue
    if re.search(r'\d', char):
        Number_Count += 1
        continue
    Other_Count += 1
print("ChineseEnglish_Count: ", ChineseEnglish_Count)
print("Space_Count: ", Space_Count)
print("Number_Count: ", Number_Count)
print("Other_Count: ", Other_Count)
print("calc after sum count: ", ChineseEnglish_Count + Space_Count + Number_Count + Other_Count);
