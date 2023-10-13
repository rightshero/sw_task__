from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer

def get_categories(request):
    # get the categories from the db
    categories = Category.objects.all()

    return render(request, 'categories/categories.html', {'categories': categories})

@api_view(['GET','POST'])
def categories_list(request):
    if request.method == 'GET':
      # get the categories from the db
      categories = Category.objects.all()
      # serialize the data
      serialized_data = CategorySerializer(categories, many=True).data
      # return response
      return JsonResponse({'categories': serialized_data})
    
    elif request.method == 'POST':
      # get the category from the db
          print('post')
          parent_id = request.data.get('parent_id')
          print(parent_id)

          try:
              parent_category = Category.objects.get(id=parent_id)
          except Category.DoesNotExist:
              return JsonResponse({'message': 'Parent category not found'}, status=404)

          # if it is first sub category
          if parent_category.parent is None:
              last_char = parent_category.name[-1]
              first_subcategory_name = f'SUB Category {last_char}1'
              second_subcategory_name = f'SUB Category {last_char}2'
          
          # else (has parent category)
          else :
              first_subcategory_name = f'SUB {parent_category.name}-1'
              second_subcategory_name = f'SUB {parent_category.name}-2'
              

          # Create the first subcategory
          first_subcategory = Category(name=first_subcategory_name,        parent=parent_category)
          first_subcategory.save()

          # Create the second subcategory
          second_subcategory = Category(name=second_subcategory_name,        parent=parent_category)
          second_subcategory.save()

          # Serialize the two categories
          subcategories = [first_subcategory, second_subcategory]
          serialized_subcategories = CategorySerializer(subcategories, many=True).data

          # Return the response with the two newly created categories
          return JsonResponse({'message': 'Subcategories created successfully',        'subcategories': serialized_subcategories}, status=201)
