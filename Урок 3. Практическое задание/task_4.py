"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


import random
import string
import hashlib

cache = {}


def random_string(length=20):
    sequence_for_salt = string.ascii_letters + string.digits
    salt = ''.join(random.sample(sequence_for_salt, length))
    return salt


def caching_web_pages(url):
    if cache.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(random_string().encode() + url.encode()).hexdigest()
        cache[url] = res
        print(cache)


caching_web_pages('https://yandex.ru')
caching_web_pages('https://yandex.ru')
caching_web_pages('https://habr.com/ru')
# random_string()
