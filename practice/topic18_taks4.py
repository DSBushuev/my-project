import requests
import string
from bs4 import BeautifulSoup
'''
Все что в кавычках сделано что бы вытащить текст лицензии с сайта python.org


Создаем локальную копию страницы с которой и будем брать текст лицензии

url = 'https://docs.python.org/3/license.html'
req = requests.get(url)

\\ headers берите сами они будут отличаться. Можно и вообще без них обойтись, это просто рекомендуют что бы за робота не приняли

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

}

src = req.text

with open('index.html', 'w') as file:
    file.write(src)

'''
# находим текст лицензии, у вас он в usr/share/licenses/python/LICENSE у меня в div pre с классом literal-blok т.е. вам надо просто указать путь к нему

with open('index.html') as file:
    scr = file.read()

soup = BeautifulSoup(scr, 'lxml')

license_text = soup.find('pre', class_='literal-block').text

# actually task
"""
Дан текст на некотором языке. Требуется подсчитать сколько раз каждое слово входит в этот текст и вывести десять самых часто употребяемых слов в этом тексте и количество их употреблений.

В качестве примера возьмите файл с текстом лицензионного соглашения Python /usr/share/licenses/python/LICENSE.

Я не нашел такой папки "licenses" у меня Ubuntu и есть только папка "common-licenses" в которой не было лицензии python:

По этому пришлось брать лицензию с оф.сайта. Так что слова из десятки у вас скорее всего должны быть другие.
"""
word_counter = {} # Создаем словарь и вносим в него новые слова со значением 1, если слово не новое добавляем к значению еденицу
words_from_license = license_text.translate(str.maketrans(" "," ",string.punctuation)).lower().split()
for word in words_from_license:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
top_values = sorted(list(word_counter.values()), reverse=True)[:10] #Находим 10 самых больших значений и складываем слова с такими значениями в список топ
top = []
for word, value in word_counter.items():
    if value in top_values:
        top.append([word, value])
top.sort(key=lambda x: x[1])              # Сортируем список по значениям и добавляем к пустой строке
string_top = ''                           # строка к которой прибавляем слова и значения
total_positions = len(set(top_values))    # всего мест
flag = True                               # для правильного построения фразы когда два слова делят одно место
for n, item in enumerate(top):            # цикл по списку топ где n - порядковый номер, word и value слово и значение 
    word, value = item
    if [y for x, y in top].count(value) == 2:                   # Если два слова с одним значением
        if flag:
            paste = f'разделяет вместе сo словом {top[n][0]}'
            flag = False
    elif [y for x, y in top].count(value) > 2:                  # Если слов с одним значением больше двух
        paste = 'разделяет вместе с другими словами с таким же результатом'
    else:
        paste = 'занимает'                                      # Усли такое слово одно
    paste2 = 'раз'
    if value%100 > 20 or value%100 < 5:
        if str(value)[-1] in '234':
            paste2 = 'раза'

    string_top += f'{total_positions} место {paste}: слово "{word.capitalize()}" употребившееся {value} {paste2}! \n'
    total_positions -= 1                                       # место для следущего участника
    flag = True                                                # поднимаем флаг, вдруг их будет два
    if n != len(top)-1 and value == top[n+1][1]:               # спавниваем со следущим словом, если его значение такое же место не меняем флаг не поднимаем
        total_positions += 1
        flag = False

print(string_top)
