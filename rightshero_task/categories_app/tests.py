from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import Category

class TestViews(TestCase):

    # setup required data for testing
    def setUp(self):

        # Client class allows to simulate HTTP requests in test env
        client = Client()
        self.parent_category = Category.objects.create(name='Parent Category', parent=None)

    def test_categories_list_view(self):

        # reverse func generate URLs for named URL pattern
        response = self.client.get(reverse('category_list'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'category_list.html')

    def test_get_subcategories_view(self):

        # simulating a GET request with parameter category_id
        response = self.client.get(reverse('get_subcategories'),{'category_id': self.parent_category.id})

        data = json.loads(response.content.decode('utf-8'))

        expected_data = [{"id": data[0]['id'], "name": "SUB Parent Category-1"}, {"id": data[1]['id'], "name": "SUB Parent Category-2"}]

        self.assertEqual(data, expected_data)
