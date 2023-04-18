'''definizione if'''

macchine = ['bmw', 'audi', 'fiat', 'tesla', 'polar']

for macchina in macchine:
    if macchina == 'tesla':
        print(macchina.upper())
    else:
        print(macchina.lower())

'''verificare la disuguaglianza'''

macchina = 'audi'

if macchina != 'tesla':
    print('fa cagare')

'''verifica elemento in lista'''

lista = ['mamma', 'papà', 'figlio']

if 'mamma'in lista:
    print('mamma è nella lista')
else:
    print('mamma non è nella lista')

''''''
banned_user = ['martina', 'nicolò', 'franco', 'damiano']
user = 'davide'

if user not in banned_user:
    print(f"{user.title()}, you are not banned, lets continue you    r game")
else:
    print(f"{user.title()}, you are banned, stop playing right no    w")


'''esercizio random'''

lista1 = ['audi','tesla','bmw','subaru']
lista2 = ['marco','luca','gianni','mario']
lista3 = []

for macchina in lista1:
    print('sono dentro il for')

