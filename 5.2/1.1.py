import random

list_el = [
    100,
    400,
    500,
    10,
    50,
    "Банан",
    "Клубника",
    "Камень",
    "Морковь",
    "Огурец",
    "Пицца",
]


def random_elements(list_el):
    r1 = random.choice(list_el)
    list_el.remove(r1)
    r2 = random.choice(list_el)
    return r1, r2


print(random_elements(list_el))
