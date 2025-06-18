from django.contrib import admin

from .models import BlogPost,LandingPage


@admin.register(BlogPost)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")





admin.site.register(LandingPage)