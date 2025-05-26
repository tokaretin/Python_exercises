#Задание 1. Дом для семьи

count = 1
for meters in 100,90,95,87,102:
    if meters % 3 == 0:
        print(f'{count} участок {meters} - Подходит ')
    else:
        print(f'{count} участок {meters} - Не подходит ')
    count += 1