#Обычный день на работе.

print('Начался восьмичасовой рабочий день')

tasks = 0
hour = 0
shop = 0
while hour < 6:
    hour += 1
    print(f'Час {hour}-й')
    task = int(input('Сколько задач решит Максим? '))
    tasks += task
    if shop < 1:
        ring = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
        if ring == 1:
            shop = 1
    # else:
    #     continue
print(f'Рабочий день закончился. Всего выполнено задач: {tasks}')
if shop == 1:
    print('Нужно зайти в магазин.')