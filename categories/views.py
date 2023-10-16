# Import necessary modules and models
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *

# Define your views here.

# View for rendering the main page with top-level categories
def index(request):
    # Retrieve top-level categories from the database
    categories = Category.objects.filter(parent=None)
    return render(request, 'categories.html', {'categories': categories})

# View to create subcategories when a POST request is made
def create_subcategories(request):
    if request.method == 'POST':
        # Get the selected category ID from the POST data
        selected_category_id = request.POST.get('category_id')

        # Find the selected category in the database
        parent_category = Category.objects.get(pk=selected_category_id)

        # Get the current count of subcategories for the selected category
        count = Category.objects.filter(parent=parent_category).count()

        # Create two new subcategories for the selected category
        subcategory1 = Category(name=f'SUB {parent_category.name}-{count + 1}', parent=parent_category, level=parent_category.level + 1)
        subcategory1.save()

        subcategory2 = Category(name=f'SUB {parent_category.name}-{count + 2}', parent=parent_category, level=parent_category.level + 1)
        subcategory2.save()

        return JsonResponse({'message': 'Subcategories created successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})

# View to delete subcategories when a POST request is made
def delete_subcategories(request):
    if request.method == 'POST':
        # Get the ID of the parent category to delete its children
        parent_category_id = request.POST.get('parent_category_id')

        try:
            # Get the parent category from the database
            parent_category = Category.objects.get(pk=parent_category_id)

            # Find and delete its children (subcategories)
            children = Category.objects.filter(parent=parent_category)
            children.delete()

            return JsonResponse({'message': 'Subcategories deleted successfully'})
        except Category.DoesNotExist:
            return JsonResponse({'message': 'Parent category not found'})
    else:
        return JsonResponse({'message': 'Invalid request method'})

# View to retrieve and provide subcategories as JSON when a GET request is made
def get_subcategories(request):
    if request.method == 'GET':
        # Get the ID of the selected category to retrieve its subcategories
        selected_category_id = request.GET.get('category_id')

        # Retrieve subcategories for the selected category from the database
        subcategories = Category.objects.filter(parent_id=selected_category_id)

        # Create an HTML string with checkboxes for the subcategories and include parent information
        subcategory_checkboxes = ''
        for subcategory in subcategories:
            subcategory_checkboxes += '<ul class="subcategory">'
            subcategory_checkboxes += f'<li>'
            subcategory_checkboxes += f'<input type="checkbox" name="category" value="{subcategory.id}" id="sub-{subcategory.id}" />'
            subcategory_checkboxes += f'<label for="sub-{subcategory.id}"> {subcategory.name} </label>'
            subcategory_checkboxes += f'<ul class="subcategory-list">'
            subcategory_checkboxes += f'</ul>'  # Empty container for potential sub-subcategories
            subcategory_checkboxes += f'</li>'
            subcategory_checkboxes += f'</ul>'

        return JsonResponse({'subcategories': subcategory_checkboxes})
    else:
        return JsonResponse({'message': 'Invalid request method'})


        