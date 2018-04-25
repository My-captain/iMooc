# -*- coding: utf-8 -*-
# ==========================================
# @Time    : 2018/3/27 下午8:18
# @Author  : Mr.Robot
# @File    : adminx.py
# ==========================================

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students',
                    'course_nums', 'add_time']
    search_fields = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students',
                     'course_nums']
    list_filter = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students',
                   'course_nums', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'image', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                     'image']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                   'image', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
