
fsmax = 18.0
fsmin = 8.0
num = 16

min_size = 100

cha = fsmax - fsmin
item = cha / num
for i in range(0, num+1):
    v = i * item + fsmin
    htmlsize = v * 1.5
    size = 50 * i
    size += min_size
    print("@media screen and (min-width: {}px) {{ html {{ font-size: {}px; }} body {{ font-size: {}px; }} }}".format(size, htmlsize, v));
