print('Задача 2. Финансовый отчёт')

# Васе пришло очередное задание — автоматизация финансовой отчётности.
# Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически.
# Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода.

# Алгоритм действий в программе:
# 1) Запросить у пользователя четыре числа.
# 2) Отдельно сложить два первых и два вторых.
# module_3_(basic)) Разделить первую сумму на вторую.
# module_4_(if_else)) Вывести результат на экран.

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
num_3 = int(input('Enter third number: '))
num_4 = int(input('Enter fourth number: '))

sum_first_two_quarters_income = num_1 + num_2
sum_second_two_quarters_income = num_3 + num_4
growth_dynamics = sum_first_two_quarters_income / sum_second_two_quarters_income
print('Динамика роста или падения:', growth_dynamics)
