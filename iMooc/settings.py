"""
Django settings for iMooc project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import pymysql
import rest_framework

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 令django识别apps/目录
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "extral_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+vpn25us)zzgeg&cdjwcxak)4)k7@-p0g7am2+&76^%%md@mus'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自定义app
    'users',
    'courses',
    'orgnization',
    'operation',
    # 第三方app
    'xadmin',
    'pure_pagination',
    'captcha',
    # 'dj_pagination',
    # xadmin依赖
    'crispy_forms',
    # 移动端接口
    'rest_framework'
]

# 配置rest_framework
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}

# 重写django default user model
AUTH_USER_MODEL = 'users.UserProfile'

# pure_pagination配置项
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'dj_pagination.middleware.PaginationMiddleware'
]

ROOT_URLCONF = 'iMooc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iMooc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iMooc',
        'USER': 'root',
        'PASSWORD': 'echo',
        'HOST': '127.0.0.1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 使用本地时间
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Linux以及Mac系统下、此处需要指定本地路径的具体位置,部署上线时需要注意
    r'C:/Users/Mr.Robot/Desktop/workspace/iMooc-master/static/',
    # os.path.join(BASE_DIR, "/static/"),
    # os.path.join(BASE_DIR, "/static/css/"),
)
# print(STATICFILES_DIRS)

# 邮箱服务配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "xxxxxxxx@163.com"
EMAIL_HOST_PASSWORD = "xxxxxxxxxxx"
EMAIL_USE_TLS = False
EMAIL_FROM = "xxxxxxxx@163.com"

# model静态文件处理(课程图片、用户头像等)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
