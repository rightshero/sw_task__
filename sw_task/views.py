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
        """
            Summary:
                This view returns an adjacency list to construct a tree.

            Args:
                request: A Django HTTP request object.
            Returns:
                dict: An adjacency list (e.g., a dictionary) representing the tree structure. Each key in the dictionary is a node, and the corresponding value is a list of its child nodes. For example:

                {
                    "node1": ["child1", "child2"],
                    "node2": ["child3",child4],
                    "node3": []
                    "node4": []
                }
        """

        # the ordering is to get the most of categories in a way that the parent is always before the child
        nodes = Category.objects.all()
        # normal dict but with default value as empty list []
        adjacency_list = collections.defaultdict(list)
        
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
                adjacency_list[key].append({"id":node.id,"type":node.type})
                if not adjacency_list[str(node.id)]:
                    adjacency_list[str(node.id)] = []
        
        
        context = {"data":json.dumps(adjacency_list)}
        
        
        # the request is from ajax so i will return json response
        if request.headers.get('Content-Type') == 'application/json':
            return JsonResponse(adjacency_list)
        
        return render(request,'sw_task/home.html',context)
    
    def post(self, request):
        """
        Summary:
            Create sub-categories and associate them with a parent category.

        Args:
            request: A Django HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating the status of the operation. Possible responses:

            - {"status": "already clicked"}: If the category already has childs .
            - {"status": "success"}: If sub-categories are successfully created and associated with the parent category.
        """
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
    
     # * so you can try my awesome work endlessly :D (Just kidding)
    def delete(self, request):
        """
        Summary:
            Delete all categories. and start over again.

        Args:
            request: A Django HTTP request object.

        Returns:
            JsonResponse: A JSON response indicating the status of the operation. Possible responses:

            - {"status": "success"}: If all categories are successfully deleted.
            - {"status": "error"}: If an error occurs during the deletion process.
        """

        try:
            Category.objects.all().delete()
        except:
            return JsonResponse({"status": "error"})

        return JsonResponse({"status": "success"})