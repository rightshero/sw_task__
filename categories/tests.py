from django.test import TestCase
from django.urls import reverse
from categories.models import Category


class CategorySelectionViewTest(TestCase):
    def test_category_selection_view(self):
        response = self.client.get(reverse('category_selection_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/categories.html')


class GetOrCreateSubcategoriesViewTest(TestCase):
    fixtures = ['initial_categories.json']

    def setUp(self):
        self.parent_category = Category.objects.get(id=1)

    def test_get_subcategories_existing_category(self):  # test success for getting subcategories
        response = self.client.get(reverse('get_subcategories', args=[self.parent_category.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)

    def test_get_subcategories_nonexistent_category(self):  # test failure for nonexistent category id
        response = self.client.get(reverse('get_subcategories', args=[999]))
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data['error'], 'Parent category does not exist')


