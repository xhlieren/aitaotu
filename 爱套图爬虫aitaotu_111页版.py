#coding=utf-8
import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.aitaotu.com/tag/rosi/'
#dailiip = ['***:**','***:**','***:**']
path = 'D:\\爱套图爬虫aitaotu\\url\\'

for n in range(1,111):
    url111 = url + str(n) + '.html'
    Hostreferer = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36','Referer':url111}
    #html = requests.get(url111,proxies={'http':random.choice(dailiip)},headers = Hostreferer)
    html = requests.get(url111,headers = Hostreferer)
    soup = BeautifulSoup(html.text,"html.parser")
    pic_url = soup.find('div',id="mainbody").find_all('a',class_="Pli-litpic")
    print (pic_url)
    for i in pic_url:
        href = i.attrs['href']
        fp=open(path + str(n) +".txt","a")
        fp.write(href + "\n")
        fp.close()
        print(href)
    time.sleep(1)

#使用代理的请求方式
#html = requests.get(url111,proxies={'http':random.choice(dailiip)},headers = Hostreferer)
#不使用代理的请求方式
#html = requests.get(url111,headers = Hostreferer)