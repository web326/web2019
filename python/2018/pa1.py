__author__ ="PSM"
'''用于记录暂时的错误，以便查看'''
import http.client
import urllib.request
import re
import os
import linecache
print("				*************************************************************************")
print("											请输入任何即可开始开始")
print("											可根据提示找到下载位置")
print("		recode.txt为系统记录文件，切勿手动删除，如果文件太大，您可以删除掉除了最后一行的所有内容")
print("									recode.txt删除后，程序会从头开始")
print("				*************************************************************************")
input("										请输入任意内容：")
siteUrl = 'http://www.mmonly.cc' #网页主地址
siteUrl1 = 'http://t1.mmonly.cc'
siteUrl_tag = 'http://www.mmonly.cc/tag' #标签页的地址
Url1_404 = siteUrl1.replace("http://","")#检测404用的测试网站
patNumN = "n=(d*)"
patNumM = 'm=(d*)'
patNumE = 'e=(d*)'
patNumR = 'r=(d*)'
patNumQ = 'q=(d*)'
patNumW = 'w=(d*)'
patNumT = 't=(d*)'
patTagTarget = '<a target="_blank" href="(.*?)" title="(.*?)">(.*?)</a>'#获取标签地址后缀和名称
patTheme = '<div class="title"><span><a target="_blank" href="(.*?)">(.*?)</a>'#每个标签内的每个主题地址和名称
patTpage = "<li><a href='(.*?)' target='_self'>末页</a></li>"#主题页末页的后缀，用来获取主题最后一页的数字
patTpageNum = "/tag/(.*?)/(d*).html' target='_self'>"#获取主题数的页数
patImg = "href='(.*?)'>查看原图</a></li>"#获取主题内图片地址用于下载
patImgPage ='<li><a>(.*?)</a></li>'#获取主题图片的总页数，用于翻页
tagUrl_data = urllib.request.urlopen(siteUrl_tag).read().decode('gbk') #读取标签页的源代码
tagUrl_data_target_result = re.compile(patTagTarget).findall(tagUrl_data)#爬出来标签名称和地址后缀
pathFir = "F:ImgSpider"
pathFirIsExists = os.path.exists(pathFir)
if not pathFirIsExists:
 os.mkdir(pathFir)
else:
 pass
