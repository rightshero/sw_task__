# Import the necessary modules

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Category
# Create your views here.



def delete_all(request):
    """ this method is used to delete the whole data inside database to reset """
    Category.objects.all().delete()
    return redirect('/')

def create_categories():
    """ this method is used to create the two parent categories ."""
    # Check if categories already exist
    if Category.objects.count() == 0:
    # Create two categories
        category1 = Category.objects.create(title='Category A')
        category2 = Category.objects.create(title='Category B')
        # print(category1,category2)
    

def get_categories(request):
    """ used to fetch the whole data and then render it on the html file , to make sure there is always two parent categories 
    i used a callback function to create the categories of two parent if not exist. """
    
    # Call the function to create categories
    create_categories()

    # # Get all the categories from the database
    categories = Category.objects.all()
    print(categories)

    # Render the template with the categories
    return render(request, 'index.html', {'categories': categories})




    



def add_categories(request):
    
    """used to add new two categories depend on the checked category (parent) """
    
    if request.method == 'POST':
        
        # Get the category values from the POST data
        category_id = request.POST.get('id')
        # Get the title of the parent category using id
        category = Category.objects.get(id=category_id)
        category_title = category.title
        
        is_checked = request.POST.get('is_checked')
        
        print(f'id: {category_id}, is_checked: {is_checked}')
        

        
        
        parent_id = category_id
        parent_level=request.POST.get("parent_level")
            
        if category_title .count('SUB ') == 0  :
            category1 = "SUB " + category_title + '1'
            print(category1)
            category2 = "SUB " + category_title + '2'
            print(category2)
            # Get the parent category from the database
            parent_category = Category.objects.get(id=parent_id)
            # Create two new categories with parent_category as their parent and save them to the database
            new_category1 = Category(title=category1, parent=parent_category,level=parent_level)
            new_category2 = Category(title=category2, parent=parent_category,level=parent_level)
            new_category1.save()
            new_category2.save()
            get_categories(request)
            return JsonResponse({'message': 'success'})
            
            
        else:
            category1  ="SUB " + category_title+ '-1'
            category2  ="SUB " + category_title+ '-2'
            
            # Get the parent category from the database
            parent_category = Category.objects.get(id=parent_id)
            # Create two new categories with parent_category as their parent and save them to the database
            new_category1 = Category(title=category1, parent=parent_category,level=parent_level)
            new_category2 = Category(title=category2, parent=parent_category,level=parent_level)
            new_category1.save()
            new_category2.save()
            get_categories(request)
            return JsonResponse({'message': 'success'})
    else:
        # Return an error response
        return JsonResponse({"status": "error"})










