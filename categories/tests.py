from django.test import TestCase
from .models import Category
from .utils import get_adjacency_list, create_default_categories, create_sub_categories, check_if_child_exists
import json

class TestUtilsFunctions(TestCase):
    
    def test_create_default_categories(self):
        # Test the create_default_categories function
        create_default_categories()
        self.assertEqual(Category.objects.count(), 2)

    def test_create_sub_categories(self):
        # Test the create_sub_categories function
        category_a = Category.objects.create(name='Category A', parent=None)
        create_sub_categories(category_a.id)
        self.assertEqual(Category.objects.filter(parent_id=category_a.id).count(), 2)

    def test_check_if_child_exists(self):
        # Test the check_if_child_exists function
        category_a = Category.objects.create(name='Category A', parent=None)
        category_b = Category.objects.create(name='Category B', parent=category_a)
        self.assertTrue(check_if_child_exists(category_a.id))
        self.assertFalse(check_if_child_exists(category_b.id))
