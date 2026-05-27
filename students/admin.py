from django.contrib import admin
from .models import Student
from django.utils.html import format_html

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cedula', 'career', 'email', 'enrollment_date', 'photo_preview')
    search_fields = ('first_name', 'last_name', 'cedula', 'email', 'career')
    list_filter = ('enrollment_date', 'career')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 45px; height: 45px; border-radius: 50%; object-fit: cover;"/>', obj.photo.url)
        return "No Photo"
    photo_preview.short_description = "Photo"
