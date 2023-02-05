def choose_coffee(*cofs):
    global ingredients
    coffee = {'Эспрессо': [1, 0, 0],
              'Капучино': [1, 3, 0],
              'Маккиато': [2, 1, 0],
              'Кофе по - венски': [1, 0, 2],
              'Латте Маккиато': [1, 2, 1],
              'Кон Панна': [1, 0, 1]}
    for name in cofs:
        if coffee[name][0] <= ingredients[0] and coffee[name][1] <= ingredients[1] \
                and coffee[name][2] <= ingredients[2]:
            ingredients[0] -= coffee[name][0]
            ingredients[1] -= coffee[name][1]
            ingredients[2] -= coffee[name][2]
            return name
    return 'К сожалению, не можем предложить Вам напиток'


ingredients = [4, 4, 0]
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
