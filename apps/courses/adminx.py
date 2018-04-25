# -*- coding: utf-8 -*-
# ==========================================
# @Time    : 2018/3/27 上午11:56
# @Author  : Mr.Robot
# @File    : adminx.py
# ==========================================

import xadmin
from .models import Type, Course, Chapter, Lesson, Video, CourseResource


class TypeAdmin(object):
    list_display = ['name', 'parent', 'is_root', 'add_time']
    search_fields= ['name', 'parent', 'is_root']
    list_filter = ['name', 'parent', 'is_root', 'add_time']


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'course_org', 'teacher', 'score', 'total_duration_study',
                    'students_nums', 'fav_nums', 'image', 'click_nums', 'category', 'tag', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'course_org', 'teacher', 'score', 'total_duration_study',
                     'students_nums', 'fav_nums', 'image', 'click_nums', 'category', 'tag']
    list_filter = ['name', 'desc', 'detail', 'degree', 'course_org', 'teacher', 'score', 'total_duration_study',
                   'students_nums', 'fav_nums', 'image', 'click_nums', 'category', 'tag', 'add_time']


class ChapterAdmin(object):
    list_display = ['course', 'chapter_order', 'chapter_title', 'chapter_desc', 'add_time']
    search_fields = ['course', 'chapter_order', 'chapter_title', 'chapter_desc', 'add_time']
    list_filter = ['course', 'chapter_order', 'chapter_title', 'chapter_desc', 'add_time']


class LessonAdmin(object):
    list_display = ['chapter', 'lesson_order', 'lesson_name', 'lesson_time_duration', 'add_time']
    search_fields = ['chapter', 'lesson_order', 'lesson_name', 'lesson_time_duration']
    list_filter = ['chapter', 'lesson_order', 'lesson_name', 'lesson_time_duration', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'video_source', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'video_source', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Type, TypeAdmin)
