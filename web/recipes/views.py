from django.shortcuts import render
from . import get_recipes



def home(request):
    return render(request, "recipes/home.html")


def recipe_view(request, label):
    all_recipes_by_ingredient = get_recipes.get_recipes_by_ingredient(label)
    display_recipes = get_recipes.get_fixed_num_recipes(3, all_recipes_by_ingredient)

    context = {
        'recipes':display_recipes
    }
    return render(request, "recipes/recipes_result.html", context)


def about(request):
    return render(request, "recipes/about.html")

def recipe_detail_view(request, meal_id):
    recipe = get_recipes.get_recipe_detail(meal_id)

    context = {
        'recipe':recipe
    }

    print(context)
    return render(request, "recipes/recipe_detail.html", context)
    