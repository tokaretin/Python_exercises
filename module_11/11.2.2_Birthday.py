# Задача 2. День рождения
# В честь дня рождения сына отец не придумал ничего лучше,
# кроме как подарить денег. Зато он придумал хоть и странную,
# но интересную формулу, по которой высчитывается сколько он
# подарит: возраст сына умножается на 1.5 и на его
# температуру тела. Остаётся только позавидовать такой фантазии.
#
# Напишите программу, которая запрашивает у пользователя возраст
# (целое число) и температуру тела (вещественное число) и в
# результате выводит сколько отец подарит сыну денег на день рождения.

age = int(input('Сколько лет сыну? '))
temperature = float(input('Какая температура тела у сына? '))
gif_money = round(age * temperature, 2)

print(f'Отец подарит {gif_money} рублей на ДР сыну')

