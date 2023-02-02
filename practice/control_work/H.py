from collections import deque

''' Правитель графландии решил провести реформу административных округов в своем государстве.
А именно ему хочется, чтобы расстояние от города до главного города его округа не превышало
расстояния от данного города до главных городов других округов.
Главные города правитель уже выбрал, вам остается всего лишь разбить остальные города по округам.
Если есть несколько вариантов расстановки - подойдет любой. Если не справитесь, вам отрубят голову.
'''

n, m, *capitals = map(int, input().split()) # кол-во городов, кол-во дорог, областные центры
roads = {}     # словарь дорог {из города А: {в город Б: расстояние между А и Б}

# добавление дорог в словарь дорог
def roads_add(s1, s2, d):
    global roads
    if s1 not in roads:
        roads[s1] = {s2: d}
    else:
        roads[s1][s2] = d


# заполняем словарь дорог
for i in range(m):
    s1, s2, distance = map(int, input().split())
    roads_add(s1, s2, distance)
    roads_add(s2, s1, distance)


cities = {}   # словарь городов {город А: (столица С, расстояние до столицы)}

# нахождение минимальной дистанции от столицы до всех городов.
def search_min_distance(G, start):
    global cities                   # подключаем словарь
    min_distance = {start: 0}       # минимальная дистанция от начальной вершины до самой себя 0
    q = deque()                     #
    q.append(start)                 # положили в очередь стартовую вершину.
    while q:
        vertex = q.popleft()        # забираем из очереди первый элемент и работаем с ним
        if vertex not in G:
            continue
        for v in G[vertex]:         # Сравниваем значение от текущей вершины с значением которое уже было,
            if v not in min_distance or min_distance[v] > min_distance[vertex] + G[vertex][v]:
                min_distance[v] = min_distance[vertex] + G[vertex][v] # если оно меньше меняем и добавляем в очередь
                q.append(v)
    for city in min_distance:       # Заполняем словарь городов расстояниями до обл.центра
        if city not in cities:      # добавляем города если их нет, если расттояние меньше того, что было, обновляем
            cities[city] = (start, min_distance[city])
        else:
            if cities[city][1] > min_distance[city]:
                cities[city] = (start, min_distance[city])

for capital in capitals: # запускаем алгоритм поиска наименьших путей для всех обл.центров выявляем самый ближний записываем в словарь городов
    search_min_distance(roads, capital)
#распечатываем по очереди городов их столицу
print(*[cities[city][0] if city in cities else -1 for city in range(n)], sep="\n")