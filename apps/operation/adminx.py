# -*- coding: utf-8 -*-
# ==========================================
# @Time    : 2018/3/27 下午7:52
# @Author  : Mr.Robot
# @File    : adminx.py
# ==========================================

import xadmin


from .models import LessonUserAsk, LessonAskAnswer, LessonUserComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['questioner', 'lesson', 'question', 'add_time']
    search_fields = ['questioner', 'lesson', 'question']
    list_filter = ['questioner', 'lesson', 'question', 'add_time']


class AskAnswerAdmin(object):
    list_display = ['question', 'reply_user', 'reply', 'reply_time']
    search_fields = ['question', 'reply_user', 'reply']
    list_filter = ['question', 'reply_user', 'reply', 'reply_time']


class UserCommentAdmin(object):
    list_display = ['commenter', 'lesson', 'comment', 'add_time']
    search_fields = ['commenter', 'lesson', 'comment']
    list_filter = ['commenter', 'lesson', 'comment', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(LessonUserAsk, UserAskAdmin)
xadmin.site.register(LessonAskAnswer, AskAnswerAdmin)
xadmin.site.register(LessonUserComment, UserCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
