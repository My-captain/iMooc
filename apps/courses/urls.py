# -*- coding: utf-8 -*-
# ==========================================
# @Time    : 2018/3/26 下午8:58
# @Author  : Mr.Robot
# @File    : urls.py
# ==========================================

from django.urls import path, re_path
from courses import views_restful
from courses import views

urlpatterns = [
    # path("list", views_restful.CourseListRest.as_view(), name='course_list'),

    re_path(r'^list/$', views.CourseListView.as_view(), name="course_list"),
    # 课程详情页
    re_path(r'^info/(?P<course_id>\d+)/$', views.CourseInfoView.as_view(), name="course_info"),
    re_path(r'^video/(?P<lesson_id>\d+)/$', views.CourseVideoView.as_view(), name="course_video"),

    # 移动端
    re_path(r'^mobile/list/$', views_restful.CourseListRest.as_view(), name="mobile_course_list"),
    re_path(r'^mobile/info/(?P<course_id>\d+)/$', views_restful.CourseInfoRest.as_view(), name="mobile_course_info"),
    re_path(r'^mobile/video/(?P<lesson_id>\d+)/$', views_restful.CourseVideoRest.as_view(), name="mobile_course_video")
]

app_name = 'courses'
