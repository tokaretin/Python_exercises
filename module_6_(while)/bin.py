start = 1
finish = 100
count = 0

while True:
    n = (start + finish) // 2
    print("Загаданное число от 1 до 100. 1 = равно, 2 - меньше, 3 - больше")
    print(f'Больше {n}')
    answer = int(input('Ваш ответ: '))

    if answer == 3:
        start = n + 1
    elif answer == 2:
        finish = n - 1
    elif answer == 1:
        print(f'Я угадал цифру с {count} попытки')
        break
    count += 1
