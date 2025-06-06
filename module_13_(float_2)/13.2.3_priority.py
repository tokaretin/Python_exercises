# Задача 3. Приоритет задач
# В одном дата-центре ресурсы распределены так, что сначала
# обрабатываются крупные задачи, а затем уже идут небольшие.
# Каждая из этих задач, по сути, просто огромный поток цифр.
# Ваша задача, как программиста этого центра, написать программу,
# которая поможет определять, какую из задач нужно решать в первую очередь.
#
# Вводится последовательность из N чисел. Нужно определить номер
# числа, у которого больше всего цифр, и вывести на экран
# соответствующее сообщение. Если число отрицательное,
# то считать его за 0. Для подсчёта количества цифр реализуйте функцию numeral_count.
#
# Пример работы программы:
#
# Введите кол-во задач: 4
# Введите число: 6
# Введите число: 14
# Введите число: 1
# Введите число: 13434
#
# Первая задача на обработку: 13434
from subprocess import check_output


def numeral_count(number):
    if number < 0:
        print('Число меньше 0. Зануляем')
        return 0

    count = 0
    if number == 0:
        return 1 # У числа 0 одна цифра

    while number > 0:
        number //= 10
        count += 1

    return count

#Ввод кол-ва задач
total_tasks = int(input('Введите кол-во задач: '))

#Переменные для хранения максимума
max_digits = 0
imortent_task = 0

for i in range(total_tasks):
    number = int(input('Введите число: '))
    digits = numeral_count(number)
    if digits > max_digits:
        max_digits = digits
        imortent_task = number

print(f'Первая задача на обработку: {imortent_task}')
