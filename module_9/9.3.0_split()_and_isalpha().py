string = 'P3242@#$ython - !#@$%это потрясаю456@#$%^&щий язык программирования'

for word in string.split():
    # Убираем лишние символы и цифры
    word_clean = word.strip("P23@#$!#%")
    # .isalpha() проверяет, состоит ли строка только из состоит ли строка только из букв.
    if word_clean.isalpha():
        print(word_clean)

