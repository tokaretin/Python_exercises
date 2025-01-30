#Задача 2. Функция

x = int(input('Введите значение Х: '))

if x > 0:
    y = x - 12
elif x == 0:
    y = 5
elif x < 0:
    y = x**2
print(f'Y = {y}')
