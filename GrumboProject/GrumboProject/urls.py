"""GrumboProject URL Configuration

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
from django.urls import path, include
from . import urls
from grumbo.views import IndexView, GuideView, CommandsView, ClassesView, StatsView, AboutView, BossView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('guide/',GuideView.as_view(),name='guide'),
    path('commands/',CommandsView.as_view(),name='commands'),
    path('classes/',ClassesView.as_view(),name='classes'),
    path('stats/',StatsView.as_view(),name='stats'),
    path('about/',AboutView.as_view(),name='about'),
    path('boss/',BossView.as_view(),name='boss'),
    path('admin/', admin.site.urls),
    path('grumbo/', include('grumbo.urls'))
]
