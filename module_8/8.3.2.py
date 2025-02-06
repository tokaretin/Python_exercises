# Задача 2. Театр
# Ваню заставили пойти в театр на балет. Ему стало там
# настолько скучно, что он придумал себе очень странное
# развлечение: считать сумму номеров каждого пятого стула
# в рядах.
#
# Напишите программу для вычисления суммы каждого пятого
# числа, лежащего в диапазоне от единицы до N. Использовать
# условный оператор нельзя.
#
# Пример:
#
# Введите число: 21
# Номер стула: 1
# Номер стула: 6
# Номер стула: 11
# Номер стула: 16
# Номер стула: 21
# Сумма: 55

number = int(input('Введите число: '))

# подсчет всех номеров с шагом 5
summ = 0

# шаг 5 от 1 до number + 1
for num_chair in range(1, number + 1, 5):
    # плюсуем номера с шагом 5
    summ += num_chair
    print(f'Номер стула: {num_chair}')

print()
print(f'Сумма номеров: {summ}')