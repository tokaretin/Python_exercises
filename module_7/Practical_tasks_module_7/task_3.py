# Задача 3. Успеваемость в классе
# В классе N человек. Каждый из них получил за урок по информатике
# три, четыре или пять, двоек сегодня не было.
# Что нужно сделать
# Напишите программу, которая получает список оценок — N чисел — и
# выводит на экран сообщение о том, кого сегодня больше: отличников,
# хорошистов или троечников.
# Замечание: можно предположить, что количество отличников, хорошистов
# и троечников различно.
#
# Пример
# Сколько в классе учеников? 5
# Введите оценку ученика: 3
# Введите оценку ученика: 4
# Введите оценку ученика: 4
# Введите оценку ученика: 5
# Введите оценку ученика: 4
#
# Сегодня больше хорошистов!
#
# Что оценивается
# Результат вывода соответствует условию.
# В выводе присутствует сообщение о том, кого больше.
# Для решения используется цикл for, а не встроенные функции или рекурсия.

all_student = int(input('Сколько в классе учеников? '))
five = 0
four = 0
three = 0

for student in range(all_student):
    while True:
        student_grade = int(input(f'Введите оценку {student + 1}-го ученика: '))
        if student_grade < 3 or student_grade > 5:
            print(f'Сегодня были только 3, 4 и 5')
        else:
            if student_grade == 5:
                five += 1
            elif student_grade == 4:
                four += 1
            elif student_grade == 3:
                three += 1
        break

print('')
if five > four and five > three:
    print(f'Сегодня больше отличников!')
elif four > five and four > three:
    print(f'Сегодня больше хорошистов!')
elif three > four and three > five:
    print(f'Сегодня больше троишников!')
elif three == four == five:
    print('Сегодня равное количестов всех оценок')
elif five == four:
    print('Сегодня отличником и хорошистов равное количество')
elif five == three:
    print('Сегодня отличником и троишников равное количество')
elif four == three:
    print('Сегодня хорошистов и троишников равное количество')
