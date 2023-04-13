scatola = ['mela', 'pera', 'banana']
for numeri in scatola:
    print(f"{numeri.title()}, sono muffa")
    print(f"che frutto sei?, {numeri.title()}\n")

print('grazie a tutti i frutti per essere stati qui')
#primo for

'''Esercizio 4.1/4.2 (Page 56)'''

pizze = ['margherite', 'funghi', 'patate']

for pizza in pizze:
    print(f"i like {pizza.title()}")

print('i rly like pizze margherita bc its')

print('qui finisce il primo esercizio')
print('qui inizia il secondo esercizio')

'''4.2'''

animali = ['cane', 'gatto', 'topo']
for animale in animali:
    print(animale)
    print(f"The {animale.title()}, is absolutly cute")
print('This pets are absolutly cute')

print('Qui finisce il secondo esercizio')
print('Qui inizia il terzo esercizio')

''''''

numbers = list(range(6))
print(numbers)

''''''

squares = []
for i in range(11):
    squares.append(i**2)

print(squares)

'''compressione della lista'''

squares = [i**2 for i in range(11)]
print(squares)

print('qui inizia esercizio')

'''4.3/4.9 (Page 60)'''

for i in range(1, 21):
    print(i)

''''''

million = []

for i in range(1000001):
    million.append(i)
    
print(million)

''''''

million = []

for i in range(1, 1000001):
    million.append(i)

print(min(million))
print(max(million))
print(sum(million))

''''''

dispari = []

for i in range(1, 21, 2):
    dispari.append(i)
    
print(dispari)


''''''
multipli_3 = []

for i in range(3, 31, 3):
    multipli_3.append(i)

print(multipli_3)

''''''
cubi = []

for i in range(1, 11):
    cubo = i**3
    cubi.append(cubo)

print(cubi)

''''''

cubo_lista = [i**3 for i in range(1, 11)]
print(cubo_lista)

'''slicing'''

player = ['martina', 'mi madre', 'tu padre', 'mi zia', 'franchino']
print(player[1:4])
#slicing dalla prima posizione fino alla quarta

player2 = ['franchino', 'martina', 'nicolò']
print(player2[:2])
#slicing dalla posizione 0 fino a 2 non includendo la seconda

player3 = ['martina', 'damiano', 'nicolò', 'franco', 'davide']
print(player3[2:])
#slicing partendo dalla seconda posizione fino a fine lista 

player4 = ['martina', 'damiano', 'nicolò', 'franco', 'davide']
print(player4[-3:])
#slicing partendo da fine lista e stampa gli ultimi 3 personaggi

player5 = ['martina', 'damiano', 'nicolò', 'franco', 'davide']

print('This is the players of my team')
for player in player5[:3]:
    print(player.title())
#for per stampare i pirmi 3 personaggi

'''copiare liste'''
cibo = ['pizza', 'pasta', 'mandolino']
cibo2 = cibo[:]

print('il mio cibo preferito è:')
print(cibo)

print('\nil cibo preferito dal mio amico è:')
print(cibo2)

'''copiare liste append'''

cibo = ['pizza', 'pasta', 'mandolinio']
cibo2 = cibo[:]

cibo.append('mela')
cibo2.append('banana')

print('il mio cibo preferito è:')
print(cibo)

print(cibo2)

'''4.10/4.12 (Page 69)'''

tavolo = ['bicchiere', 'piatto', 'forchetta', 'coltello']

for utensile in tavolo[:3]:
    print(utensile)
#stampa i primi 3 elementi della lista

for utensile in tavolo[1:3]:
    print(utensile)
#stampa i 2 elementi centrali della lista

for utensile in tavolo[-3:]:
    print(utensile)
#stampa gli ultimi 3 elementi della lista 

''''''

caramelle = ['menta', 'limone', 'banana', 'fragole', 'lamponi']
caramelle2 = caramelle[:]

caramelle.append('arancia')
caramelle2.append('anice')

print('my favourite candyes are:')
for caramella in caramelle[:]:
    print(caramella)

print('my friend favourite candyes are:')
for caramella in caramelle2[:]:
    print(caramella)

''''''



