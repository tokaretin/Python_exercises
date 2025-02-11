# Задача 4. Великий и могучий
# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Ему особенно понравилась книга «Преступление и наказание». Паоло решил найти
# самое длинное слово в этой книге, чтобы сравнить его с аналогом на своём языке.
#
# Что нужно сделать
# Напишите программу, которая получает на вход текст
# и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
#
# Пример
#
# Введите текст: Меня зовут Пётр.
# Самое длинное слово, букв: 5.
#
# Введите текст: Меня зовут Василий
# Самое длинное слово, 7 букв
#
# Рекомендации по выполнению
# При помощи функции print убедитесь, что счётчики обнуляются в нужный момент.
# Помните, что не все условия можно собирать в один условный блок.
# Некоторые из них должны срабатывать независимо друг от друга.

text = input('Введите текст: ')

# начальное первое слово
word = 0
# самое длинное слово
max_symbol_in_word = word

# идем по тексту до каждого пробела
for symbol in text:
    if symbol == " ": # если встречается пробел
        if word > max_symbol_in_word: # елси новое слово длиньше,
            max_symbol_in_word = word # то записываем его в max_symbol_in_word
        word = 0 # то обнуляем переменную word
    else: # если нет пробела
        word += 1  # то считаем дальше символы в слове

# последняя проверка на последнее слово в предложении, если после него не стоит пробел
if word > max_symbol_in_word:
    max_symbol_in_word = word

print(f"Самое длинное слово, {max_symbol_in_word} букв")