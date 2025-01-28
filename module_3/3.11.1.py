num = int(input('Введите четырехзначное число: '))
first_num = num // 1000    #деление без остатка 1234 // 1000 = 1 Делим число на 1000, чтобы оставить только первую цифру:
print('first_num', first_num)

second_num = (num // 100) % 10  #(1234 // 100) % 10 = 12 % 10 = 2  Делим на 100, а затем берём остаток от деления на 10:
print('second_num', second_num)

third_num = (num // 10) % 10   #(1234 // 10) % 10 = module_3 Делим на 10 и берём остаток от деления на 10:
print('third_num', third_num)

fourth_num = num % 10       #1234 % 10 = module_4  Остаток от деления на 10 даёт последнюю цифру:


print('fourth_num', fourth_num)

print('Цифры числа:', first_num, second_num, third_num, fourth_num)