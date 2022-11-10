"""
Дан словарь en-ru.txt с однозначным соответствием английских и русских слов в таком формате:

cat - кошка

dog - собака

mouse - мышь

house - дом

eats - ест

in - в

too - тоже

Здесь английское и русское слово разделены двумя табуляциями и минусом: '\t-\t'.

В файле input.txt дан текст для перевода, например:

Mouse in house. Cat in house.
Cat eats mouse in dog house.
Dog eats mouse too.
Требуется сделать подстрочный перевод с помощью имеющегося словаря
 и вывести результат в output.txt. Незнакомые словарю слова нужно оставлять в исходном виде.
"""
dict_en_ru = {}
finished_text = ''

with open('en-ru.txt') as dict:
    for words in (dict.read().splitlines()):
        dict_en_ru[words.split('\t-\t')[0]] = words.split('\t-\t')[1]

with open('input.txt') as text_:
    text = text_.read()

for string_en in text.splitlines():
    if string_en == '':
        finished_text += '\n'
        continue
    string_ru =''
    list_word_en = string_en.split()
    for word in list_word_en:
        temp = ''
        word_ = word
        if word[-1] in ',.:;!()&""' or word[-1] in " '' ":
            temp = word[-1]
            word = word[:-1]
            word_ = word
        if word not in dict_en_ru and word.lower() not in dict_en_ru:
            if word[-1] == 's':
                if word[:-1] in dict_en_ru or word[:-1].lower() in dict_en_ru:
                    word = word[:-1]
                    temp = 'и' + temp
        if word.lower() in dict_en_ru:
            word_ = dict_en_ru[word.lower()].capitalize()
        if word in dict_en_ru:
            word_ = dict_en_ru[word]
        string_ru += word_ + temp +' '
    finished_text += string_en + '\n' + string_ru + '\n'
f = open('output.txt', 'w')
f.write(finished_text)
f.close()