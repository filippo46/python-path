# -*- coding: utf-8 -*-
# %%esercizio_1
"""
1. Definite la funzione triangolo(N) che torna una matrice triangolare di N*N/2 elementi, 
   contenente solo la parte in basso a sinistra della matrice dei prodotti (tabelline).
   Il risultato quindi dev'essere una lista di N liste di lunghezza crescente da 1 a N.
   Esempio:
>>> triangolo(4)
[[1],
 [2, 4],
 [3, 6, 9],
 [4, 8, 12, 16]]
"""

# definisco la funzione che con la list comprehension torna direttamente il risultato
def triangolo(N):
    # creo due liste annidate (righe e colonne) che seguono le regole di una matrice triangolare
    return [[X*Y for X in range(1, Y+1)] for Y in range(1, N+1)]

# stampo la prova
print(*triangolo(4), sep = '\n')

# %%esercizio_2
"""
2. Definite la funzione potenze_crescenti(lista) che produce come risultato una lista
   in cui ciascun elemento è ottenuto come la potenza i-esima del corrispondente elemento
   in posizione i della lista passata come argomento.
   Esempio:
>>> potenze_crescenti([2, 3, 4, 5, 6])
[1, 3, 16, 125, 1296]
"""

# definisco la funzione
def potenze_crescenti(basi):
    # e ritorno direttamente la lista che eleva ogni elemento per il suo indice
    return [n**basi.index(n) for n in basi]

# stampo la prova
print(potenze_crescenti([2, 3, 4, 5, 6]))

# %%esercizio_3
"""
3. Definite la funzione non_divisibili(N, divisori) che trova tutti i numeri tra 1 e N (compresi)
   che non sono divisibili per nessuno dei valori presenti nella lista di divisori (interi).
   Esempio:
>>> non_divisibili(10, [2, 3])
[1, 5, 7]
"""

# definisco la funzione
def non_divisibili(N, divisori):
    # che ritorna una lista il cui modulo per ogni divisore è != 0
    return [x for x in range(N+1) if all(x % y != 0 for y in divisori)]

# stampo la prova
print(non_divisibili(10, [2, 3]))

# %%esercizio_4
"""
4.  Definite la funzione doppio_dado() che stampa una successione di estrazioni casuali di due dadi a 6 facce 
    e che conta e torna come risultato quante ne sono state necessarie prima di ottenere un doppio 6.
    Esempio:
>>> doppio_dado()
3 5
2 2
1 6
6 4
3 1
5 4
6 6
7
"""

# importo il modulo random per generare numeri pseudo casuali da 1 a 6
import random

# definisco la funzione
def doppio_dado():
    # definisco le tre variabili base
    lanci = 0
    dado_1 = 0
    dado_2 = 0
    # inizio un ciclo while finché entrambi i dadi non saranno 6
    while dado_1 != 6 or dado_2 != 6:
        lanci += 1
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        print(dado_1, " ", dado_2, end='\n')
    # quando entrambi sono 6 mi fermo
    else:
        print('lanci =', lanci)
        
# prova
doppio_dado()