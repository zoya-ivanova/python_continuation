# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items


items = {'палатка': 5, 'вода': 3, 'еда': 4, 'вещи': 2, 'аптечка': 1}
max_weight = 12
print(pack_backpack(items, max_weight)) 
