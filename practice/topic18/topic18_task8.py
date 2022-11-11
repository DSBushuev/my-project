'''
Упражнение №8*. Синхронизация словарей
Даны два файла словарей: task7/en-ru.txt и task7/ru-en.txt (в формате, описанном в упражнении №6).
Будте готовы к тому что словари очень плохие

en-ru.txt:

home - домашняя папка
mouse - манипулятор мышь
ru-en.txt:

дом - home
мышь - mouse
Требуется синхронизировать и актуализировать их содержимое.

en-ru.txt:

home - домашняя папка, дом
mouse - манипулятор мышь, мышь
ru-en.txt:

дом - home
домашняя папка - home
манипулятор мышь - mouse
мышь - mouse
'''
# создам пакпку task8 для словарей там создам два файла и перекину в них содержимое словарей

import os
'''
import requests
from bs4 import BeautifulSoup


url_en_ru = 'http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task7/en-ru.txt'
url_ru_en = 'http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task7/ru-en.txt'

req_en_ru = requests.get(url_en_ru)
req_ru_en = requests.get(url_ru_en)
src_en_ru = req_en_ru.text
src_ru_en = req_ru_en.text

os.mkdir("task8")
with open("task8/en-ru.txt", 'w') as en_ru:
    en_ru.write(src_en_ru)
with open("task8/ru-en.txt", "w") as ru_en:
    ru_en.write(src_ru_en)

'''
def from_list_in_dict(l:list,d:dict):
    for string_ in l:
        key_, value_ = string_.split("\t-\t")
        d[key_] = value_


def expand_dict(l:list, d:dict):
    for string_ in l:
        key_, values_ = string_.split("\t-\t")
        for value_ in values_.split(','):
            if value_ in d:
                if key_ in d[value_].split(','):
                    continue
                d[value_] += "," + key_
            else:
                d[value_] = key_

def sort_dict(d:dict):
    temp = []
    while d:
        key_, value_ = d.popitem()
        temp.append([key_, value_])
    temp.sort()
    for item in temp:
        key, value_ = item
        d[key] = value_
    return temp




with open("task8/en-ru.txt") as en_ru:
    with open("task8/ru-en.txt") as ru_en:
        list_ru_en = ru_en.read().splitlines()
        list_en_ru = en_ru.read().splitlines()

dict_en_ru = {}
dict_ru_en = {}
from_list_in_dict(list_en_ru, dict_en_ru)
from_list_in_dict(list_ru_en, dict_ru_en)
expand_dict(list_en_ru, dict_ru_en)
expand_dict(list_ru_en, dict_en_ru)
temp_ru = sort_dict(dict_ru_en)
temp_en = sort_dict(dict_en_ru)

with open("task8/en-ru_new.txt", 'w') as en_ru:
    for item in temp_en:
        key_, value_ = item
        en_ru.write(f"{key_}\t-\t{value_}\n")
with open("task8/ru-en_new.txt", "w") as ru_en:
    for item in temp_ru:
        key_, value_ = item
        ru_en.write(f"{key_}\t-\t{value_}\n")




