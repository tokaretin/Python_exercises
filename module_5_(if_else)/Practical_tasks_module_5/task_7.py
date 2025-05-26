#Задача module_7_(for). Почта

hour = int(input('Введите время когда хотите забрать посылку (0 - 23): '))

if 8 > hour < 22 or hour == 14 or hour >= 10 and hour <= 12 or hour >= 18 and hour <= 20:
    print('Посылки получить нельзя')
else:
    print('Посылки получить можно')