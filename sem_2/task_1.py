# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число: '))
result = ''
HEX = 16
print(hex(num))

while num > 0:
    result = str(num % HEX) + result
    num = num // HEX
    print('Ox' + result)

