from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Category
from .utils import get_adjacency_list, create_default_categories, create_sub_categories, check_if_child_exists
import json

class CategoryView(View):
    def get(self, request):
        if 'User-Agent' in request.headers and 'PostmanRuntime' in request.headers['User-Agent']:
            # the request is from Postman, so I will return JsonResponse
            return JsonResponse(json.loads(get_adjacency_list()))
        else:
            return render(request, 'home.html', {'data': get_adjacency_list()})

    def post(self, request):
        """
        Creates two sub categories with names '1' and '2' respectively, and the given parent category.
        """
        
        if 'User-Agent' in request.headers and 'PostmanRuntime' in request.headers['User-Agent']:
            # the request is from Postman 
            data = json.loads(request.body)
            parent_id = data.get('id')
        else:
            parent_id = request.POST.get('parent')  
        
        child_exists = check_if_child_exists(parent_id)
        if child_exists:
            return JsonResponse({"status": "already clicked"})

        create_sub_categories(parent_id)
        return JsonResponse({"status": "success"})
        

    def delete(self, request):
        """
        Deletes all categories in the database and creates two default categories with names '1' and '2' respectively, and no parent category.
        """
        try:
            Category.objects.all().delete()
            create_default_categories()
            return JsonResponse({'success': True})
        except:
            return JsonResponse({'success': False})