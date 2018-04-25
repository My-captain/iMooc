# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from orgnization.models import CourseOrg, Teacher

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"类别名称")
    parent = models.ForeignKey('self', verbose_name=u"所属父类别", null=True, blank=True, on_delete=models.CASCADE)
    is_root = models.BooleanField(default=False, verbose_name=u"是否为根节点")
    add_time = models.DateField(default=datetime.now(), verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        node = self
        string = node.name
        while not node.is_root:
            node = node.parent
            string = node.name + '/' + string

        return string


class Course(models.Model):
    # 一般出现这种新增外键的情况都将null设置为True,因为新增的用户完整性约束会与已有数据产生冲突
    # 课程基本信息
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")),
                              max_length=2)

    type = models.ForeignKey(Type, default=None, verbose_name=u"所属类别", null=True, blank=True, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name=u"课程价格", max_length=10, default=0, null=True, blank=True)

    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, verbose_name=u"授课教师", null=True, blank=True, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, verbose_name=u"课程评分")

    total_duration_study = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    students_nums = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"课程封面", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    # 课程类别2017/4/23/1:03添加
    category = models.CharField(default=u"理论知识", max_length=20, verbose_name=u"课程类别")
    # 课程标签2017/4/23/1:34添加
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name
        # db_table = "course"

    def get_course_degree(self):
        if self.degree == 'cj':
            degree = '初级'
        elif self.degree == 'zj':
            degree = '中级'
        else:
            degree = '高级'
        return degree

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        # 反向获取学习了这门课的前5个用户
        return self.usercourse_set.all()[:5]

    def __str__(self):
        return self.name


class Chapter(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"所属课程", on_delete=models.CASCADE, related_name="chapters")
    chapter_order = models.IntegerField(default=0, verbose_name=u"章节序号")
    chapter_title = models.CharField(max_length=128, verbose_name=u"章节标题", null=True, blank=True)
    chapter_desc = models.CharField(max_length=1024, verbose_name=u"章节介绍", null=True, blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章(Chapter)"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《' + self.course.name + '》' + '第' + str(self.chapter_order) + '章/' + self.chapter_title

    def get_related_lessons(self):
        return Lesson.objects.filter(chapter=self)


# 自然逻辑上,Lesson属于Course
# 此处,Lesson与Course属于多对一的关系
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name=u"所属章", on_delete=models.CASCADE, related_name="lessons")
    lesson_order = models.IntegerField(default=0, verbose_name=u"小节序号")
    lesson_name = models.CharField(max_length=128, verbose_name=u"小节标题")
    lesson_time_duration = models.CharField(max_length=10, verbose_name=u"视频时长(xx时xx分xx秒)")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"节(Lesson)"
        verbose_name_plural = verbose_name
        # db_table = "lesson"

    def __str__(self):
        return '《' + self.chapter.course.name + '》' + '第' + str(self.chapter.chapter_order) + '章/第' +\
               str(self.lesson_order) + '节'

    def get_video(self):
        return Video.objects.filter(lesson=self)


class Video(models.Model):
    def upload_to(self, filename):
        print(filename)
        return 'course/video/' + self.lesson.chapter.course.name + '/第' + str(self.lesson.chapter.chapter_order) + \
               '章/第' + str(self.lesson.lesson_order) + '节/' + filename
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    video_source = models.FileField(upload_to=upload_to)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name
        # db_table = "video"

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    """
    课程资源,例如ppt、代码之类的东西
    """
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
        # db_table = "course_resource"

    def __str__(self):
        return self.name
