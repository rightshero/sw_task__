# BUILT-IN IMPORTS
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# CUSTOM MODULES
from .models import Category

# GENERIC IMPORTS
import json
import collections


class HomeView(View):
    def get(self,request):
        # the ordering is to get the most of categories in a way that the parent is always before the child
        nodes = Category.objects.all()
        # normal dict but with default value as empty list []
        getter = collections.defaultdict(list)
        
        if not nodes:
            # initializing the first 2 buttons
            category_1 = Category.objects.create(type='1',parent=None)
            category_2 = Category.objects.create(type='2',parent=None)
            category_1.save()
            category_2.save()
            nodes = [category_1,category_2]
        
        for node in nodes:
                key = str(node.parent_id)
                    
                # * storing childs for each parent
                getter[key].append({"id":node.id,"type":node.type})
                if not getter[str(node.id)]:
                    getter[str(node.id)] = []
        
        
        context = {"data":json.dumps(getter)}
        
        
        # the request is from ajax so i will return json response
        if request.headers.get('Content-Type') == 'application/json':
            return JsonResponse(getter)
        
        return render(request,'sw_task/home.html',context)
    
    def post(self,request):
        data = request.POST
        parent_id = data.get('parent')        
        # *just in case the client sent the request twice (i handled it in the frontend too)
        child = Category.objects.filter(parent_id = parent_id).exists()
        if child:
            return JsonResponse({"status":"already clicked"})
        
        sub_category_1 = Category.objects.create(type='1',parent_id=parent_id)
        sub_category_2 = Category.objects.create(type='2',parent_id=parent_id)
        sub_category_1.save()
        sub_category_2.save()
        
        return JsonResponse({"status":"success"})