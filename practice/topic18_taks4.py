import requests
import string
from bs4 import BeautifulSoup
'''
Создаем локальную копию страницы с которой и будем брать текст лицензии

url = 'https://docs.python.org/3/license.html'
req = requests.get(url)
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

}

src = req.text

with open('index.html', 'w') as file:
    file.write(src)

'''
# находим текст лицензии

with open('index.html') as file:
    scr = file.read()

soup = BeautifulSoup(scr, 'lxml')

license_text = soup.find('pre', class_='literal-block').text

# actually task
"""
Дан текст на некотором языке. Требуется подсчитать сколько раз каждое слово входит в этот текст и вывести десять самых часто употребяемых слов в этом тексте и количество их употреблений.

В качестве примера возьмите файл с текстом лицензионного соглашения Python /usr/share/licenses/python/LICENSE.

Я не нашел такой папки "licenses" у меня Ubuntu и есть только папка "common-licenses" в которой не было лицензии python is None:

По этому пришлось брать лицензию с оф.сайта. Так что слова из десятки у вас скорее всего должны быть другие.
"""
word_counter = {}
words_from_license = license_text.translate(str.maketrans(" "," ",string.punctuation)).lower().split()
for word in words_from_license:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
top_values = sorted(list(word_counter.values()), reverse=True)[:10]
top = []
for word, value in word_counter.items():
    if value in top_values:
        top.append([word, value])
top.sort(key=lambda x: x[1])
string_top = ''
total_positions = len(set(top_values))
flag = True
for n, item in enumerate(top):
    word, value = item
    if [y for x, y in top].count(value) == 2:
        if flag:
            paste = f'разделяет вместе сo словом {top[n][0]}'
            flag = False
    elif [y for x, y in top].count(value) > 2:
        paste = 'разделяет вместе с другими словами с таким же результатом'
    else:
        paste = 'занимает'
    paste2 = 'раз'
    if value%100 > 20 or value%100 < 5:
        if str(value)[-1] in '234':
            paste2 = 'раза'

    string_top += f'{total_positions} место {paste}: слово "{word.capitalize()}" употребившееся {value} {paste2}! \n'
    total_positions -= 1
    flag = True
    if n != len(top)-1 and value == top[n+1][1]:
        total_positions += 1
        flag = False

print(string_top)
