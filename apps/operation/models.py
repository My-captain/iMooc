# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course, Lesson

# Create your models here.


class LessonUserAsk(models.Model):
    # 用户提问
    questioner = models.ForeignKey(UserProfile, verbose_name=u"提问者", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name=u"课程", on_delete=models.CASCADE)
    question = models.CharField(max_length=500, verbose_name=u"问题内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"提问时间")

    def get_related_answers(self):
        return LessonAskAnswer.objects.filter(question=self)

    def get_answer_count(self):
        return self.get_related_answers().count()

    class Meta:
        verbose_name = u"课程提问"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《' + self.lesson.chapter.course.name + '》第' + str(self.lesson.chapter.chapter_order) + '章/第' + \
               str(self.lesson.lesson_order) + '节/' + self.questioner.username + '：' + self.question[:10] + '...'


class LessonAskAnswer(models.Model):
    # 问题回复
    question = models.ForeignKey(LessonUserAsk, verbose_name=u"所属问题", on_delete=models.CASCADE)
    reply_user = models.ForeignKey(UserProfile, verbose_name=u"回复者", on_delete=models.CASCADE)
    reply = models.CharField(max_length=500, verbose_name=u"回复内容")
    reply_time = models.DateTimeField(default=datetime.now, verbose_name=u"回复时间")

    class Meta:
        verbose_name = u"问题回复"
        verbose_name_plural = verbose_name


class LessonUserComment(models.Model):
    # 课程评论、评论不准回复 / 3/27设置只有回复、没有点赞和举报
    commenter = models.ForeignKey(UserProfile, verbose_name=u"评论的用户", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name=u"评论所属章节", on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, verbose_name=u"评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    # 用户收藏   修改：只能收藏课程
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name=u"被收藏的id")
    fav_type = models.IntegerField(verbose_name=u"收藏类型", choices=((1, 'course'), (2, "teacher"), (3, "org")))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"接收用户", on_delete=models.CASCADE)
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    # 用户正在学习的课程
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u"课程", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name
