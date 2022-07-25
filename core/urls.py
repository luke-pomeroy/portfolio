from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sendmail', views.send_email, name='sendmail'),
    path('github', views.githb, name = 'githb'),
]

