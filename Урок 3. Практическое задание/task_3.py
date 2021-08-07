"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


import hashlib

s = 'papa'
substring_hash = set()
substring = []

for i in range(len(s)):

    letters = (s[i])

    substring.append(letters)
    substring_hash.add(hashlib.sha256(letters.encode()).hexdigest())

    for j in range(i, len(s) - 1):
        letters = letters + str((s[j + 1]))

        if letters != s:
            substring.append(letters)
            substring_hash.add(hashlib.sha256(letters.encode()).hexdigest())

print(substring_hash)
print(substring)
print(f'Уникальных подстрок - {len(substring_hash)}')
