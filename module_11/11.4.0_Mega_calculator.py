import math

user_number = float(input("Введите число: "))
print(f'math.floor \t{math.floor(user_number)}   \t - округляет вниз')
print(f'math.ceil  \t{math.ceil(user_number)}    \t - округляет вверх')
print(f'abs        \t{abs(user_number)} \t - берет модуль числа')
print(f'math.sqrt  \t{math.sqrt(user_number)} \t - извлекает квадратный корень')
print(f'math.exp   \t{math.exp(user_number)} \t - возводит экспоненту в степень, равную числу')
print(f'math.log   \t{math.log(user_number)} \t - считает натуральный логарифм числа')
print(f'math.log2  \t{math.log2(user_number)} \t - считает логарифм числа по основанию 2')
print(f'math.log10 \t{math.log10(user_number)} \t - считает логарифм числа по основанию 10')
print(f'math.sin   \t{math.sin(user_number)} \t - считает синус числа')
print(f'math.cos   \t{math.cos(user_number)} \t - считает косинус числа')
if user_number >= 0:
    print(f'math.factorial \t{math.factorial(int(user_number))} \t - факториал числа')
else:
    print("Факториал отрицательного числа не определен")