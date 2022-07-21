from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('test', views.index, name = 'index'),
    path('', views.githb, name = 'githb')

]

