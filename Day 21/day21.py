import itertools

from Utils.file_reader import read_lines


def part1():
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

    print(allergen_to_ingredient)
    print(all_ingredients)
    allergen_ingredients = list(itertools.chain(*[ingredients for ingredients in allergen_to_ingredient.values()]))
    print(allergen_ingredients)

    no_allergen_list = [ingredient for ingredient in all_ingredients if ingredient not in allergen_ingredients]
    print(no_allergen_list)

    count_map = {}
    for ingredient in no_allergen_list:
        if ingredient in count_map.keys():
            count_map[ingredient] += 1
        else:
            count_map[ingredient] = 1

    print(sum(count_map.values()))


part1()
