a = 'questa è una stringa'
b = "questa è un'altra stringa"
#definisco 2 stringhe   

c = 'uno'
d = 'due'
print(c + " " + d)
#stampo a schermo la concatenazione di 2 stringhe

print(c + "\t" + d)
#stampo a schermo la concatenazione di 2 stringhe tabate

print(c + "\n"  + d)
#stampa a shcermo la concatenazione di 2 stringhe in colonna

print(c + "\n\t" + d)
#stampa a schermo la concatenazione di 2 stringhe in colonna tabate

print(c.upper())
#stampa a schermo tutti i caratteri della stringa in caps

print(c.lower())
#stampa a schermo tutti i caratteri della stringa minuscoli

first_name = 'leonardo'
last_name = 'ascenzi'
full_name = f"{first_name} {last_name}"
print (full_name)
#stampa a schermo l'intero nome utilizzando il caratter f prima della definizione

print(f"Hello, {full_name.title()}!")
#stampa a schermo l'intero nome utilizzando la funzione title()

message = f"Hello, {full_name.title()}! Would you like to learn some python today?"
print(message)
#stampa a schermo questo message

python = 'python.exe'
print(python.removesuffix('.exe'))
#stampa a schermo python senza l'estenzione file
