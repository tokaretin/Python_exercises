def tax_material(price, tax):
    total = price + (price * tax / 100)
    return total

price = int(input('Цена? '))
tax = float(input('Налог? '))

total_price = tax_material(price, tax)
print(total_price)

new_tax = float(input('Новый налог? '))
total_price = tax_material(total_price, new_tax)
print(total_price)
