# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:56:52 2021

@author: Filippo
"""

# %%esercizio_1
"""
1. clines(fname, s) ritorna il numero di linee del file di testo fname che contengono la stringa s senza
   differenziare tra maiuscole e minuscole. Esempi: se il file testo.txt contiene le 4 righe

SUGLI ERRORI
Gli errori sono inevitabili. Errare è umano,
perseverare è diabolico. Non ci sono rimedi
a questo stato di cose (su questa terra).

allora
	clines('testo.txt', 'err')	ritorna 3
	clines('testo.txt', 'Errori')	ritorna 2
"""

# prendo in input il file e la stringa
def clines(fname, s):
    # imposto s in minuscolo
    s = s.lower()
    # imposto una variabile contatore
    lcount = 0
    # apro il file
    with open(fname, encoding = 'utf8') as f:
    # avvio un ciclo dove per ogni linea:
        for linea in f:
            # porto tutto in minuscolo (non dobbiamo fare distinzione)
            linea = linea.lower()
            # controllo se s è in linea
            if s in linea:
                # se vero, aggiorno il contatore
                lcount += 1
    # ritorno il contatore
    return lcount

# stampo le prove
print(clines('files/testo.txt', 'err'))
print(clines('files/testo.txt', 'Errori'))

# %%eercizio_2
"""
2. all_char(fname, enc) ritorna una stringa unicode contenente tutti i caratteri, senza ripetizioni e in
   ordine di apparizione, nel file fname decodificato con la codifica enc . Ad esempio se il file è quello
   dell'esercizio precedente, assumendo che sia codificato in UTF-8, si ha:

>>> allc = all_char('testo.txt', 'utf8')
>>> allc
'SUGLI ERO\nlierosnvtab.èum,pdcNq()'
>>> print(allc)
SUGLI ERO
lierosnvtab.èum,pdcNq()
"""

# definisco la funzione
def all_char(fname, enc):
    # imposto una stringa vuota da "riempire"
    s = ''
    # apro il file
    with open(fname, encoding = enc) as f:
        # per ogni linea del file
        for line in f:
            # per ogni carattere
            for c in line:
                # se non è già presente nella stringa, lo aggiungo alla stessa
                if c not in s:
                    s += c
    # ritorno la stringa            
    return s

# eseguo la prova
allc = all_char('files/testo.txt', 'utf8')
print(allc)

# %%esercizio_3
"""
3. anagrams(fname, w) ritorna una lista contenente tutti gli anagrammi, senza ripetizioni e senza
   differenziare tra maiuscole e minuscole, della parola w nel file fname . Un anagramma di una parola w è
   un'altra parola che usa esattamente le stesse lettere di w ma in ordine diverso, ad esempio mangiare e
   germania, torre e retro. La lista ritornata deve includere anche la parola w stessa, se è presente.
   Possono risultare utili la funzione built-in sorted() e il metodo join() delle stringhe.
   Nel risultato non ci devono essere doppioni.
   Esempi, sia fname il file 'alice.txt' :

>>> anagrams(fname, 'read')	ritorna ['dear', 'read', 'dare']
>>> anagrams(fname, 'elbow')	ritorna ['elbow', 'below']
"""

# definisco la funzione
def anagrams(fname, w):
    # "ordino" la parola da cercare
    sorted_w = ''.join(sorted(w))
    sorted_w = sorted_w.lower()
    # imposto una lista vuota
    a_list = []
    # apro il file
    with open(fname) as f:
        # per ogni linea del file
        for line in f:
            # per ogni parola
            for word in line.split():
                # ordino la parola corrente
                sorted_word = ''.join(sorted(word))
                sorted_word = sorted_word.lower()
                # e la confronto con quella da cercare
                if sorted_word == sorted_w and word.lower() not in a_list:
                    # se uguale e non già presente in lista, la inserisco
                    a_list.append(word)
    # ritorno la lista
    return a_list

# stampo le prove
print(anagrams('files/alice.txt', 'read'))
print(anagrams('files/alice.txt', 'elbow'))

# %%esercizio_4
"""
4. log_update(filelog, evento) aggiorna il file filelog aggiungendo una nuova linea che inizia con la data e l'orario
   della chiamata e dopo ': ' la stringa in evento . Per ottenere la data e l'orario si possono usare le funzioni
   ctime() e time() del modulo time della libreria standard. Esempio, se il file log contiene:

Mon Oct 7 17:48:22 2013: first event
Mon Oct 7 17:48:32 2013: second event
Mon Oct 7 17:49:15 2013: Event n. 3

e se dopo 84 secondi dall'ultimo aggiornamento viene effettuata la chiamata log_update(log, 'New event!') , il file log diventa:

Mon Oct 7 17:48:22 2013: first event
Mon Oct 7 17:48:32 2013: second event
Mon Oct 7 17:49:15 2013: Event n. 3
Mon Oct 7 17:50:39 2013: New event!
"""

# importo time
import time

# definisco la funzione
def log_update(filelog, evento):
    # ottengo i secondi della "data"
    seconds = time.time()
    # li converto nella data effettiva
    date = time.ctime(seconds)
    # apro il file in modalità append
    with open( filelog, mode='a',) as f:
        # scrivo l'evento
        f.write(date + ': ' + evento + '\n')
    return
        
# eseguo la prova
log_update('files/log.log', 'New event!')

# %%esercizio_5
"""
5. findurl(lista_url, s, k) ritorna in una lista gli URL contenuti nella lista lista_urls tali che le pagine da essi puntate contengano almeno k
   occorrenze della stringa s . Si assume che gli URL in urls siano relativi a pagine HTML e quindi documenti di testo. 
   Esempi, sia

>>> urls = ['http://python.org', 'http://google.com', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html']
>>> findurl(urls, 'Python', 2) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html'] 
>>> findurl(urls, 'Python', 7) ritorna 
['http://python.org', 'http://docs.python.org/2.7/index.html']
"""

# importo requests
import requests

# definisco la funzione
def findurl(lista_url, s, k):
    # imposto la lista di output
    out_list = []
    # per ciascun url in input
    for url in lista_url:
        # richiedo la pagina
        ask_url = requests.get(url)
        # e leggo il contenuto
        content = ask_url.text
        # conto le occorrenze di s
        n = content.count(s)
        # se >= a k
        if n >= k:
            # aggiungo l'url all'output
            out_list.append(url)
    # e lo restituisco
    return out_list

# imposto la lista di prova
urls = ['http://python.org',
        'http://google.com',
        'http://docs.python.org/2.7/index.html',
        'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html']

# stampo le prove
print(findurl(urls, 'Python', 2))
print(findurl(urls, 'Python', 7))