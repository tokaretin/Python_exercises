#Задача 2. Покупка артефакта в игре
money = int(input('Введите колличество балов: '))

artifact = 55000

if money >= artifact:
    money -= artifact
    if money < 5000:
        money += 1000
        print("Получен бонус")

    print("Артефакт успешно приобретён!")
else:
    print("Недостаточно баллов для покупки")
print(f'На счету {money} балов. Удачной игры!')