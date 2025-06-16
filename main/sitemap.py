from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['landingPage', 'about']  # List of view names

    def location(self, item):
        return reverse(item)  # Resolves the view name to the URL