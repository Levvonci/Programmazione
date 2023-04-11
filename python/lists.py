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

