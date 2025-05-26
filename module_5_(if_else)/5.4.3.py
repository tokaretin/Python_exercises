#Задача 3. Бактерии живут комфортно

temperature = int(input('Введите темератру: '))
left_side = int(input('Введите начало левой границы диапазона: '))
right_side = int(input('Введите конец правой границы диапазона: '))

if temperature < left_side or temperature > right_side:
    print('Внимание!!! Опасность!!! Темперература вышла из диапазона')
else:
    print('Температура в пределах нормы')