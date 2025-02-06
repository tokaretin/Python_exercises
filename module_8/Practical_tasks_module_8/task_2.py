# Задача 2. Долги
# В базе данных «МирПрогБанка» есть список должников.
# Операторам банка дали задание позвонить каждому пятому
# человеку из списка (нумерация начинается с нуля) и
# уточнить, какую сумму каждый из них задолжал банку.
#
# Что нужно сделать
# Напишите программу, которая получает данные о количестве
# должников, а затем спрашивает у каждого пятого
# (начиная с нуля) его долг. В конце выводится общая сумма долгов.
#
# Пример 1
#
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
#
# Общая сумма долга: 8000
#
# Пример 2
#
# Введите количество должников: 10
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
#
# Общая сумма долга: 6000
#
# Что оценивается
# Результат вывода соответствует условию.
# В выводе присутствует общая сумма долга.
# Формат вывода соответствует примеру (не выведены числа без описания).
# Для решения использован цикл for и range c шагом.

number_of_debtors = int(input('Введите количество должников: '))

money_total = 0

# цикл от 0 до 9 итого 10 должников с шагом 5
for number in range(0, number_of_debtors, 5):
    money = int(input(f'Должник с номером {number}. Сколько должны? '))
    money_total += money

print(f'\nОбщая сумма долга: {money_total}')