number = int(input('Введите число: '))

prime = True

for divider in range(2, number):
    if number % divider == 0:
        prime = False
        break

if prime:
    print('Число простое')
else:
    print('Число составное')

