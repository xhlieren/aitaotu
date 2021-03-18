# 爱套图爬虫简介
## 项目分3种py文件

* 1，获取每组图片的网址，并保存网址到指定文件，因为本项目一个页面包含20组图片，所以每20组图片网址保存为一个txt文件  
- 爱套图爬虫aitaotu_111页版.py  
* 2，读取保存好的ulr文件，用于循环url文件，从中获取一组图片的url，然后通过该组图片的url进行爬取图片  
- 爱套图爬虫aitaotu单TXT20组图片版.py  
* 3，该项目图片框架无关，大量图片每页一张，有少量图片每页多张，所以把每页多张的图片从（2）中挑选出来，单独爬取  
- 爱套图爬虫aitaotu_error版.py  
- **PS：分文件的好处是，能同时开多个py同时爬取，只需读取不同URL文件即可** 
****
## 项目分2种显示方式  
* 1，命令行版  
- 命令行显示爬取时的一些信息  
* 2，python-tk版  
- 把爬取时的主要信息通过python-tk显示  
- **PS：图片刷新采用每组图片建立一个窗口显示，该组图片爬取完成后关闭该窗口，爬下一组图片时重新建立新窗口**  
- **PS：为何要每组图片单独建立窗口显示？测试python-tk在一个窗口刷新22万张图片时百分百崩溃，故采用一组图片一个窗口的方法**  
- **PS：对python-tk是在爬虫项目中首次使用，多次测试无问题，连续运行状态未知**  
- **PS：为防止爬取的图片已存在时，python-tk无图片显示而意外崩溃，请在python-tk版143行filenametk =（'D：\ 1 \ 1.jpg'）更改为自己的一张图片（任意路径任意图片）（V1.1中删除）**
- **PS：命令行版的爬取效率约为python-tk版的6倍，因此python-tk版决定暂时只更新到V1.1版本**  
****
## 项目代码说明  
* 本示例代码，仅获取爱套图ROSI标签下的111页图片网址  
* 如要爬取其他标签或全部图片，请在（1）文件中修改  
****
## 项目声明<br>
### 此代码仅用于python学习交流使用<br>
****
## python-tk版示例
![](https://github.com/xhlieren/aitaotu/blob/main/%E7%88%B1%E5%A5%97%E5%9B%BEpython-tk%E6%98%BE%E7%A4%BA%E7%A4%BA%E4%BE%8B.png)<br>
****
## 更新说明
* **V1.1**  
- 更改了python-tk版窗口部分代码的写法，倒置
- 删除无用代码，添加注释等
## 更新预告
* **V1.2**
- 预计在V1.2中添加代理使用新方法
- 预计在V1.2中添加自动获取本地path方法
