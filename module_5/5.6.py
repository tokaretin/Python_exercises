
experience = int(input('Введите очки опыта: '))
# Какое значение переменной level должно быть задано изначально?
if experience < 0:
    print('Ошибка')
else:
    if experience < 1000:
        level = 1
    elif experience < 2500:
        level = 2
    elif experience < 5000:
        level = 3
    else:
        level = 4
    print(f'Уровень персонала: {level}')
