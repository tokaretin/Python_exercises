# Задача 1. Возможности компьютера
# В одной IT-компании тестируют возможности различных языков
# программирования, компиляторов и, конечно же, компьютеров.
# Компания дала вам задачу понять, какое самое маленькое возможное
# число можно получить путём постоянного деления числа на 2.
# Изначально число равно единице. Также, помимо самого числа,
# компания просит вывести количество делений. Реализуйте такую программу.

x = 1
divide = float(input('Введите делитель: '))

count = 0
the_smallest_possible_number = x

#Нужно сравнивать с очень маленьким числом — например, 1e-308. Очень маленькое число: 1 × 10⁻³⁰⁸
#Это называется машинный ноль — когда значение уже настолько близко к 0, что меньше него float в Python не хранит.
#while x > 1e-308:	Очень много итераций, не 0
while x != 0:
    #Сохраняю последнее число поделенное на 2
    the_smallest_possible_number = x
    x /= divide
    count += 1
    print(f'Итерация: {count} - {x}')


print(f'\nВсего итераций: {count}')
print(f'Cамое маленькое возможное число постоянного деления числа на 2: {the_smallest_possible_number}')
