"""iMooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# 导入Django通用视图，以将index.html快捷地返回
from django.views.generic import TemplateView
# 开发环境下处理静态文件请求
from django.views.static import serve

from django.urls import path, include, re_path
import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyView
from courses.views import IndexView

from rest_framework.documentation import include_docs_urls
from iMooc.settings import MEDIA_ROOT

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path('^$', IndexView.as_view(), name="index"),

    # 课程相关url配置
    re_path(r'^course/', include('courses.urls', namespace="course")),

    re_path('^login/$', LoginView.as_view(), name="login"),
    re_path('^register/$', RegisterView.as_view(), name="register"),
    re_path(r'^captcha/', include('captcha.urls')),
    re_path(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    re_path(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    re_path(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    re_path(r'^modify_pwd/$', ModifyView.as_view(), name="modify_pwd"),

    # 课程机构url配置
    # re_path(r'^org/', include('orgnization.urls', namespace="org")),

    # 配置上传文件的访问处理函数
    re_path(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # path('mobile/course/', include('courses.urls', namespace='courses')),
    # path('mobile/user/', include('users.urls', namespace='users')),
    # path('mobile/orgnization/', include('orgnization.urls', namespace='orgnization')),


    # rest_frame_work
    re_path('docs/', include_docs_urls("iMooc")),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
