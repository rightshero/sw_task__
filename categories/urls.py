# Import necessary modules and views
from django.urls import path
from . import views

# Define URL patterns for the application
urlpatterns = [
    # The main page for categories, typically the index page
    path('', views.index, name='categories'),

    # Endpoint to create subcategories, used with AJAX POST requests
    path('create_subcategories/', views.create_subcategories, name='create_subcategories'),

    # Endpoint to retrieve subcategories, used with AJAX GET requests
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),

    # Endpoint to delete subcategories, used with AJAX POST requests
    path('delete_subcategories/', views.delete_subcategories, name='delete_subcategories'),
]
