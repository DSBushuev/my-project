"""
Дан список стран и языков на которых говорят в этой стране
в формате <Название Страны> : <язык1> <язык2> <язык3> ... в файле task6_input.txt.
 На ввод задается N - длина списка и список языков. Для каждого языка укажите, в каких странах на нем говорят.

Ввод	        Вывод
3
азербайджанский	Азербайджан
греческий	    Кипр Греция
китайский	    Китай Сингапур
"""

with open('task6_input.txt', 'r') as dict:
    dict_en_ru = {}
    for string in dict.read().splitlines():
        country, lang = string.split(" : ")
        for language in lang.split():
            if language in dict_en_ru:
                dict_en_ru[language].append(country)
            else:
                dict_en_ru[language] = [country]

n = int(input("Введите кол-во языков: "))
languages = []
for i in range(n):
    language = input(f'language {i+1}: ')
    languages.append(language)

for language in languages:
    print(language, *dict_en_ru[language])