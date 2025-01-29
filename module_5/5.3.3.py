#Задача 3. Фальшивомонетчики

coin_1 = int(input('Введите вес 1-ой монеты: '))
coin_2 = int(input('Введите вес 2-ой монеты: '))
coin_3 = int(input('Введите вес 3-ой монеты: '))
if coin_1 == coin_2 == coin_3:
    print('Ошибка: Фальшивой монеты нет')
elif coin_1 == coin_2 and coin_3 < coin_1:
    print('Третья монета легче')
elif coin_1 == coin_3 and coin_2 < coin_1:
    print('Вторая монета легче')
elif coin_2 == coin_3 and coin_1 < coin_2:
    print('Первая монета легче')
else:
    print('Ошибка ввода: Должны быть 2 монеты одинаковык и одна легче')
