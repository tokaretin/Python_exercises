# Задача 1. Космические рейнджеры
# В далеком (а может и не очень) будущем на некоторой планете
# можно купить космический корабль за пол-кредита (CR). Один CR
# это 2200 чатлов. Причем чатлы неделимы и являются всегда целым
# числом. Напишите простую программу-конвертор валют. В программу
# вводится количество чатлов, а она сообщает сколько это CR и сколько
# кораблей можно купить на эту сумму.
#
# Пример 1:
#
# Сколько чатлов? 3150
# Это 1.4318181818181819 CR
# Можно купить кораблей: 2
#
# Пример 2:
# Сколько чатлов? 4400
# Это 2.0 CR
# Можно купить кораблей: 4


money = int(input('Сколько чатлов? '))
CR = 2200  # 1 CR = 2200 чатлов

cr_value = money / CR # Переводим чатлы в CR
spaceship = int(cr_value / 0.5)  # Считаем корабли (1 корабль = 0.5 CR)

print(f'Это {cr_value} CR')
print('Мжоно купить кораблей:', spaceship)