#Задача 1. Датчик погоды
rain = int(input('На улице идёт дождь? '))

if rain == 0:
    print('Дождя нет!')
if rain == 1:
    print('Пошёл дождь. Возьмите зонтик!')
else:
    print('Такой команды нет. Try again')


