spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_list = []
    for food in spicy_foods:
            food_list.append(food.get("name"))
    return food_list


def get_spiciest_foods(spicy_foods):
    spicy_food_list = []
    for food in spicy_foods:
        if food.get("heat_level") > 5:
            spicy_food_list.append(food)
    return spicy_food_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food.get("name") + " (" + food.get("cuisine") + ") | " + "\U0001f336\uFE0F " * food.get("heat_level"))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food_cuisine = []
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            food_cuisine.append(food)
    return food_cuisine

def print_spiciest_foods(spicy_foods):
    most_spicy = sorted(spicy_foods, key=lambda x: x['heat_level'], reverse=True)
    print(most_spicy[0].get("name") + " (" + most_spicy[0].get("cuisine") + ") | " + "\U0001f336\uFE0F " * most_spicy[0].get("heat_level"))


def get_average_heat_level(spicy_foods):
    avg = 0
    tot = 0
    for food in spicy_foods:
        avg += food.get("heat_level")
        tot += 1
    return avg / tot

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods.append(spicy_food)