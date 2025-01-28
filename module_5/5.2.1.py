#Задача 1. Координаты
x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x > y:
    print('X больше Y')
elif y > x:
    print('Y больше X')
else:
    print('X и Y равны')