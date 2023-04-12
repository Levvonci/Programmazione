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
