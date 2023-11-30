from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['index', 'githb']

    def location(self, item):
        return reverse(f"core:{item}")
