'''Definizione di tuple'''

dimensioni = (200, 50)
print(dimensioni[0])
print(dimensioni[1])

''''''

for dimensione in dimensioni:
    print(dimensione)

'''Sovrascrivere una tupla'''

print('dimensioni originali:')
for dimensione in dimensioni:
    print(dimensione)

dimensioni = (400, 100)
print('\ndimensioni modificate:')
for dimensione in dimensioni:
    print(dimensione)

'''4.13'''

piatti = ('pizza', 'pasta', 'patate', 'carote', 'mela')

for piatto in piatti:
    print(piatto)

#piatti.append('banana') #ovviamente la tupla è inmodificabile quindi non posso usare l'append

piatti = ('pizza', 'pasta', 'patate', 'fragole', 'panna')

for piatto in piatti:
    print(piatto)

