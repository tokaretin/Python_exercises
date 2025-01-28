#Задача 3. Маша пошла за сыром
money = int(input('Введите колличество денег: '))
cheese = 60
icecreem = 20

if money >= cheese:
    money -= cheese
    print("На сыр денег хватило")
    if money >= icecreem:
        money -= icecreem
        print("И на мороженое тоже!")
    else:
        print('Денег маловато')
else:
    print("Денег не хватило даже на сыр!")
