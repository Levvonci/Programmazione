computer = ['processore','ram','mb','alimentatore','gpu','ssd']
print(computer)
#stampa a schermo una lista

print(computer[0])
#stampa a schermo l'elemento in posizione 0 nella lista

print(computer[3])
#stampa a schermo l'elemento in posizione 3 nella lista

print(computer[3].title())
#stampa a schermo l'elemento in posizione 3 nella lista come titolo

print(computer[-1])
#stampa a schermo l'ultimo elemento della lista

message = f"My first component of my pc was {computer[0].title()}"
print(message)
#stampa a schermo il messaggio scritto

computer[0] = 'mouse'
print(computer)
#stampa a schermo l'elemento appena sostituito in poszione 0

computer.append('processore')
print(computer)
#stampa a schermo la lista con l'elemento aggiunto in ultima posizione

scatola = []
scatola.append('1')
scatola.append('2')
scatola.append('3')
print(scatola)
#da una lista vuota, aggiungere 3 elementi con l'append e stampare a schermo la lista finale

negozio = ['pane', 'pasta', 'frutta']
negozio.insert(0, 'verdure')
print(negozio)
#con la funzione insert, si specifica la posizione in cui si vuole inserire l'elemento della lista e il nome dell'elemento

casa = ['papà', 'mamma', 'figlio']
del casa[0]
print(casa)
#utilizzare la funzione del per rimuovere l'elemento in questo caso in posizone 0

popped_casa = casa.pop()
print(casa)
print(popped_casa)
#utilizzare la funzione pop per rimuovere l'ultimo elemento in una lista e stampare sia la lista senza l'ultimo elemento che l'elemento poppato

paradiso = ['dio', 'gesù', 'madonna']
paradiso_poppato = paradiso.pop(1)
print(paradiso)
print(paradiso_poppato)
#utilizzare la funzione pop per rimuovere l'elemento in posizione 1 e stampare sia l'elemento poppato che la lista poppata

paradiso.remove('madonna')
print(paradiso)
#utilizzare la funzione per rimuovere l'elemento chiamato 'madonna' dalla lista non specificando la posizione se non si conosce

invitati = ['luca', 'massimo', 'franco']
message1 = f"Hello {invitati[0].title()}, u are invited to my party"
message2 = f"Hello {invitati[1].title()}, u are invited to my party"
message3 = f"Hello {invitati[2].title()}, u are invited to my party"
print(message1, message2, message3)
#scrivere una lista di messaggi a 3 persone per invitarle alla mia festa e stampare a schermo il messaggio

classe = ['marco', 'antonio', 'giuseppe']
classe.append('gianluca')
classe_poppata = classe.pop(2)
del classe[0]
print(classe_poppata)
print(classe)
#un po' di operazioni con le liste


''' Esercizio python crash course 3.4/3.7 (Page 41) '''

invitati_cena = ['marco', 'luca', 'andrea']

messaggio_marco = f"Hello, {invitati_cena[0].title()}, u are invited to my dinner"
messaggio_luca = f"Hello, {invitati_cena[1].title()}, u are invited to my dinner"
messaggio_andrea = f"Hello, {invitati_cena[2].title()}, u are invited to my dinner"

print(messaggio_marco)
print(messaggio_luca)
print(messaggio_andrea)

print('andrea: i cant bro, sry')

del invitati_cena[2]

messaggio_marco_2 = f"{invitati_cena[0].title()} : im still there"
messaggio_luca_2 = f"{invitati_cena[1].title()} : im still there"

print(messaggio_marco_2)
print(messaggio_luca_2)

print('guys, ive found a bigger table, we have 3 more spaces')

invitati_cena.insert(0, 'damiano')
invitati_cena.insert(1, 'franco')
invitati_cena.append('nicolò')

messaggio_damiano = f"Hello, {invitati_cena[0].title()}, u are invited to my dinner"
messaggio_franco = f"Hello, {invitati_cena[1].title()}, u are invited to my dinner"
messaggio_nicolò = f"Hello, {invitati_cena[4].title()}, u are invited to my dinner"

print(messaggio_franco)
print(messaggio_damiano)
print(messaggio_nicolò)

print('sry guys there are only 2 spaces for dinner')

no_cena1 = invitati_cena.pop()
print(f"Sry, {no_cena1}, cya")

no_cena2 = invitati_cena.pop()
print(f"Sry, {no_cena2}, cya")

no_cena3 = invitati_cena.pop()
print(f"Sry, {no_cena3}, cya")

message_franco = f"Hello, {invitati_cena[0].title()}, you still invited"
message_damiano = f"Hello, {invitati_cena[1].title()}, you still invited"

print(messaggio_franco)
print(messaggio_damiano)

del invitati_cena[0]
del invitati_cena[0]
print(invitati_cena)
