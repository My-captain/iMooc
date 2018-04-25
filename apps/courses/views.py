# -*- coding:utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import View
# 分页器
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite, LessonUserAsk, LessonUserComment

from .models import Course, Chapter, Lesson
from users.models import Banner
from django.db.models.query import QuerySet


# Create your views here.

class IndexView(View):
    def get(self, request):
        banner_courses = Banner.objects.all().order_by("index")

        # 新手入门
        fresh_man_courses = Course.objects.all().filter(degree=u"cj")[:10]

        # 热门课程
        hot_courses = Course.objects.all().order_by("-click_nums")[:10]

        return render(request, "index.html", {
            "banner_courses": banner_courses,
            "fresh_man_courses": fresh_man_courses,
            "hot_courses": hot_courses
        })


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        # 用于展示在右侧热门区域的几门课程(只取前三个)
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 用户选择的排序方式,注意筛选功能一定要写在分页之前
        # 因为分页只是对筛选结果进行合理展示,如果将分页写在前面则会失效
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        # 5是必修给的参数,代表每页显示的数量
        p = Paginator(all_courses, 6, request=request)

        courses = p.page(page)

        return render(request, 'course/course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseInfoView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        chapters = Chapter.objects.filter(course=course)
        lessons = QuerySet(model=Lesson)
        lessons = lessons.filter(chapter=None)
        for chapter_i in chapters:
            lessons = lessons | Lesson.objects.filter(chapter=chapter_i)
        # 每当用户点击该课程自动增加课程点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False
        has_fav_teacher = False

        # 检测该用户是否登录
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=3):
                has_fav_org = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.teacher.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            # 如果不存在,就将其置为空数组
            relate_courses = []

        lesson_user_ask = QuerySet(model=LessonUserAsk).filter(lesson=None)
        for lesson_i in lessons:
            lesson_user_ask = lesson_user_ask | LessonUserAsk.objects.filter(lesson=lesson_i)

        lesson_comments = QuerySet(model=LessonUserComment).filter(lesson=None)
        for lesson_i in lessons:
            lesson_comments = lesson_comments | LessonUserComment.objects.filter(lesson=lesson_i)

        return render(request, "course/course-info.html", {
            "course": course,
            "chapters": chapters,
            "lessons": lessons,
            "lesson_user_ask": lesson_user_ask,
            "lesson_user_comments": lesson_comments,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
            "has_fav_teacher": has_fav_teacher
        })


class CourseVideoView(View):
    """
    课程章节信息
    """
    def get(self, request, lesson_id):
        lesson = Lesson.objects.get(id=int(lesson_id))
        return render(request, "course/course-video.html", {
            "lesson": lesson
        })
