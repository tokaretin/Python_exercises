text = "Enumerate в Python"
for index, symbol in enumerate(text):
    print("Символ", symbol, "находится на", index, "позиции в тексте")

print()
# Чтобы считать символы в привычном нам формате,
# начиная с единицы можно использовать параметр start
for index, symbol in enumerate(text, start=1):
    print("Символ", symbol, "находится на", index, "позиции в тексте")