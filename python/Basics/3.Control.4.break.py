# coding: UTF-8

testStr = "Python"
print("\nprint testStr => {}".format(testStr))
for nowchar in testStr:
   if nowchar == 'h':
      break
   print("now char: {}".format(nowchar))

varint = 10
print("\nwhile varint => {}".format(varint))
while varint > 0:
   print("now intvalue: {}".format(varint))
   varint -= 1
   if varint == 5:
      break
 