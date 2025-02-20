# Задание 1. Тестовое задание
# Степан устраивается на работу и должен выполнить тестовое задание:
# проанализировать таблицу, понять, как она строится, и написать
# программу для её вывода на экран.
#
#
# Что нужно сделать
# Помогите Степану реализовать программу.
#
# Подсказка: обращайте внимание на номера столбцов и помните о литерале \t для табуляции.
#
# Что оценивается
# Результат вывода соответствует условию.
# Задача решена с помощью циклов for или while.
# Формат вывода соответствует примеру.

# Введите число: 5
#   0	2	4	6	8	10
#   1	3	5	7	9	11
#   2	4	6	8	10	12
#   3	5	7	9	11	13
#   4	6	8	10	12	14
#   5	7	9	11	13	15

number = int(input('Введите число: '))

for row in range(number + 1):
    for col in range(number + 1):
        # Здесь :2 делает так, чтобы все числа занимали минимум 2 символа
        # (цифры выравниваются по правому краю).
        #s = row + col * 2
        print(f'{row + col * 2:3}', end=' ')
    print('')

print()
for row in range(number + 1):
    for col in range(number + 1):
        # Здесь '\t' делает отступ от последнего символа
        # (цифры выравниваются по левому краю).
        print(f'{row + col * 2}', end='\t')
    print('')

