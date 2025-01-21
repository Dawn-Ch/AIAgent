"""
URL configuration for my_ai_agent project.

URL和函数的对应关系都写在这里
常操作，每写一个请求，就要在本文件加东西

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

from app01 import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path('api/', include('tasks.urls')),  # 包含任务 api 路由

    # www.xxx.com/index/  ->  函数
    path('index/', views.index),
    path('api/', include('chat.urls')),   # 所有 chat APP 的 URL 以 /api/ 为前缀

    path('user/list/', views.user_list),
    path('user/add/', views.user_add),

    path('login/', views.login),

    path('orm/', views.orm),

    # path('api/', include('api.urls')),  # 包括 api 的 URL
]
