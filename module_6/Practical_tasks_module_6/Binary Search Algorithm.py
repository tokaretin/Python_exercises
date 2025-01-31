start = 1
finish = 100
count = 1

while True:
    n = (start + finish) // 2 # n = 50
    print('Загаданное число равно, меньше или больше', n)
    answer = int(input('1 - равно, 2 - меньше, 3 - больше '))

    if answer == 2:
        finish = n - 1 # 49
    elif answer == 3:
        start = n + 1
    elif answer == 1:
        print(f'Я угадал! Ура! с {count} попытки. Ваше число {answer}' )
        break
    count += 1

