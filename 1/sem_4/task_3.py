# 1. Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

# 2. Разбейте на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def main():
    balance = 0
    count = 0
    register = []
    print('Добро пожаловать в банкомат!')
    while True:
        while True:
            act = input('Выберите действие:\n 1 - пополнить \n 2 - снять \n 3 - вывести историю операций \n 4 - выйти ')
            if act not in ("1", "2", "3", "4"):
                print('Неверный ввод')
            else:
                break
        match act:
            case "1":
                balance, count, register = add_money(balance, count, register)
                print(f'Ваш баланс {balance}')
                print(f'История операций {register[::-1]}')
            case "2":
                balance, count, register = get_money(balance, count, register)
                print(f'Ваш баланс {balance}')
                print(f'История операций {register[::-1]}')
            case "3":
                print(register)
                break
            case "4":
                print(f'Ваш баланс {balance}')
                print(f'История операций {register[::-1]}')
                print('До свидания!')
                break

def add_money(balance, count, register):
    if balance > 5_000_000:
        register.append(-balance * 0.1)
        balance *= 0.9
    while True:
        try:
            summ = int(input('Введите сумму пополнения, кратную 50: '))
        except:
            ex = input('Хотите выйти в меню?\n')
            if ex.lower() == 'да':
                return balance, count, register
            else:
                continue
        if summ % 50 == 0:
            break
    balance += summ
    count += 1
    if count % 3 == 0:
        register.append(-balance * 0.03)
        balance *= 1.03
    return balance, count, register

def get_money(balance, count, register):
    if balance > 5_000_000:
        register.append(-balance * 0.1)
        balance *= 0.9
    while True:
        try:
            summ = int(input('Введите сумму снятия, кратную 50: '))
        except:
            ex = input('Хотите выйти в меню?\n')
            if ex.lower() == 'да':
                return balance, count, register
            else:
                continue
        if summ % 50 == 0:
            perc = summ * 0.015
            if perc < 30:
                perc = 30
            elif perc > 600:
                perc = 600
            if summ + perc > balance:
                print('Недостаточно средств!')
                continue
            else:
                break
    balance -= (summ + perc)
    count += 1
    register.append(-(summ + perc))
    if count % 3 == 0:
        register.append(balance * 0.03)
        balance *= 1.03
    return balance, count, register

if __name__ == '__main__':
    main()
