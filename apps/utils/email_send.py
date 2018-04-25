# -*- coding: utf-8 -*-
# ==========================================
# @Time    : 2018/4/3 上午11:09
# @Author  : Mr.Robot
# @File    : email_send.py
# ==========================================

from random import Random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from iMooc.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGHYJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "iMooc--STBoys  账户激活链接"
        email_body = "尊敬的用户:" \
                     "      感谢您注册使用iMooc在线教育平台，请点击以下链接激活您的账号:" \
                     "http://10.120.52.198:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "iMooc--STBoys  密码重置链接"
        email_body = "尊敬的用户：" \
                     "      请点击一下链接重置您的密码:" \
                     "http://10.120.52.198:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
