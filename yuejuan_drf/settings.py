"""
Django settings for yuejuan_drf project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys
from datetime import timedelta
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 设置apps为根路径
# sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
# 设置extra_apps为根路径
sys.path.insert(0, os.path.join(BASE_DIR, "extra_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d_b666pa98ysis28@w7adz&-xzy2!4^-7b+eafmxgx=ibi9gmm"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "apps.users",
    "apps.papers",
    "corsheaders",
    "rest_framework_simplejwt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "yuejuan_drf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "yuejuan_drf.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 使用mysql数据库
        "NAME": "yuejuan_drf",  # 要连接的数据库
        "USER": "root",  # 链接数据库的用于名
        "PASSWORD": "123456",  # 链接数据库的用于名
        "HOST": "10.165.27.210",  # mysql服务监听的ip
        # "HOST": "192.168.12.9",
        "PORT": 3306,  # mysql服务监听的端口
        "ATOMIC_REQUEST": True,  # 设置为True代表同一个http请求所对应的所有sql都放在一个事务中执行
        # (要么所有都成功，要么所有都失败)，这是全局性的配置，如果要对某个
        # http请求放水（然后自定义事务），可以用non_atomic_requests修饰器
        "OPTIONS": {
            "init_command": "SET storage_engine=INNODB",  # 设置创建表的存储引擎为INNODB
        },
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# 添加媒体路径
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# 替换系统原本的用户model
AUTH_USER_MODEL = "users.UserProfile"


# 通过中间件解决跨域问题
CORS_ALLOWED_ORIGINS = [
    "http://10.165.27.210",
    "http://10.165.27.210:9527",  # 允许的前端域
]

# 解决跨域访问问题
CORS_ORIGIN_WHITELIST = [
    "http://10.165.27.210:9527",
]

# 如果你想允许所有来源，则可以使用
CORS_ALLOW_ALL_ORIGINS = True

# 配置restframework 的验证类
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # 使用rest_framework_simplejwt验证身份
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"  # 默认权限为验证用户
    ],
}

# simple JWT配置
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),  # Access Token的有效期
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # Refresh Token的有效期
}

# 手机验证的正则表达式
REGEX_MOBILE = r"^1[3456789]\d{9}$"

APIKEY = "73966ba57a4453fadcce63a230dc4150"

# url结尾默认不加/
# APPEND_SLASH = False
