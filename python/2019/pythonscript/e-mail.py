#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import xlrd

class mail_send():
    def __init__(self,username,password,send_to_arrw,mail_address,mail_port,people_name,people_passwd):
        self.username = username
        self.passwd = password
        self.send_to_arrw = send_to_arrw
        self.mail_address = mail_address
        self.mail_port = mail_port
        self.text ="""
        <p>以下为您在苏州中试共享(\\\\10.67.40.166)上的用户名和密码，如有疑问请联系管理员</p>
        <p>用户名:"""+str(people_name)+"""<p>
        <p>密码:"""+str(people_passwd)+"""<p>
        <p>该邮件为系统自动发送，请勿回复"""



    def _format_addr(self,s):
        name, addr = parseaddr(s)#这个函数会解析出姓名和邮箱地址
        print name,addr
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))


    def run(self):
        msg = MIMEText(self.text, 'html', 'utf-8')
        msg['From'] = self._format_addr(u'来自苏州中试共享服务器的通知 <%s>' % self.username)
        msg['To'] = self._format_addr(u'苏州中试共享账号使用人员 <%s>' % self.username)
        msg['Subject'] = Header(u'苏州中试共享服务器-个人账号信息', 'utf-8').encode()
        print msg
        smtpObj = smtplib.SMTP(host=self.mail_address, port=self.mail_port)
        smtpObj.set_debuglevel(1)
        smtpObj.login(self.username, self.passwd)
        smtpObj.sendmail(self.username, self.send_to_arrw, msg.as_string())

class excel_get_value():
    def __init__(self):
        pass

    def run(self):
        lists = []
        excel_data = xlrd.open_workbook(u'人员基础表格.xlsx')
        table = excel_data.sheets()[0]
        #print table.col_values(4)
        user = table.col_values(10)
        passwd = table.col_values(11)
        lists.append(user)
        lists.append(passwd)
        return lists


ge = excel_get_value()
arrw = ge.run()
for index,value in enumerate(arrw[0]):
    list = []
    username = value.encode('utf-8').split('@')[0]
    mail = value.encode('utf-8')
    passwd = arrw[1][index]
    list.append(mail)
    print "username:%s" % username
    print "mail:%s" % mail
    print "passwd:%s" % passwd
    print list
    send_mail = mail_send(username='wuyang@kedacom.com',password='邮箱密码',
                          send_to_arrw=list,mail_address='smtp.kedacom.com',
                          mail_port=25,people_name=username,people_passwd=passwd)
    send_mail.run()



