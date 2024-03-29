# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Алексей', 'Александр', 'Аркадий', 'Антонина', 'Алефтина']
salaries = [130000, 115000, 125000, 95000, 105000]
awards = ['9.75%', '8.25%', '10.25%', '9%', '8.50%']
result = {n: s * float(a[:-1]) / 100 for n, s, a in zip(names, salaries, awards)}
print(f'Данные по сотрудникам:\n{names}\n{salaries}\n{awards}')
print(f'Сумма премии:', result)
