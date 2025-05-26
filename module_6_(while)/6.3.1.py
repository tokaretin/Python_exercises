temperature = int(input('Сколько на улице градусов? '))
meters = 0
while temperature > 15:
    meters += 20
    temperature -= 2
    if temperature <= 15:
        print('Температура меньше 15 градусов. Тренировка окончена')
        break
    meters += 10
print(f'Kоличество пройденных по стадиону метров {meters}')