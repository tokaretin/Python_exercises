#Задача 2. Поступление
print('Привет студент')
math = int(input('Введите бал по математике: '))
biologia = int(input('Введите бал по биологии: '))
english = int(input('Введите бал по английскому: '))
sum_ball = math + biologia + english
if sum_ball >= 270:
    print(f'Поздравляю, ты поступил на бюджет! И набрал {sum_ball} балла')
else:
    print(f'Проходной бал 270. К сожалению, ты не прошёл на бюджет. Вы не добрали {270 - sum_ball} баллов')


