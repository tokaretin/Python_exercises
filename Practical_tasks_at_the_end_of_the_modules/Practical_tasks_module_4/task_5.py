#Задача module_5. Модуль числа
modul = int(input('Введите любое число от -n до n: '))
n = 0
if modul >= 0:
    n = modul
    print(f'Модуль числа |{modul}| = {n}')
if modul < 0:
    n = -modul
    print(f'Модуль числа |{modul}| = {n}')