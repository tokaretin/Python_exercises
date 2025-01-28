print('Задача 3. Угадай число')
print("Добро пожаловать в игру «Угадай число»!")
print("Настя загадывает число. Дима, не подглядывай!")
nastya_number = int(input("Введите число: "))
dima_number = int(input("Введите число: "))

if dima_number == nastya_number:
    print("Ура! Угадал!")
else:
    print("Нет, это не то, что я загадала.")