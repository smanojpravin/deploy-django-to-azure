# from django.conf.urls import url
from django.urls import path
from food import views
from django.urls import include, re_path

urlpatterns = [
    path('', views.index, name='index'),
]
