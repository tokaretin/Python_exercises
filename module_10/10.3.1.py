# Задача 1. Врата
# Напишите программу, которая выводит в консоль «врата»,
# состоящие из тире, вертикальных линий и пробелов. Поле
# состоит из 20 строк и 30 столбцов (но не стесняйтесь пробовать
# и другие размеры).
from html.parser import endendtag

row_number = int(input('Введите высоту ворот: '))
col_number = int(input('Введите ширину ворот: '))

for row in range(row_number):
    for col in range(col_number):
        if row == 0:
            print('-', end='')
        elif col == 0 or col == col_number - 1:
            print('|', end='')
        else:
            print(' ', end='')
    print()
