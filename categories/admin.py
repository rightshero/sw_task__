from django.contrib import admin
from django.core.management import call_command
from categories.models import Category

call_command('loaddata', 'initial_categories.json')
admin.site.register(Category)
