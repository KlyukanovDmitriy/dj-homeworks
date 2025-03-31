from django.http import HttpResponse

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def get_valid_servings(request):
    """Функция для получения и валидации количества порций."""
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        return 1  # Используем значение по умолчанию
    return servings

def select_recipe(request, name_dish):
    servings = get_valid_servings(request)
    recipe = DATA.get(name_dish, {})
    new_recipe = {}
    for ingridient, count in recipe.items():
        new_count = count * servings
        new_recipe[ingridient] = new_count
    context = {
       'recipe': new_recipe
    }
    return render(request, 'calculator/index.html', context)
