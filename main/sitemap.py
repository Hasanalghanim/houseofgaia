from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogPost
from services.models import Service


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ['landingPage', 'about','allBlogs','appointments']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.created_at 
    




class ServicesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.created_at   