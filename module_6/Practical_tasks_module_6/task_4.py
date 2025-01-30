#Вклады.
# Вклад в банке: 50
# Проценты: 5
# Порог вклада: 60
#
# 1 год. 50 + 5% = 52
# 2 год. 52 + 5% = 54
# 3 год. 54 + 5% = 56
# 4 год. 56 + 5% = 58
# 5 год. 58 + 5% = 60
#
# Кол-во лет для достижения порога: 5
money = int(input('Сколько вы хотите внести денег? '))
procent = int(input('Под какой проент? '))
finish_money = int(input('Сколько хотите забрать из банка? '))

year = 0 #подсчет лет

while money < finish_money:
    year += 1
    money_procent = int(money + (money * procent / 100))  # Увеличиваем вклад и отбрасываем копейки
    print(f'{year}-й год. {money} + {procent}% = {money_procent} руб.')
    money = money_procent

print(f'Кол-во лет для достижения порога: {year}')
   # print(f'{year}-й год. {money} + {procent}% = {money_proc} руб.')
