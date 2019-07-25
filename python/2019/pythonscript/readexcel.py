#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  xlrd
import os,time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

'''
class Excel_get_value():
    def __init__(self):
        pass

    def run(self):
        lists = []
        excel_data = xlrd.open_workbook(u'园区设备管理总表20190708.xlsx')
        table = excel_data.sheets()[0]
        ipaddr = table.col_values(12)
        #print (table.col_values(12)[3:-1])

        lists.append(ipaddr[3:-1])
        #print (lists)
        return lists

ge = Excel_get_value()
arrw = ge.run()

for index,value in enumerate(arrw[0]): #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    #print (index,value)
    man_file = open('man_data.txt', 'a')
    if len(value) == 0:
        print('此行IP地址为空，无数据，跳过',file=man_file)
        pass
    else:
        pings = os.popen(('ping -n 1 %s')%value).readlines()
        try:
            #print(pings[2])
            #lls = pings[2]
            if pings[2] in '请求超时。\n':
                time.sleep(3)
                print (('第%s个IP地址')%index,('IP:%s')%value,'IP存在问题，网络不通，请检查！',file=man_file)
            else:
                print(('第%s个IP地址')%index,('IP:%s') % value, '网络OK！',file=man_file)
        except:
            print(('第%s个IP地址')%index,('IP:%s')%value,'文件存在问题，无法进行ping操作，请检查excel文件！',file=man_file)
            pass
    print('测试结束，请查看报告', file=man_file)
    man_file.close()
'''

man_file = open('man_data.txt', 'r')
data = man_file.readlines()
man_file.close()
'''
mail_msg = []
for v in range(0,(len(data))):
    msg = data[v]
    print(msg)
    mail_msg = mail_msg.append(msg)
print('邮件信息：',mail_msg)
'''


mail_msg = """
        <p>""" + str(data) + """<p>
        """
mail_host = "smtp.kedacom.com"  # 设置服务器
mail_user = "wuweibin@kedacom.com"  # 用户名
mail_pass = "kedacom123"  # 口令
sender = "wuweibin@kedacom.com"
receivers = ["wuweibin@kedacom.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


message = MIMEText(mail_msg,'html', 'utf-8')
message['From'] = "wuweibin@kedacom.com"
message['To'] = "wuweibin@kedacom.com"
subject = '主题：IP地址监控自动化邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.set_debuglevel(1)
    smtpObj.connect(mail_host, 25 )  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    #smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.sendmail(sender, receivers, message.as_string().encode())
    print( "邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
