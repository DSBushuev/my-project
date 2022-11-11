'''Вывести на экран все элементы множества A, которых нет в множестве B.
'''
A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
res = []
for x in A:
    if x not in B:
        res.append(x)
print (*res)