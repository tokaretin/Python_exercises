# Задача 3. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются
# не только обычные арифметические действия. Он ничего не хочет делать вручную, поэтому решил
# немного расширить функциональность калькулятора.
#
# Что нужно сделать
# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать
# с числом: вывести сумму его цифр, максимальную или минимальную цифру. Каждое действие оформите
# в виде отдельной функции, а основную программу зациклите.
#
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
#
# Пример 1
#
# Пример 2
#
# Пример 3
#
# Введите число: 984
#
# Введите номер действия:
# 1 - сумма цифр
# 2 - максимальная цифра
# 3 - минимальная цифра: 1
#
# Сумма цифр: 21
#
# Введите число: 546
#
# Введите номер действия:
# 1 - сумма цифр
# 2 - максимальная цифра
# 3 - минимальная цифра: 2
#
# Максимальная цифра: 6
#
# Введите число: 741
#
# Введите номер действия:
# 1 - сумма цифр
# 2 - максимальная цифра
# 3 - минимальная цифра: 3
#
# Минимальная цифра: 1
#
# Рекомендации по выполнению
# Помните, что параметры функции и переменные снаружи могут иметь разные названия.
# При необходимости пересмотрите видео по работе с аргументами либо ознакомьтесь с дополнительными
# источниками информации, например со статьёй «Функции и их аргументы в Python 3».
# Что оценивается
# Результат вывода соответствует условию задачи.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).
# Нельзя использовать переменные, которые созданы вне функции.
# Все числа, необходимые для работы функции, передаются через её параметры (аргументы).

def digital_sum(num):
    total = 0
    while num > 0:
        total += num % 10 # забираем последнюю цифру числа (остаток от деления на 10) и прибавляем ее в total
        num //= 10 # убираем последнюю цифру числа (деление без остатка на 10)
    return total

def max_num(num):
    max_d = 0
    while num > 0:
        digital = num % 10
        if max_d < digital:
            max_d = digital
        num //= 10
    return max_d

def min_num(num):
    min_d = 9 # макимальное число для сравнения
    while num > 0:
        digital = num % 10
        if min_d > digital:
            min_d = digital
        num //= 10
    return min_d

while True:
    choice = int(input('Выберите действие:\n'
            '1 - сумма цифр\n'
            '2 - максимальная цифра\n'
            '3 - минимальная цифра\n'
            'Ваш выбор: '))
    if choice < 1 or choice > 3:
        print('🔖Ошибка. Попробуйте еще раз\n')
        continue
    num = int(input('Введите число: '))
    if choice == 1:
        print(f'Сумма цифр в числе = {digital_sum(num)}\n')
    elif choice == 2:
        print(f'Максимальноя цифра в числе = {max_num(num)}\n')
    elif choice == 3:
        print(f'Минимальноя цифра в числе = {min_num(num)}\n')
