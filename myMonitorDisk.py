#-*- coding: UTF-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def monitorDiskPctUsed():
    pct_used = int(os.popen("df /dev/xvda1 |sed 1d | awk '{print $5}'|tr -d %").read())
    msg = '服务器vehicle1/task1硬盘超过 %s%%了'%pct_used

    if pct_used>1:
        sendMail('liansheng <liansheng@comodin.cn>', msg, msg)
    return


def sendMail(p_to_addr,p_title,p_msg):
    v_from_addr = 'maintain1@comodin.cn'

    smtp_server = 'smtp.exmail.qq.com'
    password = 'Mypassword520'

    msg = MIMEText(p_msg, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'maintain1 <%s>' % v_from_addr)
    msg['To'] = _format_addr(u'liansheng <%s>' % p_to_addr)
    #msg['CC'] = _format_addr(u'liansheng <%s>' % from_addr)
    msg['Subject'] = Header(p_title, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(0)
    server.login(v_from_addr, password)
    server.sendmail(v_from_addr, [p_to_addr], msg.as_string())
    server.quit()

monitorDiskPctUsed()
