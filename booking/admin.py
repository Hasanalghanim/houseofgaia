from django.contrib import admin
from .models import AccessCode

@admin.register(AccessCode)
class AccessCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'expires_at')