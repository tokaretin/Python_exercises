#Кубы чисел.

# Напишите программу, которая возводит в третью степень
# каждое число от 1 до N и выводит результат на экран.
#
# Пример
#
# Введите число: 3
# 1 ** 3 = 1
# 2 ** 3 = 8
# 3 ** 3 = 27

number = int(input('Введите число: '))
count = 1
degree = 0

while count <= number:
    degree = count ** 3
    print(f'{count} ** 3 = {degree}')
    count += 1