# Задача «Максимальное число»
# Пользователь вводит три числа.
#
# Напишите программу, которая выводит на экран максимальное из этих трёх чисел (все числа разные). Используйте дополнительные переменные, если нужно.
a = int(input('Введите 1-е число: '))
b = int(input('Введите 2-е число: '))
c = int(input('Введите 3-е число: '))
max = a

if b > max:
    max = b
if c > max:
    max = c

print(f'Максимальное число из 3-х: {max}')

# a > b
# b > a
# c > a