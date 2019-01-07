# coding: UTF-8

testStr = "Python"
print("\nprint testStr => {}".format(testStr))
for nowchar in testStr:
   if nowchar == 'h':
      continue
   print("now char: {}".format(nowchar))

varint = 10
print("\nwhile varint => {}".format(varint))
while varint > 0:
   varint -= 1
   if varint == 5:
      continue
   print("now varint: {}".format(varint))
