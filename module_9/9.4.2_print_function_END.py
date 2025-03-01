# Задача 2. Локальная сеть
# У Никиты дома есть много компьютеров, которые он
# хочет подключить к одной локальной сети. Для этого
# ему нужно сгенерировать айпи адрес для каждого
# компьютера. Айпи адрес записывается как 4 числа,
# которые отделяются точкой. Не долго думая, для
# генерации Никита решил использовать арифметическую
# прогрессию, причём первые 3 числа в адресе - это
# члены прогрессии, а последнее число - это её сумма.
#
# Напишите программу, где пользователь вводит:
#
# Первый член прогрессии.
# Разность (шаг, с которым будут увеличиваться числа).
# И в результате получает IP-адрес.

# Запрашиваем у пользователя числа и преобразуем их в int
number = int(input('Введите первый член прогрессии: '))
step = int(input('Введите разность (шаг, с которым будут увеличиваться числа): '))
# Переменная для хранения суммы
summ = 0

# Вывод без перехода на новую строку end=' '
print('\nIP адрес:', end=' ')

# Цикл для генерации первых трех чисел прогрессии range(3)
for count in range(3):
    print(number, end = '.') # Вывод числа и точки
    summ += number # Добавляем число в сумму
    number += step  # Увеличиваем число на шаг

# Вывод суммы в коце строчки IP адрес:
print(summ)
