from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Category
from .utils import get_adjacency_list, create_default_categories, create_sub_categories, check_if_child_exists, get_categories

class CategoryView(View):
    def get(self, request):
        """
        first time, it will render the home page and then 
        it will return the adjacency list of all categories in the database to construct the tree.
        """
        if request.headers.get('Content-Type') == 'application/json':
            categories = get_categories()
            return JsonResponse(get_adjacency_list(categories))
        else:
            return render(request, 'home.html')



    def post(self, request):
        """
        1- know the current parent
        2- check if it has children already
        3- if it has children, return a message that it has already been clicked
        4- if it doesn't have children, create two sub categories and return them
        """
        parent_id = request.POST.get('parent')
        child_exists = check_if_child_exists(parent_id)
        if child_exists:
            return JsonResponse({"status": "already clicked"})

        subcategories = create_sub_categories(parent_id)
        subcategories = [{"id": subcategory.id, "name": subcategory.name} for subcategory in subcategories]
        
        return JsonResponse({"status": "success", "subcategories": subcategories})



    def delete(self, request):
        """
        Deletes all categories in the database and creates two default categories.
        """
        try:
            Category.objects.all().delete()
            create_default_categories()
            return JsonResponse({'success': True})
        except:
            return JsonResponse({'success': False})