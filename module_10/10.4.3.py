# Задача 3. Лестница чисел
# Пользователь вводит число N. Напишите программу, которая
# по этому числу выводит вот такую лестницу из чисел:
#

number = int(input('Введите число: '))

for row in range(number + 1):
    for col in range(row, number + 1):
        print(col, end='\t')
    print()
