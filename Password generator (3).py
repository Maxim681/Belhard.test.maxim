

import random
from collections import Counter

# Введите колличество символов для пароля
n = n = int(input("Длина пароля (от 1 до 100): "))

# Задаем символы
s = "qwertyuiopasdfghjklzxcvbnm1234567890"

# Из данных символов сделаем кортеж
s_tuple = tuple(s)

# Соеденим рандомные символы для пароля в нужной послежовательности
p = ''.join(random.choice(s_tuple) for i in range(n))

# Множества для уникальных символов

words_numbers1 = set(p)           # обычное множество (можно изменять)
words_numbers2= frozenset(p)     # замороженное множество (неизменяемое)

# Проверяем диапазон
if n < 1 or n > 100:
    print("Ошибка! Длина должна быть от 1 до 100")
    print("Попробуйте ввести заново ")

    n = int(input("Длина пароля (от 1 до 100): "))

    # Спросим продолжить или выйти

    s = "qwertyuiopasdfghjklzxcvbnm1234567890"
    p = ''.join(random.choice(s) for i in range(n))

    if n < 1 or n > 100:
        exit()  # Если ввели цифру мешьше 1,то завершаем программу

print("Пароль:", p)
print("Set (уникальные символы):", words_numbers1)
print("Frozenset:", words_numbers2)
print("Количество раз которое ыстречается это число:", dict(Counter(p)))









