
from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        template = 'recipes/pages/home.html'
        self.assertTemplateUsed(response, template)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8')
        )

    def test_recipe_template_loads_recipe(self):
        self.make_recipe(author_data={
            'first_name': "Joãozinho"
        })
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertEqual(len(context_recipes), 1)

    def test_recipes_by_category_returns_404_if_no_found_recipes(self):
        response = self.client.get(
            reverse('recipes:recipes_by_category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe_detail', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_found_recipe(self):
        response = self.client.get(
            reverse('recipes:recipe_detail', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_by_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipes_by_category',
                               kwargs={'category_id': 1}))
        self.assertIs(view.func, views.recipes_by_category)
