# -*- coding:utf-8 -*-
__author__ = 'Mr.Robot'
__time__ = '2018/4/22'

from rest_framework import serializers
from .models import LessonUserAsk, LessonAskAnswer, LessonUserComment, UserFavorite, UserMessage, UserCourse


class LessonUserAskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonUserAsk
        fields = "__all__"


class LessonAskAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAskAnswer
        fields = "__all__"


class LessonUserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonUserComment
        fields = "__all__"


class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = "__all__"


class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = "__all__"


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = "__all__"
