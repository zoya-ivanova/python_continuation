# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код: from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
EFFORT = 10 

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f'Программа загадала число от {LOWER_LIMIT} до {UPPER_LIMIT} и у тебя {EFFORT} попыток, чтобы угадать его')

for i in range(EFFORT):
    chance = int(input(f'{i + 1}-я попытка! >>>  '))
    if chance == num:
        print(f'Урааа! Вы угадали число {num} с {i + 1}-й попытки')
        break
    elif chance > num:
        print(f'Вы должны ввести число меньше, чем {chance}')
    else:
        print(f'Вы должны ввести число больше, чем {chance}')
if chance != num:
    print(f'Увы... Вы не угадали число {num} за 10 попыток')
    