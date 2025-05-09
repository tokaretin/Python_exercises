# Задача 2. Компьютерное зрение
# Вы участвуете в разработке робота, который играет в шахматы на
# реальной, физической шахматной доске размером 0.8 х 0.8 метра.
# Робот смотрит камерой на доску и видит расположение фигур в
# вещественных числах с очень высокой точностью.
#
# Напишите программу, в которую вводятся вещественные координаты
# шахматной фигуры, а программа определяет в какой клетке доски
# находится эта фигура. Каждая клетка доски имеет размер 10х10 см
# и целочисленные координаты, состоящие из двух чисел. Например
# левая верхняя клетка имеет целые координаты (0, 0), справа от
# неё клетка (1, 0) а снизу (0, 1). Также обеспечьте контроль ввода:
# нельзя выходить за границы доски.
#
# Пример:
#
# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.149
#
# Фигура находится в клетке (7, 1)
#
# Введите местоположение фигуры
# По горизонтали: 0.833
# По вертикали: -0.132
#
# Клетки с такой координатой не существует

print('Введите местоположение фигуры')
x = float(input('По горизонтали: '))
y = float(input('По вертикали: '))

x_square = int(x * 10)
y_square = int(y * 10)

if 0 <= x_square < 8 and 0 <= y_square < 8:
    print(f'Фигура находится в клетке ({x_square}, {y_square})')
else:
    print('Клетки с такой координатой не существует')

