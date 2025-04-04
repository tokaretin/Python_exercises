# Задача 1. Степень нечётного числа
# Выведите третью степень каждого нечётного числа в диапазоне от
# единицы до указанного пользователем числа включительно. Для этого
# используйте шаг внутри функции range.

n = int(input('Введите число: '))
degree = 0

# loop for от 1 до n + 1. С шагом 2 - это значит, что цикл будет идти только по нечетным числам
for number in range(1, n + 1, 2):
    degree = number ** 3
    print(f'{number} ** 3 = {degree}')