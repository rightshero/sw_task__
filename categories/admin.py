from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    ordering = ('id',)

admin.site.register(Category, CategoryAdmin)