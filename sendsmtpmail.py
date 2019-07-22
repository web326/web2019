#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
ip = '192.168.8.9'
vale = "OK"
# 第三方 SMTP 服务
mail_host = "smtp.kedacom.com"  # 设置服务器
mail_user = "wuweibin@kedacom.com"  # 用户名
mail_pass = "kedacom123"  # 口令
sender = "wuweibin@kedacom.com"
receivers = ["wuweibin@kedacom.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p>用户名:"""+str(ip)+""":不通"""+str(vale)+"""<p>
        """
message = MIMEText(mail_msg,'html', 'utf-8')
message['From'] = "wuweibin@kedacom.com"
message['To'] = "wuweibin@kedacom.com"
subject = '主题：Python SMTP 邮件测试'
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
