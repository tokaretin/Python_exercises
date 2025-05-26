#Игра «Угадай число».
number = int(input('Загадай число от 1 до 5: '))
answer = 0
number_of_attempts = 0


while answer != number:
    answer = int(input('Введите числ: '))
    # Подсчет попыток
    number_of_attempts += 1

    if answer < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз! ')
    elif answer > number:
        print('Число больше, чем нужно. Попробуйте ещё раз! ')
    else:
        break


print(f'Вы угадали! Число попыток: {number_of_attempts}')

