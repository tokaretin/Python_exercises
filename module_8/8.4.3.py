# Задача 3. Прятки 2
# Пока все прятались, “голя” решил схитрить
# и считать секунды быстрее, чем нужно.
#
# Используя цикл for, напишите программу, которая
# выводит только чётные числа в порядке убывания.
# Нельзя использовать условный оператор.

total_sec = int(input('Сколько сеунда считает "голя"? '))

for sec in range(total_sec, -1, -2):
    print(sec)