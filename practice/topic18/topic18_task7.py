"""
В файле task6/en-ru.txt находятся строки англо-русского словаря в таком формате:

cat - кошка
dog - собака
home - домашняя папка, дом
mouse - мышь, манипулятор мышь
to do - делать, изготавливать
to make - изготавливать

// В задании дан кривой словарь поэтому я его исправил на примеры приведенные в задании, a название его исправил на task7/en-ru.txt    //
import os

os.makedirs('topic18/task7')
os.replace('task6_en--ru.txt', 'topic18/task7/en-ru.txt')
for doc in os.listdir():
    if doc == "topic18" or doc == '.idea':
        continue
    os.replace(doc, 'topic18/'+doc)

Здесь английское слово (выражение) и список русских слов (выражений) разделены двумя табуляциями и минусом: '\t-\t' # в моем словоре ' - '

Требуется создать русско-английский словарь и вывести его в файл task7/ru-en.txt в таком формате:

делать - to do
дом - home
домашняя папка - home
изготавливать - to do, to make
кошка - cat
манипулятор мышь - mouse
мышь - mouse
собака - dog
Порядок строк в выходном файле должен быть словарным с человеческой точки зрения (так называемый лексикографический порядок слов). То есть выходные строки нужно отсортировать.
"""

dict_ru_en = {}
dict_en_ru = {}
with open('task7/en-ru.txt', 'r') as dict:
    for string in dict.read().splitlines():
        split_key_value = string.split(' - ')
        dict_en_ru[split_key_value[0]] = split_key_value[1]
print(dict_en_ru)
while dict_en_ru:
    en, ru = dict_en_ru.popitem()
    for word_ru in ru.split(', '):
        if word_ru in dict_ru_en:
            dict_ru_en[word_ru] += ', ' + en
        else:
            dict_ru_en[word_ru] = en

with open('task7/ru-en.txt', 'w') as dict:
    sort_list = []
    while dict_ru_en:
        key, value = dict_ru_en.popitem()
        sort_list.append(f'{key}\t-\t{value}\n')
    sort_list.sort()
    for i in sort_list:
        dict.write(i)
