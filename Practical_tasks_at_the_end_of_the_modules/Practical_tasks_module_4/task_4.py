#Задача module_4. Калькулятор скидки
thing_1 = int(input('Сколько стоит 1-я вещь? '))
thing_2 = int(input('Сколько стоит 2-я вещь? '))
thing_3 = int(input('Сколько стоит module_3-я вещь? '))

sum_things = thing_1 + thing_2 + thing_3
if sum_things >= 10000:
    sum_things -= sum_things * 0.1 #скидку 10% (умножить на 10, разделить на 100)
    print(f'На вашу покупку действует скидка 10%\nСумма к оплате {sum_things}')
else:
    print(f'Сумма к оплате {sum_things}')