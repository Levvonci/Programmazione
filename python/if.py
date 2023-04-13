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

