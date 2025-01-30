#Задача 6. Новоселье
# Что нужно сделать
# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении, какую купить квартиру, исходя из предпочтений и семейного бюджета,
# они остановились на двух вариантах:
#
# Выбрать квартиру попросторнее (не менее 100 м2), но стоимостью не более 10 млн.
# Немного расширить круг поиска, то есть выбрать квартиру поменьше (от 80 м2), но и стоимостью не более 7 млн.
# Напишите программу, которая получает на вход стоимость квартиры и её площадь и выводит сообщение, подходит ли она.


money = int(input('Введиет стоимость квартиры: '))
flat_meters = int(input('Введите площадь квартиры: '))

if money <= 10000000 and flat_meters >= 100:
    print('Вам подходит квартира попросторнее (не менее 100 м2) и стоимостью не более 10 млн')
elif money <= 7000000 and flat_meters >= 80:
    print('Вам подходит квартира поменьше (от 80 м2) и стоимостью не более 7 млн.')
else:
    print('Вам не походит не один вариант')

