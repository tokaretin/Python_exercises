# Задача 2. Таблица суммы
# Напишите программу, которая запрашивает у пользователя
# число N и выводит таблицу суммы для чисел от 0 до N.
#
# Пример:
#   0   1	2	3	4	5
#   1	2	3	4	5	6
#   2	3	4	5	6	7
#   3	4	5	6	7	8
#   4	5	6	7	8	9
#   5	6	7	8	9	10
#

num = int(input('Введите число: '))

for row in range(num + 1):
    for col in range(num + 1):
        print(row + col, end = '\t')
    print('')