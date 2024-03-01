# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def creat_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(creat_to_dict(name='Кирилл', sername='Нестеров', age=20, weight=70.5,
                     friends=['Иван', 'Алексей', 'Леонид'],
                     training={'колледж': 'техник', 'университет': 'инженер'}))
