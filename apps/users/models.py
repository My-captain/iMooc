# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from courses.models import Course

# Create your models here.


class UserProfile(AbstractUser):
    # 继承AbstractUser类
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    mobile_phone_number = models.CharField(max_length=11, verbose_name=u"联系电话", default="", blank=True, null=True)
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=7, choices=(("male", u"男"), ("female", u"女")), default="female")
    address = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
        db_table = "user"

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=10)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"所属课程", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图片", max_length=100)
    # image在数据库中实际上存储的是图片的url路径,此处max_length就是对url路径的限定
    desc = models.CharField(max_length=1024, verbose_name=u"轮播图介绍")
    index = models.IntegerField(verbose_name=u"顺序")
    # 当前记录生成时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《' + self.course.name + '》'