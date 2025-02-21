# Задача 1. Космический корабль
# На космическом корабле каждый пассажир получает уникальный номер
# для идентификации. Эти номера всегда были положительными числами.
# Однако во время полёта произошёл сбой системы, и некоторые номера
# стали отрицательными.
# Для следующего этапа путешествия капитан должен отобрать только тех
# пассажиров, кто имеет положительные и чётные номера.
# Что нужно сделать
# Напишите программу, которая при вводе десяти чисел определяет, сколько
# из них являются одновременно чётными и положительными.
# Пример
# Введите номер человека: 2
# Введите номер человека: 3
# …
# …

# …
# Количество корректных номеров (чётных и положительных): 8
# Что оценивается
# Результат вывода соответствует условию.
# Задача решена с помощью конструкции for.

# переменная для подсчета (чётных и положительных) сколько всего
num_total = 0
# переменная для вывода (чётных и положительных)
correct_nubers = []

# цикл запроса какой номер
for people in range(10):
    num = int(input(f'Введите номер {people + 1}-го человека: '))
    # выполнения условия задачи
    if num > 0 and num % 2 == 0:
        #  Метод .append() добавляет элементы в конец списка,
        #  не изменяя уже существующие
        correct_nubers.append(num)
        # четные и положительные отправляем в переменную для подсчета
        num_total += 1

print(f'Количество корректных номеров (чётных и положительных): {num_total}')
print(f'Итоговый список (чётных и положительных): {correct_nubers}')