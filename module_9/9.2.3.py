# Задача 3. Дразнилка
# Напишите программу-дразнилку “Купи слона”.
# Она спрашивает у пользователя, как его зовут,
# затем отвечает “%username%, купи слона”. Дальше,
# что бы он ни говорил, она передразнивает:
# Все говорят “...”, а ты купи слона!
#
# Пример:
#
# Как тебя зовут? Дима
#
# Дима, купи слона!
#
# Хорошо, давай куплю
#
# Все говорят Хорошо, давай куплю, а ты купи слона!
#
# ...

username = input('Как тебя зовут? ')
print(f'{username} купи слона!!!')

while True:
    answer = input('')
    print(f'Все говорят, - "{answer}", а ты купи слона!')
