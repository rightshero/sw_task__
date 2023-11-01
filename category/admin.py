from django.contrib import admin

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug",'parent','level','created_at','is_checked']

admin.site.register(Category, CategoryAdmin)