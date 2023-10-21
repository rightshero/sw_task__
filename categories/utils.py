# utils.py
import json
import collections
from .models import Category


def get_adjacency_list():
    """
    Returns a JSON string representing the adjacency list of all categories in the database to construct the tree.
    why ? ==> so if we refesh the page we will not lose the sub categories made already
    
    The adjacency list is represented as a dictionary where the keys are the parent category IDs
    and the values are lists of dictionaries representing the child categories.
    Each child category dictionary contains the 'id' and 'name' of the category.
    """
    categories = Category.objects.all()
    # in case there are no categories in the database, create two default categories
    if not categories:
        create_default_categories()
        categories = Category.objects.all()

    adjacency_list = collections.defaultdict(lambda: [])

    for category in categories:
        key = str(category.parent_id)
        adjacency_list[key].append({"id": category.id, "name": category.name})
        if not adjacency_list[str(category.id)]:
            adjacency_list[str(category.id)] = []

    return json.dumps(adjacency_list)


def create_default_categories():
    """
    Creates two default categories with names '1' and '2' respectively, and no parent category.
    """
    category_1 = Category.objects.create(name='Category A', parent=None)
    category_2 = Category.objects.create(name='Category B', parent=None)
    category_1.save()
    category_2.save()

def create_sub_categories(parent_id):
    """
    Creates two sub categories with names '1' and '2' respectively, and the given parent category.
    """
    # Generate new sub-category names based on the parent category name
    parent_name = Category.objects.get(id=parent_id).name
    sub_category_name_1 = f'SUB {parent_name}-1' if "SUB" in parent_name else f'SUB {parent_name}1'
    sub_category_name_2 = f'SUB {parent_name}-2' if "SUB" in parent_name else f'SUB {parent_name}2'

    sub_category_1 = Category.objects.create(name=sub_category_name_1, parent_id=parent_id)
    sub_category_2 = Category.objects.create(name=sub_category_name_2, parent_id=parent_id)
    
    sub_category_1.save()
    sub_category_2.save()

def check_if_child_exists(parent_id):
    return Category.objects.filter(parent_id=parent_id).exists()