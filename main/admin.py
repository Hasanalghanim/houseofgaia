from django.contrib import admin

from .models import AboutPage, AllBlogsPage, BlogPost, LandingPage


@admin.register(BlogPost)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

    





admin.site.register(LandingPage)
admin.site.register(AboutPage)
admin.site.register(AllBlogsPage)
