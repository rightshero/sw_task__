# urls.py
from django.urls import path
from .views import add_categories,get_categories,delete_all



app_name='category'
urlpatterns = [
    path("", get_categories, name="get_categories"),
    path("add/", add_categories, name="add_categories"),
    path('delete-all/', delete_all, name='delete_all'),
]
