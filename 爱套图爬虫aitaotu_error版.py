#coding=utf-8
import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup

#dailiip = ['117.185.17.145:80','180.97.34.35:80','111.13.100.91:80']        #代理IP，本次未使用
#imghtml = requests.get(urltxt,proxies={'http':random.choice(dailiip)},headers = Hostreferer)   #如要使用代理爬取，按照此代码更改下面所有请求方法
urlpath = 'D:\\爱套图爬虫aitaotu\\url\\'     #url的txt文件路径
imgpath = 'D:\\爱套图爬虫aitaotu\\图片\\'       #图片要保存的路径
#for i in range(1,112):     #本爬虫最大111页，如需单线程爬取，改下面代码缩进即可，最好上多线程爬取
    #urltxt = open(urlpath + str(i) + ".txt")
urltxt = open(urlpath + "error.txt")        #加载已经获取到的url
for i in urltxt:
    urltxt = i[:-1]        #去除url后面的换行符"\n"
    print (urltxt)
    Hostreferer = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36','Referer': urltxt}
    print (Hostreferer)     #请求头
    imghtml = requests.get(urltxt,headers = Hostreferer)
    soup = BeautifulSoup(imghtml.text,"html.parser")
    findhtml = soup.find('div',{'class':'big-pic'}).find('img')     #查找图片链接所在的元素
    print (findhtml)
    imgname = findhtml.attrs['alt'][:-3]        #获取图片名称，作为目录/文件夹名称使用
    print (imgname)
    imgurlmax = soup.find('span',{'id':'picnum'}).find('span',{'class':'totalpage'})
    print (imgurlmax)      #查找图片张数所在的元素
    imgurlmax = imgurlmax.text
    print (imgurlmax)      #获取图片有多少张，用text把元素改换成数值
    imgmaxurl1 = urltxt[:-5]
    print (imgmaxurl1)

    title = imgname                     #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace(',', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('?', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace(':', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('：', '')     #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('，', '')     #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('<', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('>', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace(' ', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('[', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace(']', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('\'', '')     #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('\\', '')     #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('!', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('！', '')     #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('_', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('"', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符
    title = title.replace('.', '')      #对获取图片名称处理一下，防止有影响目录/文件夹创建的特殊字符

    if(title != ''):        #检查图片名称是否为空
        print("准备扒取："+title)

        if(os.path.exists(imgpath+title.strip().replace('?',''))):
            flag = 1        #检查存放图片的目录/文件夹下是否重复，如果有相同的目录/文件夹在，则设状态机为1
            print('已经保存完毕，跳过') 
            time.sleep(1)
            continue        #检测到已保存，则跳过本次循环，进行爬取下一组
        else:
            os.makedirs(imgpath+title.strip().replace('?',''))
            flag = 0        #如果目录/文件夹下没有重复，则创建该目录/文件夹，并设状态机为0
        os.chdir(imgpath + title.strip().replace('?',''))   #进入创建的目录/文件夹

    for i in range(1,int(imgurlmax) + 1):

        imgmaxurl = imgmaxurl1 + "_" + str(i) + ".html"
        print (imgmaxurl)
        imgmaxurl = requests.get(imgmaxurl,headers = Hostreferer)
        imgmaxurlsoup = BeautifulSoup(imgmaxurl.text,"html.parser")
        imgmaxurl = imgmaxurlsoup.find('div',{'class':'big-pic'}).find_all('img')
        print (imgmaxurl)
        for imgmax in imgmaxurl:
            print (imgmax)
            imgurl = imgmax.attrs['src']
            print (imgurl)
            img = requests.get(imgurl, headers = Hostreferer)       #获取单个图片
            hrefmax = imgurl.split("/")[-1]
            hrefmax = hrefmax.split(".")[0]
            imgname = str(hrefmax) + ".jpg"       #单个图片的名称
            f = open(imgname, 'wb')         #打开/创建单个图片，图片是二进制文件，要加b，因为前面已经进入到目录/文件夹，所以不用写文件路径
            f.write(img.content)            #保存图片
            f.close()                       #关闭文件
            time.sleep(0.5)                 #时间间隔，出于对网站的尊重，不要间隔过短，另外尽可能先看一下网站的robots.txt