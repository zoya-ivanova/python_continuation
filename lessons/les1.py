# 2. Посчитайте сумму четных элементов, от 1 до n исключая кратные e.
# n = int(input('Введите число n: '))
# e = int(input('Введите число e: '))
# total = 0
# i = 2

# while i <= n:
#     if i % e != 0:
#         total += i
#     i += 2
# print(total)


# 3. Определите високосный ли год. Учтите год Григорянского календаря 1582
# Год является високосным, если его номер кратен 
# 4, но не кратен 100 или если он кратен 400.

# START_YEAR = 1582
# year = int(input('Введите год и проверьте является ли он високосным: '))

# if year < START_YEAR:
#     print('Введите другой год')
# elif (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('Год високосный')
# else:
#     print('Год не является високосным')


# 4. Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 025
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# LIMIT = 0
# LIMIT1 = 10
# LIMIT2 = 100
# LIMIT3 = 1000

# while True:
#     num = int(input(f'Введите число от {LIMIT + 1} до {LIMIT3 - 1} '))
#     if LIMIT < num < LIMIT3:
#         break
#     else:
#         print('Error')
    
# if num < LIMIT1:
#     print(num**2)
# elif num < LIMIT2:
#     print((num // 10) * (num % 10))
# else:
#     print(f'{num % 10}{num // 10 % 10}{num // 100}')


# 5. Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата: Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

# row = int(input('Введите сколько рядов у елки: '))
# for i in range(row):
#     print(f'{" " * (row - i - 1)}{"*" * (2 * (i + 1) - 1)}')


# 6. Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 11):
    for j in range(2, 6):
        print(f'{j} * {i} = {j * i}', end='\t')
    print()
print()

for i in range(2, 11):
    for j in range(6, 10):
        print(f'{j} * {i} = {j * i}', end='\t')
    print()
print()