#Задача 8. Максимальное число (по желанию)
num1 = int(input('Введите 1-е число: '))
num2 = int(input('Введите 2-е число: '))
num3 = int(input('Введите module_3-е число: '))

max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3

print(f'Максимальное число = {max}')
