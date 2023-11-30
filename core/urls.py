from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Static_Sitemap

sitemaps = {
    'static': Static_Sitemap(),
}

app_name = 'core'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sendmail', views.send_email, name='sendmail'),
    path('github', views.githb, name = 'githb'),
]

