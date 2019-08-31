"""ysu_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from web import views as web_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',web_views.welcome, name='welcome'),
    path('index/',web_views.index, name='index'),
    path('info/',web_views.info, name='info'),
    path('newuser/',web_views.newuser, name='newuser'),
    path('search/',web_views.search, name='search'),
    path('login/',web_views.login, name='login'),
    path('logout/',web_views.logout, name='logout'),
    path('register/',web_views.register, name='register'),
    path('article/<str:id>',web_views.article, name='article'),
    path('publish/',web_views.publish, name='publish'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)