# Задача 2. Театр
# В городе планируют построить театр под открытым небом, но для
# начала нужно оценить, сколько сделать рядов, сидений в них и
# каким должно быть расстояние между рядами.
#
# Что нужно сделать
# Напишите программу, которая получает на вход количество рядов,
# сидений и свободных метров между рядами, а затем выводит примерный
# макет театра на экран.
#
# Пример

number_of_rows = int(input('Введите количество рядов: '))
seats = int(input('Введите количество сидений: '))
free_meters = int(input('Введите количество свободных метров между рядами: '))

for n in range(1, number_of_rows + 1):
    print(n, 'ряд\t', seats * '-', free_meters * '*', seats * '-')






