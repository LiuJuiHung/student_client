#-*-coding:utf-8-*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('group_information/', views.info_page, name='group_information_page'),
]