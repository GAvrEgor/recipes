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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipes_views(request, recipe_name):
    print(recipe_name)
    if recipe_name in DATA:
        dish = DATA[recipe_name]
        print(dish)
        servings = request.GET.get('servings')
        print(servings)
        if servings:
            result = dict()
            for item, value in dish.items():
                new_value = value * int(servings)
                result[item] = new_value
            context = {
                'recipe_name': recipe_name,
                'recipes': result
            }
        else:
            context = {
                'recipe_name': recipe_name,
                'recipes': dish
            }
    else:
        context = None
    return render(request, 'calculator/index.html', context=context)
