# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

string = 'c:/Users/User/.vscode/python_continuation-1/sem_5/task_1.py'

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension
