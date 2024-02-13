# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions

import fractions

frac_1 = [int(x) for x in input('Введите первую дробь вида “a/b”: ').split('/')]
frac_2 = [int(x) for x in input('Введите вторую дробь вида “a/b”: ').split('/')]

summ = ((frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1]) / (frac_1[1] * frac_2[1]))
print(f'Сумма дробей равна: {summ}')

product = ((frac_1[0] * frac_2[0]) / (frac_1[1] * frac_2[1]))
print(f'Прозведение дробей равно: {product}')


# frac1 = fractions.Fraction(1, 3)
# print(frac1)
# frac2 = fractions.Fraction(3, 5)
# print(frac2)

# def process_fractions(frac1, frac2):
#     try:
#         fraction1 = frac1
#         fraction2 = frac2

#         sum_result = fraction1 + fraction2
#         product_result = fraction1 * fraction2

#         return sum_result, product_result

#     except ValueError:
#         return None

# results = process_fractions(frac1, frac2)

# if results is not None:
#     sum_result, product_result = results
#     print(f'Сумма дробей: {sum_result}')
#     print(f'Произведение дробей: {product_result}')
# else:
#     print('Ошибка: Введите корректные дроби.')
