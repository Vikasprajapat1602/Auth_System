from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_draft', 'created_at')
    list_filter = ('category', 'is_draft', 'created_at')
    search_fields = ('title', 'summary', 'content')
