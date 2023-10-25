from django.http import JsonResponse
from django.shortcuts import render
from categories.models import Category
from django.core.exceptions import ObjectDoesNotExist


def category_selection_view(request):
    return render(request, 'categories/categories.html')


def get_subcategories(request, category_id):
    try:
        parent_category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Parent category does not exist'}, status=400)

    subcategories = Category.objects.filter(parent=parent_category)

    if subcategories.exists():
        data = [{'id': sub.id, 'name': sub.name} for sub in subcategories]
    else:
        data = create_subcategories(parent_category)

    return JsonResponse(data, safe=False)


def create_subcategories(parent_category):
    subcategory_names = [f'SUB {parent_category.name} - 1', f'SUB {parent_category.name} - 2']

    created_subcategories = []
    for subcategory_name in subcategory_names:
        subcategory = Category.objects.create(name=subcategory_name, parent=parent_category)
        created_subcategories.append({'id': subcategory.id, 'name': subcategory.name})

    return created_subcategories
