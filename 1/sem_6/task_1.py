# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from module_task_1 import check_date, check_year


if __name__ == '__main__':
    print(check_date('30.02.2005'))
    print(check_year(2000))
