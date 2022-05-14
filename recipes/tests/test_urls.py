from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):

    def test_recipe_home_urls_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_detail_urls_is_correct(self):
        url = reverse('recipes:recipe_detail', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipes_by_category_urls_is_correct(self):
        url = reverse('recipes:recipes_by_category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')
