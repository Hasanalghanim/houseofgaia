from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")