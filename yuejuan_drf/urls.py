"""
URL configuration for yuejuan_drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.views.static import serve
from . import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.papers.views import (
    StudentViewSet,
    AnswerViewSet,
    QuestionViewSet,
    PaperViewSet,
)

# from apps.users.views import UserViewSet, UserLoginView
from apps.users.views import UserViewSet

# # 配置papers的url
router = DefaultRouter()
# pages应用url
router.register("students", StudentViewSet, basename="studnets")
router.register("answers", AnswerViewSet, basename="answers")
router.register("questions", QuestionViewSet, basename="questions")
router.register("papers", PaperViewSet, basename="papers")
# user应用url
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls(title="阅卷系统")),
    # api页面的登录功能
    path("api-auth/", include("rest_framework.urls")),
    # 试卷列表页
    path("api/", include(router.urls)),
    # jwt 验证接口
    # 登录接口，验证用户名密码，并产生token
    path("users/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # 刷新token
    path("users/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # 验证token
    path("users/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # 重置密码
    path(
        "api/auth/reset-password/",
        UserViewSet.as_view({"post": "reset_password"}),
        name="reset_password",
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
