from django.contrib import admin
from .models import Student, ImageStudent

class ImageInline(admin.TabularInline):
    model = ImageStudent
    extra = 0


class ImageAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Student, ImageAdmin)