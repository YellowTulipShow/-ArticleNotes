# coding: UTF-8
# http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%B7%CF%F1&fr=ala&oriquery=%E5%A4%B4%E5%83%8F&ala=1&alatpl=portait&pos=0

from urllib.request import urlopen,urlretrieve
import re

save_path = "D:\\ZRQDownloads\\userheadimg\\";
source_url_array = [
    "http://image.so.com/i?q=%E5%A4%B4%E5%83%8F&src=srp&pic_type=5&pic_style=11&pic_effect=14&box=box_tx",
    # "https://baike.so.com/doc/1178580-1246621.html",
]


def DownloadImg(sour_url):
    html = urlopen(sour_url).read().decode('utf-8') #html -> charset
    val = re.findall(r'<p>([.]*)</p>', html)
    urls = re.findall(r'"thumb":"(.+?)"', html)
    print(urls)
    for url in urls:
        try:
            url = url.replace('\\','')
            urlretrieve(url, save_path + url.split('/')[-1], callmetho)
        except:
            print('下载失败!')

def callmetho(pre_1 = 0, pre_2 = 0, pre_3 = 0, pre_4 = 0):
    print(pre_1, pre_2, pre_3, pre_4);


for sour_url in source_url_array:
    DownloadImg(sour_url);
