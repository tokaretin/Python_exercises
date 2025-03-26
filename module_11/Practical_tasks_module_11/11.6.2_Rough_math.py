# Задача 2. Грубая математика
# В одном центре математического анализа работал практикант,
# который писал программы для расчёта функций. Однажды он очень
# устал и неправильно понял техническое задание, поэтому функции
# стали грубо рассчитываться.
#
# Его программа работает следующим образом: вводится последовательность
# из N вещественных чисел, при этом положительные числа округляются
# вверх, а отрицательные — вниз.
#
# Что нужно сделать
# Напишите программу, которая выводит натуральный логарифм от числа,
# если оно положительное, и экспоненту в степени числа, если оно отрицательное.
#
# Пример
#
# Введите кол-во чисел: 3
#
# Введите число: 1.3
#
# x = 2 log(x) = 0.6931471805599453
#
# Введите число: -2.1
#
# x = -3 exp(x) = 0.049787068367863944
#
# Введите число: -5.9
#
# x = -6 exp(x) = 0.0024787521766663585
#
# Что оценивается
# Результат вывода соответствует условию, применяются корректные
# функции, округление осуществляется в нужную сторону.
# Формат вывода соответствует примеру.
# Вывод содержит описание результата (выведенные числа сопровождаются
# текстовым описанием).

import math

numbers = int(input('Введите кол-во чисел: '))

for i in range(1, numbers + 1):
    x = float(input('Введите число: '))

    if x < 0:
        x = math.floor(x)
        exp = math.exp(x)
        print(f'x = {x}, exp(x) = {exp}')
    if x > 0:
        x = math.ceil(x)
        log = math.log(x)
        print(f'x = {x}, log(x) = {log}')

'''Второй вариант кода. Он отключен, так как первый более понятен на мой взгяд
import math

numbers = int(input('Введите кол-во чисел: '))

for i in range(1, numbers + 1):
    x = float(input('Введите число: '))

    if x < 0:
        print(f'x = {math.floor(x)}, exp(x) = {math.exp(math.floor(x))}')
    if x > 0:
        print(f'x = {math.ceil(x)}, log(x) = {math.log(math.ceil(x))}')'''