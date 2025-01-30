#Задача 1. Калькулятор опыта

experience = int(input('Введите колличество опыта: '))
if experience < 0:
    print('Error')
else:
    if experience < 1000:
        level = 1
    elif experience < 2500:
        level = 2
    elif experience < 5000:
        level = 3
    else:
        level = 4
    print(f'Ваш уровень в игре {level}')