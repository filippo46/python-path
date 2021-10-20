# -*- coding: utf-8 -*-

# %%esercizio_1
"""
1. occ(lst, v) ritorna una lista contenente gli indici delle occorrenze di v nella lista lst . 
   Esempi, sia	lst = ['red','blue','red','gray','yellow','red']
	occ(lst, 'red')		ritorna [0,2,5]
	occ(lst, 'green')	ritorna []
"""

# definisco la funzione come richiesto
def occ(lst, v):
    # imposto la lista di output
    risultato = []
    # per ogni elemento di lst ottengo l'index con enumerate
    for i, colore in enumerate(lst):
        # controllo se uguale a v
        if colore == v:
            # se vero, aggiungo l'indice a risultato
            risultato.append(i)
    # ritorno risultato
    return risultato

# imposto lst di prova
lst = ['red','blue','red','gray','yellow','red']

# stampo le prove
print(occ(lst, 'red'))
print(occ(lst, 'green'))

# %%esercizio_1_avanzato
"""
Con list comprehension
"""

# definisco la funzione come richiesto
def occ(lst, v):
    # ritorno direttamente la lista risultato
    return [i for i, colore in enumerate(lst) if colore == v]

# imposto lst di prova
lst = ['red','blue','red','gray','yellow','red']

# stampo le prove
print(occ(lst, 'red'))
print(occ(lst, 'green'))

# %%esercizio_2
"""
2. rep(lst, k) ritorna una lista, senza ripetizioni, che contiene i valori che nella lista lst occorrono
   almeno k volte. 
   Esempi, sia lst = [1,2,1,5,3,4,2,1,3,5,6]

	rep(lst, 2)	ritorna [1,2,5,3]
	rep(lst, 3)	ritorna [1]
	rep(lst, 4)	ritorna []
"""

# definisco la funzione come richiesto
def rep(lst, k):
   # imposto la lista di output
   risultato = []
   # per ogni elemento di lst
   for i in lst:
       # se presente >= K volte e non è già in risultato, lo aggiungo
       if lst.count(i) >= k and i not in risultato:
           risultato.append(i)
   # ritorno risultato
   return risultato

# imposto lst di prova
lst = [1,2,1,5,3,4,2,1,3,5,6]

# stampo le prove
print(rep(lst, 2))
print(rep(lst, 3))
print(rep(lst, 4))

# %%esercizio_3
"""
3. lastfirst(lst) presa in input una lista lst di parole, ritorna la prima parola che inizia con un
   carattere diverso dall'ultimo carattere della parola precedente, se non c'è ritorna None . 
   Esempi
	lastfirst(['sole','elmo','orco','alba','asta'])		ritorna 'alba'
	lastfirst(['sky','you','use','ear','right'])		ritorna None
"""

# definisco la funzione come richiesto
def lastfirst(lst):
    # imposto le variabili e le liste d'appoggio
    first_word = ''
    second_word = ''
    lst_first = []
    lst_second = []
    # scandisco la lista
    for i in range(0, len(lst)-1):
        # assegno l'n-sima e la n-sima +1 paroa alle rispettive variabili
        # e ne ottengo le liste di caratteri
        first_word = str(lst[i])
        second_word = str(lst[i+1])
        lst_first = list(first_word)
        lst_second = list(second_word)
        # se l'ultima lettera della parola n è diversa dalla prima della parola n+1
        # abbiamo il risultato
        if lst_first[-1] != lst_second[0]:
            risultato = second_word
            return risultato
        # se i non è l'ultima parola, continua
        elif i != len(lst)-1:
            continue
        # altrimenti ritorno none
        else:
            return None
        
# stampo le prove
print(lastfirst(['sole','elmo','orco','alba','asta']))
print(lastfirst(['sky','you','use','ear','right']))

# %%esercizio_3_avanzato
"""
Ottimizzata
"""

# definisco la funzione come richiesto
def lastfirst(lst):
    # scandisco a partire dalla seconda parola (così evito il controllo alla fine)
    for i in range(1, len(lst)):
        # assegno le parole a due variabili
        prev_word = lst[i-1]
        word = lst[i]
        # confronto le lettere
        if prev_word[-1] != word[0]:
            # ritorno la parola
            return word
    # se il ciclo finisce, ritorno None
    return None

# stampo le prove
print(lastfirst(['sole','elmo','orco','alba','asta']))
print(lastfirst(['sky','you','use','ear','right']))

# %%esercizio_4
"""
4. groupd(lst) presa in input una lista lst di interi tale che i primi tre rappresentano una data, 
   i secondi tre un'altra data, i successivi tre un'altra data e così via, 
   modifica la lista lst raggruppando ogni tripla in una stringa separando i numeri con il carattere '/' . 
   Si assume che la lista lst abbia una lunghezza multipla di 3. 
   Esempio
>>> lst = [1, 2, 2013, 23, 9, 2011, 10, 11, 2000]
>>> groupd(lst)
>>> lst
['1/2/2013', '23/9/2011', '10/11/2000']
"""

# definisco la funzione
def groupd(lst):
    # imposto la lista di output
    lst_g = []
    # scandisco la lista con step da 3
    for i in range(0, len(lst)-1, 3):
        # assegno le variabili
        day = str(lst[i])
        month = str(lst[i+1])
        year = str(lst[i+2])
        # creo la stringa
        date = day + '/' + month + '/' + year
        # e l'aggiungo alla lista
        lst_g.append(date)
    # ritorno la lista
    return lst_g

# stampo la prova
print(groupd([1, 2, 2013, 23, 9, 2011, 10, 11, 2000]))