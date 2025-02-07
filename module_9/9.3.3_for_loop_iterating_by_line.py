# Задача 3.
# Мы входим в команду разработки нового текстового редактора
# и нам поручили разработать для него подсчёт нужного символа
# в тексте, а именно - буквы Ы. Причём отдельно с верхним
# регистром и отдельно с нижним.
#
# Напишите программу, которая считает количество больших
# и количество маленьких букв Ы в тексте и выводит ответ на экран.
#
# Пример:
#
# Введите текст: Прыг скок
#
# Больших букв Ы: 0
#
# Маленьких букв Ы: 1

text = input('Введите текст: ')
# symbol_big = input('Введите большую букву: ')
# symbol_small = input('Введите маленькую букву: ')

symbol_big = 'Ы'
symbol_small = 'ы'

symbol_big_count = 0
symbol_small_count = 0

for symbol in text:
    if symbol == symbol_big:
        symbol_big_count += 1
    if symbol == symbol_small:
        symbol_small_count += 1

print()
print(f'Больших букв {symbol_big} = {symbol_big_count}')
print(f'Маленьких букв {symbol_small} = {symbol_small_count}')

