# -*- coding:utf-8 -*-
__author__ = 'Mr.Robot'
__time__ = '2018/4/22'

from .models import CityDict, CourseOrg, Teacher
from rest_framework import serializers


class CityDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityDict
        fields = "__all__"


class CourseOrgSerializer(serializers.ModelSerializer):
    city = CityDictSerializer()

    class Meta:
        model = CourseOrg
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    org = CourseOrgSerializer()

    class Meta:
        model = Teacher
        fields = "__all__"



