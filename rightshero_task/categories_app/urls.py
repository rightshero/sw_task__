from django.urls import path
from .views import CategoryViews

urlpatterns = [
    path('', CategoryViews.category_list, name='category_list'),
    path('get_subcategories/', CategoryViews.get_subcategories, name='get_subcategories'),
]