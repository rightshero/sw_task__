from django.urls import path
from categories.views import get_subcategories, category_selection_view

urlpatterns = [
    path('get_subcategories/<int:category_id>/', get_subcategories, name='get_subcategories'),
    path('', category_selection_view, name='category_selection_view'),

]