file_recode1 = open(r"F:ImgSpider
ecode.txt","a",encoding="utf-8")
file_recode1.close()
print("已创建出recode.txt文件夹，用于记录和读取")
print("请勿手动删除")
file_recode2 = open(r"F:ImgSpider
ecode.txt","rU",encoding="utf-8")#写入用于记录断点位置的txt文件
file_recode_result = file_recode2.readlines() #将文件中的数值分为一行一行的读取
file_recode2.seek(0)
file_recode2.close()
file_recode_count = len(file_recode_result) #读取记录文件中的行数，用于后面的判定
# print(file_recode.readlines(file_recode_count))
if file_recode_count == 0:
 n = 0 # 表示标签列表的循环
 m = 1 # 表示标签的循环
 q = 0 # 表示主题页中页数的循环
 w = 2 # 表示主题页第一页的循环
 e = 2 # 表示图片页中的页数的循环
 r = 2 # 表示后几页主题的图片页数的循环
 t = 0
else:
 recodeData = linecache.getline(r"F:ImgSpider
ecode.txt",file_recode_count)
 # print(recodeData)
 n = re.compile(patNumN).findall(recodeData)
 # print(n1)
 m = re.compile(patNumM).findall(recodeData)
 # print(m1)
 q = re.compile(patNumQ).findall(recodeData)
 w = re.compile(patNumW).findall(recodeData)
 e = re.compile(patNumE).findall(recodeData)
 r = re.compile(patNumR).findall(recodeData)
 t = re.compile(patNumT).findall(recodeData)
 if bool(n) is True and bool(m) is True and bool(e) is True and bool(r) is True:
 n = n[0]
 m = m[0]
 e = e[0]
 r = r[0]
 q = []
 w = 2
 t = 0
 elif bool(n) is True and bool(w) is True and bool(q) is True:
 n = n[0]
 q = q[0]
 w = w[0]
 m = 1
 e = 2
 r = 2
 t = 0
 elif bool(n) is True and bool(t) is True and bool(w) is True:
 n = n[0]
 t = t[0]
 w = w[0]
 m = 1
 e = 2
 r = 2
 q = 0
n = int(n)#标签的切换，第一个循环 n =0
# print(w1)
while n< len(tagUrl_data_target_result):
 tagName = tagUrl_data_target_result[n][1]#标签的名称
 tagUrlPart = tagUrl_data_target_result[n][0]#标签网址的后缀
 pathTag = "F:\ImgSpider\%s"%tagName#标签路径
 pathTagIsExists = os.path.exists(pathTag)
 if not pathTagIsExists:#创建标签文件夹在本地
 print("检测到您的文件夹内没有[{}]这个文件夹，已帮您成功创建！！".format(str(tagName)))
 os.mkdir(pathTag)
 else:
 print("检测到[{}]这个文件夹已经创建！已自动进入这个文件夹".format(str(tagName)))
 tagUrl = siteUrl + tagUrlPart#每个标签的网址，又是第一页主题页的网址
 tagUrlData = urllib.request.urlopen(tagUrl).read().decode("gbk")#每个标签的源代码，或者第一页主题页的源代码
 themeRe_num = re.compile(patTpageNum).findall(tagUrlData)#主题页数，用于判定主题页是否是1
 m = int(m)
 # print(m)
 if m <len(themeRe_num):#判定主题页数是否为1，不是就会调用翻页程序m =1
 themePage = themeRe_num[0] # 主题的页数
 themeRe = re.compile(patTheme).findall(tagUrlData) # 第一页主题的地址加名称
 if bool(q) is True:
 '''有多个主题页时，第一个主题页里面每个主题图片的下载'''
 while int(q) < len(themeRe):#循环第一页主题q = 0
 '''先把第一页的内容给搞定了'''
 themeName = themeRe[int(q)][1].replace("<b>","").replace("</b>","")#主题名称
 themeUrl = themeRe[int(q)][0]#主题内地址，也是图片页第一页地址
 themePath = "F:\ImgSpider\{}\{}".format(str(tagName),str(themeName))#设置主题名路径
 themePathIE = os.path.exists(themePath)
 if not themePathIE:
 print("检测到您电脑上没有[{}]文件夹，已自动帮您创建！！".format(str(themeName)))
 print("当前路径为[{}]".format(str(themePath)))
 os.mkdir(themePath)
 else:
 print("检测到[{}]已经创建！".format(str(themeName)))
 print("当前路径为[{}]".format(str(themePath)))
 themeUrlData = urllib.request.urlopen(themeUrl).read().decode("gbk")#主题内的源代码可以获取第一页图片地址和图片页数
 inThemeRe = re.compile(patImg).findall(themeUrlData)#第一页图片的下载地址
 inThemePageRe = re.compile(patImgPage).findall(themeUrlData)#获取了图片的页数，用于图片翻页。未处理
 print("已探测到有可下载图片，已开始全速前进开始下载")
 if bool(inThemeRe) is True:
 Url_404 = inThemeRe[0].replace(siteUrl,"")
 Is4041 = http.client.HTTPConnection(Url1_404)
 Is4041.request("GET", Url_404, '', {})
 Is404 = Is4041.getresponse().status
 if Is404 != 404:
 imgPathFir = themePath +"\1.jpg"
 for imgFir in inThemeRe:
 imgFirDown = urllib.request.urlretrieve(imgFir,imgPathFir)
 print("[{}]标签的第[1]页的[{}]主题的第[1]张图片已下载成功".format(str(tagName),str(themeName)))
 else:
 print("[{}]标签的第[1]页的[{}]主题的第[1]张图片未找到下载地址".format(str(tagName),str(themeName)))
 inThemePage = inThemePageRe[0].replace("共","").replace("页: ","")#图片的页数，已处理
 print("[{}]主题已发现了[{}]张图片，加快马达，全速下载！!".format(str(themeName),int(inThemePage)))
 '''第一页主题页图片翻页'''
 while w <= int(inThemePage):#w =2
 '''写入循环数值用于记录'''
 file_recode3 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode3.write("n=%s"%n)
 file_recode3.close()
 file_recode4 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode4.write("q=%s"%q)
 file_recode4.close()
 file_recode5 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode5.write("w=%s"%w)
 file_recode5.close()
 file_recode6 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode6.write("
")
 file_recode6.close()
 imgUrlN = themeUrl.replace(".html","_%s.html"%w)#图片后面页数的地址，用于获取源代码，下载图片
 imgUrlNData = urllib.request.urlopen(imgUrlN).read().decode('gbk')#图片页后面页的源代码
 imgNext = re.compile(patImg).findall(imgUrlNData)#后面页数的下载地址
 Url2_404 = imgUrlN.replace(siteUrl, "")
 # Url11_404 = siteUrl.replace("http://", "")
 Is4041 = http.client.HTTPConnection(Url1_404)
 Is4041.request("GET", Url2_404, '', {})
 Is404 = Is4041.getresponse().status
 if Is404 != 404:
 for imgNex in imgNext:#下载后页数的图片
 imgPathNex = themePath + "\%s.jpg"%w
 imgNextDown = urllib.request.urlretrieve(imgNex,imgPathNex)
 print("[{}]标签的第[1]页的[{}]主题的第[{}]张图片已下载成功！！".format(str(tagName),str(themeName),w))
 else:
 print("[{}]标签的第[1]页的[{}]主题的第[{}]张图片未找到地址！".format(str(tagName),str(themeName),w))
 w =int(w) + 1
 if w > int(inThemePage):
 w = 2
 else:
 w = int(w)
 else:
 print("[{}]主题的第[1]页未发现可下载内容，已自动进入下一主题".format(str(themeName)))
 q =int(q) +1
 if int(q) > len(themeRe) :
 q = 0
 else:
 q = int(q)
 else:
 '''上面第一页搞定了，现在来搞定第n页的图片抓取'''
 while int(m) < len(themePage):#循环主题页数 m = 1与上面m相同，上面用于判定，这里用于循环。
 #先获取后面页数的主题的地址，好用于获取源代码
 themeNextUrl = tagUrl + "/%s.html"%int(m+1)#从第二页主题页开始
 # print(themeNextUrl)
 themeNextData = urllib.request.urlopen(themeNextUrl).read().decode("gbk")#第二页主题开始的源代码
 themeNextRe = re.compile(patTheme).findall(themeNextData)#第二页开始的主题地址和名称
 while int(e)< len(themeNextRe):#循环主题数e = 0
 themeNextName = themeNextRe[int(e)][1].replace("<b>","").replace("</b>","")#第二页开始的主题名
 inThemeNextUrl = themeNextRe[int(e)][0]#第二页开始的主题链接地址也是第一页图片地址
 themePathNext = "F:\ImgSpider\{}\{}".format(str(tagName),str(themeNextName))#第二页开始的主题本地路径
 themePathNextIE = os.path.exists(themePathNext)
 if not themePathNextIE:
 print("检测到您电脑上没有[{}]文件夹，已自动帮您创建！！".format(str(themeNextName)))
 print("当前路径为[{}]".format(str(themePathNext)))
 os.mkdir(themePathNext)
 else:
 print("检测到[{}]已经创建！".format(str(themeNextName)))
 print("当前路径为[{}]".format(str(themePathNext)))
 inThemeNeData = urllib.request.urlopen(inThemeNextUrl).read().decode("gbk")#第一页图片内的源代码
 thNextImgRe = re.compile(patImg).findall(inThemeNeData)#第一页图片地址
 thNextimgPageRe =re.compile(patImgPage) .findall(inThemeNeData)#后面页的页数，未处理
 print("已探测到有可下载图片，已开始全速前进开始下载")
 if bool(thNextImgRe) is True:
 themeNextimgPathFir = themePathNext + "\1.jpg"
 Url4_404 = thNextImgRe[0].replace(siteUrl, "")
 # Url11_404 = siteUrl.replace("http://", "")
 Is4041 = http.client.HTTPConnection(Url1_404)
 Is4041.request("GET", Url4_404, '', {})
 Is404 = Is4041.getresponse().status
 if Is404 != 404:
 for tNimgFir in thNextImgRe:
 tNimgFirDown = urllib.request.urlretrieve(tNimgFir,themeNextimgPathFir)
 print("[{}]标签的第[{}]页的[{}]主题的第[1]张图片已下载成功".format(str(tagName),int(m+1),str(themeNextName)))
 else:
 print("[{}]标签的第[{}]页的[{}]主题的第[1]张图片未找到下载地址！！".format(str(tagName), int(m + 1),
 str(themeNextName)))
 #上面第一张图片完成
 '''现在来搞定后n页图片的下载'''
 thNextimgPage = thNextimgPageRe[0].replace("共","").replace("页: ","")
 print("[{}]主题已发现了[{}]张图片，加快马达，全速下载！!".format(str(themeNextName),int(thNextimgPage)))
 while int(r) <= int(thNextimgPage):#翻页下载后面页的图片，r=2
 file_recode7 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode7.write("n=%s"%n)
 file_recode7.close()
 file_recode8 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode8.write("m=%s"%m)
 file_recode8.close()
 file_recode9 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode9.write("e=%s"%e)
 file_recode9.close()
 file_recode_1 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode_1.write("r=%s"%r)
 file_recode_1.close()
 file_recode_2 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode_2.write("
")
 file_recode_2.close()
 thNextimgN = inThemeNextUrl.replace(".html","_%s.html"%r)
 # print(thNextimgN)
 thNextimgNData = urllib.request.urlopen(thNextimgN).read().decode('gbk')
 thNextimgNRe = re.compile(patImg).findall(thNextimgNData)#后面页数的下载地址
 Url3_404 = thNextimgNRe[0].replace(siteUrl, "")
 # Url1_404 = siteUrl.replace("http://", "")
 Is4041 = http.client.HTTPConnection(Url1_404)
 Is4041.request("GET", Url3_404, '', {})
 Is404 = Is4041.getresponse().status
 if Is404 != 404:
 for thNextimgNex in thNextimgNRe:#下载后面页数的图片
 thNextimgPathNex = themePathNext + "\%s.jpg"%r
 thNextimgNDown = urllib.request.urlretrieve(thNextimgNex,thNextimgPathNex)
 print("[{}]标签的第[{}]页的[{}]主题的第[{}]张图片已下载成功！！".format(str(tagName),int(m+1), str(themeNextName),
 r))
 else:
 print("[{}]标签的第[{}]页的[{}]主题的第[{}]张图片未找到下载地址！！".format(str(tagName),int(m+1), str(themeNextName),
 r))
 r =int(r)+1
 if r > int(thNextimgPage):
 r = 2
 else:
 r = r
 else:
 print("[{}]主题的第[1]页未发现可下载内容，已自动进入下一主题".format(str(themeNextName)))
 '''上面主题页翻页已经完成，下面是主题页只有一页的代码，复制粘贴一下上面主题页第一页的改改就行了'''
 # print(r)
 e=int(e)+ 1
 if int(e)>len(themeNextRe):
 e = 0
 else:
 e = int(e)
 m=int(m)+1
 if int(m)>len(themePage):
 m = 1
 else:
 m = int(m)
 else:
 themeRe = re.compile(patTheme).findall(tagUrlData) # 主题的地址加名称
 while int(t) < len(themeRe):#循环第一页主题t = 0
 '''只有一页的标签的时候搞定代码'''
 themeName = themeRe[int(t)][1].replace("<b>","").replace("</b>","")#主题名称
 themeUrl = themeRe[int(t)][0]#主题内地址，也是图片页第一页地址
 # print(themeUrl)
 themePath = "F:\ImgSpider\{}\{}".format(str(tagName),str(themeName))#设置主题名路径
 themePathIE = os.path.exists(themePath)
 if not themePathIE:
 print("检测到您电脑上没有[{}]文件夹，已自动帮您创建！！".format(str(themeName)))
 print("当前路径为[{}]".format(str(themePath)))
 os.mkdir(themePath)
 else:
 print("检测到[{}]已经创建！".format(str(themeName)))
 print("当前路径为[{}]".format(str(themePath)))
 themeUrlData = urllib.request.urlopen(themeUrl).read().decode("gbk")#主题内的源代码可以获取第一页图片地址和图片页数
 inThemeRe = re.compile(patImg).findall(themeUrlData)#第一页图片的下载地址
 inThemePageRe = re.compile(patImgPage).findall(themeUrlData)#获取了图片的页数，用于图片翻页。未处理
 # print(inThemeRe[0])
 if bool(inThemeRe) is True:
 print("已探测到有可下载图片，已开始全速前进下载")
 imgPathFir = themePath +"\1.jpg"
 Url5_404 = inThemeRe[0].replace(siteUrl, "")
 # Url1_404 = siteUrl.replace("http://", "")
 Is4041 = http.client.HTTPConnection(Url1_404)
 Is4041.request("GET", Url5_404, '', {})
 Is404 = Is4041.getresponse().status
 if Is404 != 404:
 # print(Is404)
 for imgFir in inThemeRe:
 imgFirDown = urllib.request.urlretrieve(imgFir,imgPathFir)
 print("[{}]标签的[{}]主题的第[1]张图片已下载成功".format(str(tagName),str(themeName)))
 else:
 print("[{}]标签的[{}]主题的第[1]张图片已下载成功".format(str(tagName), str(themeName)))
 # print(inThemePageRe)
 inThemePage = inThemePageRe[0].replace("共","").replace("页: ","")#图片的页数，已处理
 # print(inThemePage)
 print("[{}]主题已发现了[{}]张图片，加快马达，全速下载！!".format(str(themeName),inThemePage))
 '''图片翻页'''
 print("已开始下载剩余页数的图片")
 while int(w) <= int(inThemePage):#w =2
 file_recode_3 = open(r"F:ImgSpider
ecode.txt","a",encoding="utf-8")
 file_recode_3.write("n=%s"%n)
 file_recode_3.close()
 file_recode_4 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode_4.write("t=%s"%t)
 file_recode_4.close()
 file_recode_5 = open(r"F:ImgSpider
ecode.txt","a",encoding="utf-8")
 file_recode_5.write("w=%s"%w)
 file_recode_5.close()
 file_recode_6 = open(r"F:ImgSpider
ecode.txt", "a", encoding="utf-8")
 file_recode_6.write("
")
 file_recode_6.close()
 imgUrlN = themeUrl.replace(".html","_%s.html"%int(w))#图片后面页数的地址，用于获取源代码，下载图片
 # print(imgUrlN)
 imgUrlNData = urllib.request.urlopen(imgUrlN).read().decode('gbk')#图片页后面页的源代码
 imgNext = re.compile(patImg).findall(imgUrlNData)#后面页数的下载地址
 Url6_404 = imgNext[0].replace(siteUrl, "")
 # Url1_404 = siteUrl.replace("http://", "")
 Is4041 = http.client.HTTPConnection(Url1_404)
 Is4041.request("GET", Url6_404, '', {})
 Is404 =Is4041.getresponse().status
 if Is404 != 404:
 for imgNex in imgNext:#下载后页数的图片
 imgPathNex = themePath + "\%s.jpg"%w
 imgNextDown = urllib.request.urlretrieve(imgNex,imgPathNex)
 print("[{}]标签的[{}]主题的第[{}]张图片已下载成功！！".format(str(tagName),str(themeName),w))
 else:
 print("[{}]标签的[{}]主题的第[{}]张图片已下载成功！！".format(str(tagName), str(themeName), w))
 w =int(w)+1
 if int(w) >int(inThemePage):
 w =2
 else:
 w =int(w)
 else:
 print("[{}]主题的第[1]页未发现可下载内容，已自动进入下一主题".format(str(themeName)))
 t =int(t) +1
 if int(t)>len(themeRe) :
 t = 0
 else :
 t = int(t)
 n +=1
print("***************************")
print("	请输入任何内容结束")
print("***************************")
input()