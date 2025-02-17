# Задача 2. Цифры больше пяти
# Пользователь вводит последовательность из N чисел.
# Напишите программу, которая подсчитывает общее количество
# цифр больше пяти во всей последовательности.
#
# Пример:
#
# Количество чисел в последовательности: 3
# Введите число: 9
# Введите число: 4
# Введите число: 7
# Результат:  2

# number_of_numbers = int(input('Сколько всего будет чисел? '))
# numeral = int(input('Какую цифру нужно посчитать? '))
#
# while number_of_numbers < 0 and number_of_numbers > 5:
#     print('Цифра должна быть от 0 и до 5 включительно: ')
#
# numeral_count = 0
#
# for num in range(number_of_numbers):
#     number = int(input(f'Введите {num + 1}-е число: '))
#     # Проверяем каждое введенное число
#     while number > 0:
#         if number % 10 == numeral:
#             numeral_count += 1
#         number //= 10
#
# print(f'Цифр {numeral} в последовательности {numeral_count}')


number_of_numbers = int(input('Количество чисел в последовательности: '))
# Задаю константу
FIVE = 5
# Подсчет чисел больше пяти
number_count = 0

for num in range(number_of_numbers):
    number = int(input(f'Введите {num + 1}-е число: '))
    # Проверяем каждое введенное число
    while number > 0:
        if number % 10 >= FIVE: # Если остаток от деления на 10 >= 5
            number_count += 1   # То прибавляем один к number_count
        number //= 10           # Записываем number без последней цифры

print(f'Количество цифр >= 5 Всего: {number_count}')
