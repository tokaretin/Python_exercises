# Задача 3. Диета
# Саша просыпается когда угодно, но в 23 часа уже точно
# идёт спать. Питается Саша следующим образом: каждые 3
# часа он выпивает литр воды и съедает N калорий. Пить и
# есть он, кстати, начинает сразу как только проснётся.
# Напишите программу, которая считает сколько он выпьет
# литров воды и сколько калорий он съест перед тем как
# пойдёт спать.

wake_up = int(input('Во колько встал Саша? '))

water_total = 0
calories_total = 0

for hour in range (wake_up + 1, 23, 3):
    print(f'hour')
    water = int(input('Сколько Саша выпил литров воды? '))
    water_total += water
    calories = int(input('Сколько Саша съел калорий? '))
    calories_total += calories
    print()

print(f'Выпил за день воды: {water_total}')
print(f'Съел калорий за день: {calories_total}')