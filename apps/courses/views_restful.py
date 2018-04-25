# -*- coding: utf-8 -*-
# ==========================================
# @Time    : 2018/3/26 下午8:24
# @Author  : Mr.Robot
# @File    : views_restful.py
# ==========================================

from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Chapter


class CourseListRest(APIView):
    def get(self, request):
        courses = Course.objects.all()[:10]
        courses_serializer = CourseSerializer(courses, many=True)
        return Response(courses_serializer.data)


class CourseInfoRest(APIView):
    def get(self, request, course_id):
        course = Course.objects.filter(id=course_id)
        course = course[0]
        course_serializer = CourseSerializer(course)
        return Response(course_serializer.data)


class CourseVideoRest(APIView):
    def get(self, request, lesson_id):
        return None
