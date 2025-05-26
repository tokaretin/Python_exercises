from decimal import Decimal, ROUND_HALF_UP

num = 1234.56789

print("1. f-строка (современный способ):")
print(f"{num:.2f}")  # 1234.57

print("\n2. Метод .format():")
print("{:.2f}".format(num))  # 1234.57

print("\n3. Функция round():")
print(round(num, 2))  # 1234.57 (без добавления нулей)

print("\n4. Модуль decimal (высокая точность):")
d = Decimal('1234.56789')
print(d.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))  # 1234.57

print("\n5. Старый стиль форматирования (%.2f):")
print("%.2f" % num)  # 1234.57

print("\n6. f-строка с разделителем тысяч:")
print(f"{num:,.2f}")  # 1,234.57
