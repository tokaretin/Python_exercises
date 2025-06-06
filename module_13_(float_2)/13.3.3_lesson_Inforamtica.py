# Задача 3. Урок информатики
# На одном из уроков информатики учитель объяснял тему
# «Числа с плавающей точкой», но несколько учеников никак
# не могли понять, почему эта точка «плавает» и как вообще
# выглядят числа в такой форме. Для наглядности учитель написал
# программу, которая берёт число больше десяти и выводит его
# в формате плавающей точки.
#
# Пользователь вводит положительное число x (x > 10). Напишите
# функцию, которая выводит его в формате плавающей точки, то есть
# x = a*10**b, где 1 ≤ a < 10.
#
# Пример 1:
# Введите число: 16
# Формат плавающей точки: x = 1.6 * 10 ** 1
#
# Пример 2:
# Введите число: 92345
# Формат плавающей точки: x = 9.2345 * 10 ** 4


def to_scientific_notation(x):
    b = 0
    a = float(x)

    # Делим пока не получится a от 1 до 10
    while a >= 10:
        a /= 10
        b += 1

    print(f'Формат плавающей точки: x = {a} * 10 ** {b}')


# Ввод и проверка
while True:
    try:
        number = float(input("Введите положительное число (больше 10): "))
        if number > 10:
            break
        else:
            print("❗ Число должно быть больше 10.")
    except ValueError:
        print("❗ Введите корректное число!")

to_scientific_notation(number)