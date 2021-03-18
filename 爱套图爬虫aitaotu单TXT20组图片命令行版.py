#coding=utf-8
import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup

#自己找代理IP，或者使用无代理的requests.get
dailiip = ['***:**','***:**','***:**']        #代理IP，本次未使用
#imghtml = requests.get(urltxt,proxies={'http':random.choice(dailiip)},headers = Hostreferer)   #如要使用代理爬取，按照此代码更改下面所有请求方法
urlpath = 'D:\\爱套图爬虫aitaotu\\url\\'     #url的txt文件路径
imgpath = 'D:\\爱套图爬虫aitaotu\\图片\\'       #图片要保存的路径
#for i in range(1,112):     #本爬虫最大111页，如需单线程爬取，改下面代码缩进即可，最好上多线程爬取
    #urltxt = open(urlpath + str(i) + ".txt")
urltxt = open(urlpath + "1.txt")        #加载已经获取到的url

for i in urltxt:
    urltxt = "https://www.aitaotu.com" + str(i)     #补全url
    urltxt = urltxt[:-1]        #去除url后面的换行符"\n"
    print (urltxt)
    Hostreferer = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36','Referer': urltxt}
    print (Hostreferer)     #请求头
    imghtml = requests.get(urltxt,headers = Hostreferer)
    soup = BeautifulSoup(imghtml.text,"html.parser")
    findhtml = soup.find('div',{'class':'big-pic'}).find('img')     #查找图片链接所在的元素
    print (findhtml)
    imgname = findhtml.attrs['alt'][:-3]        #获取图片名称，作为目录/文件夹名称使用
    print (imgname)
    imgurl = findhtml.attrs['src']      #获取图片单张链接
    print (imgurl)
    hrefmin = imgurl.split("/")[-1]     #将图片单张链接分割
    hrefmin = hrefmin.split(".")[0]     #获取图片初值，因为有些图片的初始值不是从01开始
    print (hrefmin)
    imgurlmax = soup.find('span',{'id':'picnum'}).find('span',{'class':'totalpage'})
    print (imgurlmax)      #查找图片张数所在的元素
    imgurlmax = imgurlmax.text
    print (imgurlmax)      #获取图片有多少张，用text把元素改换成数值
    imgmaxurl = urltxt[:-5]
    print (imgmaxurl)
    imgmaxurl = imgmaxurl + "_" + imgurlmax + ".html"
    print (imgmaxurl)
    imgmaxurl = requests.get(imgmaxurl,headers = Hostreferer)
    imgmaxurlsoup = BeautifulSoup(imgmaxurl.text,"html.parser")
    imgmaxurl = imgmaxurlsoup.find('div',{'class':'big-pic'}).find_all('img')
    for imgmax in imgmaxurl:
        print (imgmax)
        href = imgmax.attrs['src']
        print(href)
        hrefmax = href.split("/")[-1]
        hrefmax = hrefmax.split(".")[0]
        imgmax = hrefmax
    print (imgmax)
    value = imgmax.isdigit()
    if imgmax.isdigit():
        if int(imgmax) > 199:
            fp=open(urlpath + "error.txt","a")
            fp.write(urltxt + "\n")
            fp.close()
            continue
    else:
        fp=open(urlpath + "error.txt","a")
        fp.write(urltxt + "\n")
        fp.close()
        continue

    imgmun = int(imgurlmax) + int(hrefmin)      #真实张数，因为有些图片初始不是从01.jpg开始，要计算一下



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
        else:
            os.makedirs(imgpath+title.strip().replace('?',''))
            flag = 0        #如果目录/文件夹下没有重复，则创建该目录/文件夹，并设状态机为0
        os.chdir(imgpath + title.strip().replace('?',''))   #进入创建的目录/文件夹
        if(flag == 1 and len(os.listdir(imgpath + title.strip().replace('?',''))) >= int(imgmun)):
            print('已经保存完毕，跳过')     #如果有目录/文件夹重复，且目录/文件夹下的图片也重复，说明已经保存过了
            continue        #检测到已保存，则跳过本次循环，进行爬取下一组

    for n in range(int(hrefmin),int(imgmun)):    #从图片的初值开始循环，初值+图片的数量+1为循环的次数
        href = imgurl.split("/")[:-1]       #处理下图片链接，去除链接尾部需要循环的部分，以"/"字符为分割符，例如：01.jpg，处理后的链接没有"/"字符，且为数组
        imgurl = href[0] + "//" + href[2] + "/" + href[3] + "/" + href[4] + "/" + href[5] + "/" + href[6] + "/"     #把处理后的链接数组合并起来
        if n < 10:      #小于10的尾部链接要加上"0"，否则链接错误，例如:https://***/01.jpg
            imgurl = imgurl + "0" + str(n) +".jpg"
        else:           #大于9的尾部链接无需处理
            imgurl = imgurl + str(n) + ".jpg"
        print (imgurl)
        img = requests.get(imgurl,headers = Hostreferer)       #获取单个图片
        imgname = str(n) + ".jpg"       #单个图片的名称
        f = open(imgname, 'wb')         #打开/创建单个图片，图片是二进制文件，要加b，因为前面已经进入到目录/文件夹，所以不用写文件路径
        f.write(img.content)            #保存图片
        f.close()                       #关闭文件
        time.sleep(0.2)                 #时间间隔，出于对网站的尊重，不要间隔过短，另外尽可能先看一下网站的robots.txt