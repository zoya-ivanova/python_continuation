# a) Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# b) Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

def is_attacked(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def is_valid(board):
    for i in range(7):
        for j in range(i + 1, 8):
            x1, y1 = board[i]
            x2, y2 = board[j]
            if is_attacked(x1, y1, x2, y2):
                return False
    return True

def generate_random_queens():
    queens = []
    for _ in range(8):
        queens.append((random.randint(1, 8), random.randint(1, 8)))
    return queens

def main():
    successful_boards = 0
    while successful_boards < 4:
        random_queens = generate_random_queens()
        if is_valid(random_queens):
            print("A successful random placement:", random_queens)
            successful_boards += 1

main()