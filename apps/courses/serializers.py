from rest_framework import serializers
from .models import Course, Type, Chapter, Lesson
from orgnization.serializers import CourseOrgSerializer, TeacherSerializer
from operation.models import LessonUserAsk, LessonAskAnswer


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class LessonAskAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAskAnswer
        fields = "__all__"


class LessonUserAskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonUserAsk
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ('id', 'chapter_order', 'chapter_title', 'chapter_desc', 'lessons')


class CourseSerializer(serializers.ModelSerializer):
    course_org = CourseOrgSerializer()
    teacher = TeacherSerializer()
    type = TeacherSerializer()
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Course
        fields = ('name', 'desc', 'detail', 'degree', 'type', 'price', 'course_org', 'teacher', 'score',
                  'total_duration_study', 'students_nums', 'fav_nums', 'image', 'click_nums', 'category', 'tag',
                  'add_time', 'chapters')
