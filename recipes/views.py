from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe


# Create your views here.
def home(request):

    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    context = {
        'recipes': recipes
    }

    return render(request, 'recipes/pages/home.html', context)


def recipes_by_category(request, category_id):

    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id).filter(
            is_published=True
        ).order_by('-id')
    )

    context = {
        'recipes': recipes,
        'title': f'{recipes[0].category.name}'
    }

    return render(request, 'recipes/pages/recipes_by_category.html', context)


def recipe(request, id):

    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    context = {
        'recipe': recipe,
        'is_detail_page': True,
    }

    return render(request, 'recipes/pages/recipe-view.html', context)
