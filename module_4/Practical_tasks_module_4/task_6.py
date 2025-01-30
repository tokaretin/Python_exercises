# Задача 6. Игра в кубики
num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
if num1 == num2:
    n = num1 * num2
    print(f'Игрок платит {n}')
else:
    n = num1 + num2
    print(f'Владелец платит {n}')
print(f'Игра окончена')


