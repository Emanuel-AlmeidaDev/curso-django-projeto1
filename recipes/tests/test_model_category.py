from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.category = self.make_category(
            name="Category Testing"
        )
        return super().setUp()

    def test_category_name_max_length(self):
        max_length_needed = 65
        self.category.name = 'A' * (max_length_needed + 1)
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_category_string_representation(self):
        needed = 'Category Testing'
        self.assertEqual(
            str(self.category), needed,
            msg='Category string representation must be '
            f'"{needed}" but "{str(self.category)}"'
        )
