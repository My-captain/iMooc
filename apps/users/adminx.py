# -*- coding: utf-8 -*-
# ==========================================
# @Time    : 2018/3/27 下午8:23
# @Author  : Mr.Robot
# @File    : adminx.py
# ==========================================
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "iMooc"
    site_footer = "iMooc\n" \
                  "南京中医药大学"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['course', 'title', 'image', 'desc', 'index', 'add_time']
    search_fields = ['course', 'title', 'image', 'desc', 'index']
    list_filter = ['course', 'title', 'image', 'desc', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
