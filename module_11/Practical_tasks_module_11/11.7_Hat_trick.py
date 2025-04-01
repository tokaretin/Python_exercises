# Задача 1. Ход конём
# В рамках разработки шахматного ИИ стоит новая задача: по заданным вещественным
# координатам коня и точки программа должна определить, может ли конь ходить
# в эту точку. Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.
#
# Пример работы программы
#
# Введите местоположение коня:
#
# 0.071
#
# 0.118
#
# Введите местоположение точки на доске:
#
# 0.213
#
# 0.068
#
# Конь в клетке (0, 1). Точка в клетке (2, 0).
#
# Да, конь может ходить в эту точку.
#
# Когда будете готовы, нажмите кнопку ниже, чтобы посмотреть решение задачи.

print('Введите местоположение коня: ')
x_horse = float(input('По гаризонтали: '))
y_horse = float(input('По вертикали: '))

print('Введите местоположение точки на доске: ')
x_point = float(input('По гаризонтали: '))
y_point = float(input('По вертикали: '))

# Определяем номер клетки (каждая клетка делится на 10)
x_horse = int(x_horse * 10)
y_horse = int(y_horse * 10)
x_point = int(x_point * 10)
y_point = int(y_point * 10)

print(f'({x_horse}, {y_horse})')
print(f'({x_point}, {y_point})')

if 0 <= sqr_x1 < 8 or 0 <= sqr_y1 < 8:
    print(f'Конь находится в клетке {sqr_x}, {sqr_y}')
    print(f'Будет ходить в клетку {sqr_x1}, {sqr_y1}')
else:
    print('Клетки с такой координатой не существует')

if