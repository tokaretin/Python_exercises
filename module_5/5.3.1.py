#Задача 1. Сравнение веса грузов
weight_1 = int(input('Введите вес 1-го груза: '))
weight_2 = int(input('Введите вес 2-го груза: '))

if weight_1 > weight_2:
    print(f'Вес 1-го груза больше 2-го')
elif weight_2 > weight_1:
    print(f'Вес 2-го груза больше 1-го')
else:
    print(f'Оба груза весят одинаково')