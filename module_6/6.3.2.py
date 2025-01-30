number = int(input('Введите число: '))
summ = 0
while number != 0:
    last_namber = number % 10
    print(last_namber)
    if last_namber == 5:
        print('Мы встетили число 5')
        break
    summ += last_namber
    number //= 10
print(f'Сумма последних чисел = {summ}')
