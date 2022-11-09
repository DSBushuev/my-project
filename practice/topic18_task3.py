'''

Даны четыре множества:

A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
Найти элементы, принадлежащие множеству E:

E = ((A / B) ^ (C / D)) v ((D / A) ^ (B / C))
'''

A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
E = set( (A.difference(B).intersection(C.difference(D))).union((D.difference(A)).intersection(B.difference(C))))
