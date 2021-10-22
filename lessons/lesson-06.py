# -*- coding: utf-8 -*-

# %%esercizio_1
"""
1. firstline(t, s) ritorna la prima linea della stringa t che contiene la stringa s , mentre se s non occorre in t ritorna None . 
	Esempio
>>> t = '''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.'''
	firstline(t, 'non')		ritorna		'del doman non c’è certezza.'
"""

# definisco la funzione
def firstline(t, s):
    # porto tutto in minuscole e divido il testo per righe
    s = s.lower()
    t = t.lower().splitlines()
    # inizio la ricerca di s in t
    for e in t:
        if e.find(s) != -1:
            # se lo trovo, ritorno la riga
            pos = e.find('\n')
            return e[pos + 1:]
    # se il ciclo finisce, ritorno None
    return None

# imposto il testo di prova
t = '''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.'''

# stampo la prova
print(firstline(t, 'non'))

# %%esercizio_1_avanzato
"""
Versione semplificata
"""

# definisco la funzione
def firstline(t, s):
    # porto tutto in minuscole e divido il testo per righe
    s = s.lower()
    t = t.lower().splitlines()
    # inizio la ricerca di s nelle singole righe
    for line in t:
        if s in line:
            # se lo trovo, ritorno la riga
            return line
    # se il ciclo finisce, ritorno None
    return None

# imposto il testo di prova
t = '''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.'''

# stampo la prova
print(firstline(t, 'non'))

# %%esercizio_2
"""
2. countw(t, w) ritorna il numero di occorrenze della parola w nella stringa t . 
	Esempio
	t = 'le cose non sono solo cose, ma anche cosette'
	countw(t, 'cose') 		ritorna		2
"""

# definisco la funzione
def countw(t, w):
    # creo la lista non_alfa per trovare e sostituire eventuali caratteri per poi semplificare la divisione
    non_alfa = []
    for c in t:
        if c not in non_alfa and not c.isalpha():
            non_alfa.append(c)
    # sostituisco i non alfa
    for c in non_alfa:
        t = t.replace(c, ' ')
    # porto tutto in minuscolo e divido il testo
    t = t.lower().split()
    w = w.lower()
    # conto le occorrenze
    count = t.count(w)
    return count
    
# imposto il testo di prova
t = 'le cose non sono solo cose, ma anche cosette'

# stampo la prova
print(countw(t, 'cose'))

# %%esercizio_3
"""
3. digits(t) ritorna la lista delle sequenze numeriche contenute nella stringa t . 
   Per sequenza numerica intendiamo una sequenza di cifre (caratteri 0 , 1 ,…, 9 ) di lunghezza massimale. 
	Esempio
	t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
	digits(t) 			ritorna 	['23', '06', '7867555', '345', '675665676', '34565']
"""

# definisco la funzione
def digits(t):
    # imposto una lista e una stringa on the go
    numeri = []
    seq_corrente = ''
    # scanndisco il testo
    for c in t:
        # se trovo un numero, lo scrivo nella stringa temporanea
        if c.isdigit():
            seq_corrente += c
        # quando la string "finisce", l'aggiungo ala lista
        elif seq_corrente:
            numeri.append(seq_corrente)
            seq_corrente = ''
    # ritorno la lista
    return numeri

# imposto il testo di prova
t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
# stampo la prova
print(digits(t))

# %%esercizio_4
"""
4. column(table, k) ritorna una lista che contiene i valori della colonna k della tabella table . 
   La tabella è rappresentata in modo che ogni linea di table contiene una riga e i valori delle colonne sono separati
   dal carattere ';' . Se table ha n colonne, allora ogni linea di table conterrà esattamente n-1 caratteri ';' .
	Esempio
	table = '''Milano;12;23
Roma;16;25
Napoli;15;27
Firenze;11;20'''
	column(table, 1)		ritorna		['12', '16', '15', '11']
"""

# definisco la funzione
def column(table, k):
    # imposto la lista di output
    result = []
    # divido la tabella in righe
    rows = table.splitlines()
    # per ogni riga
    for row in rows:
        # ottengo le colonne splittando sul carattere
        _ = row.split(';')
        # aggiungo l'elemento nella posizione definita (k) alla lista di output
        result.append(_[k])
    # ritorno l'output
    return result

# testo di prova
table = '''Milano;12;23
Roma;16;25
Napoli;15;27
Firenze;11;20'''

# stampo la prova
print(column(table, 1))