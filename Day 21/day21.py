import itertools

from Utils.file_reader import read_lines


def get_all_ingredients_and_allergen_map():
    lines = read_lines('Input.txt')

    allergen_to_ingredient = {}
    all_ingredients = list()

    for line in lines:
        contains_str = ' (contains '
        contains_index = line.index(contains_str)
        ingredients = line[:contains_index]
        allergens = line[contains_index + len(contains_str):].replace(',', '').replace(')', '')
        ingredient_set = set(ingredients.split(' '))
        all_ingredients.extend(list(ingredient_set))
        for allergen in allergens.split(' '):
            if allergen in allergen_to_ingredient.keys():
                allergen_to_ingredient[allergen] = set.intersection(ingredient_set, allergen_to_ingredient[allergen])
            else:
                allergen_to_ingredient[allergen] = ingredient_set

    return [all_ingredients, allergen_to_ingredient]


def part1():
    [all_ingredients, allergen_to_ingredient] = get_all_ingredients_and_allergen_map()

    allergen_ingredients = list(itertools.chain(*[ingredients for ingredients in allergen_to_ingredient.values()]))

    no_allergen_list = [ingredient for ingredient in all_ingredients if ingredient not in allergen_ingredients]

    count_map = {}
    for ingredient in no_allergen_list:
        if ingredient in count_map.keys():
            count_map[ingredient] += 1
        else:
            count_map[ingredient] = 1

    return sum(count_map.values())


def part2():
    allergen_to_ingredient = get_all_ingredients_and_allergen_map()[1]

    while len([ingredients for ingredients in allergen_to_ingredient.values() if len(ingredients) > 1]) > 0:
        for key in allergen_to_ingredient.keys():
            if len(allergen_to_ingredient[key]) == 1:
                ingredient_to_remove = list(allergen_to_ingredient[key])[0]
                for other_key in allergen_to_ingredient.keys():
                    if other_key != key and ingredient_to_remove in allergen_to_ingredient[other_key]:
                        allergen_to_ingredient[other_key].remove(ingredient_to_remove)

    allergen_list = list(allergen_to_ingredient.keys())
    allergen_list.sort()

    return ','.join([list(allergen_to_ingredient[allergen])[0] for allergen in allergen_list])


print(part1())
print(part2())
