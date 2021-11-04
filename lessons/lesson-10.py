# -*- coding: utf-8 -*-

# importo words
from files import words

# %%esercizio_1
"""
1. wset(fname) ritorna un insieme contenente le parole (distinte) del file fname . Le parole sono ridotte
   alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> wset('alice.txt') ritorna un insieme di cardinalità 3009
"""

# definisco la funzione
def wset(fname):
    # creo la lista delle parole
    word_list = words.fwords(fname, 'utf-8-sig')
    # le porto tutte in minuscolo
    word_list = [w.lower() for w in word_list]
    # ritorno direttaente la lunghezza del set della lista
    return len(set(word_list))

# prova
print(wset('files/alice.txt'))

# %%esercizio_2
"""
2. wsub(fn1, fn2) ritorna un insieme contenente le parole (distinte) che appaiono nel file fn1 e che non
   appaiono nel file fn2 . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> wsub('alice.txt', 'holmes.txt') ritorna un insieme di cardinalità 712
"""

# definisco la funzione sulla base di quella usata nell'esercizio precedente
def wsub(fn1, fn2):
    # creo la lista delle parole del primo file
    word_list_fn1 = words.fwords(fn1, 'utf-8-sig')
    # le porto tutte in minuscolo
    word_list_fn1 = [w.lower() for w in word_list_fn1]
    # creo la lista delle parole del secondo file
    word_list_fn2 = words.fwords(fn2, 'utf-8-sig')
    # le porto tutte in minuscolo
    word_list_fn2 = [w.lower() for w in word_list_fn2]
    # ritorno direttamente la lunghezza della differenza tra i set delle due liste
    return len(set(word_list_fn1) - set(word_list_fn2))

# prova
print(wsub('files/alice.txt', 'files/holmes.txt'))

# %%esercizio_3
"""
3. wdict(fname) ritorna un dizionario che ad ogni parola del file fname associa il numero di occorrenze
   della parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempio
>>> d = wdict('alice.txt')
>>> d['alice'] --> 403
>>> d['rabbit'] --> 51
>>> d['queen'] --> 75
"""

# definisco la funzione
def wdict(fname):
    # inizializzo il dizionario
    d =  {}
    # creo la lista delle parole
    word_list = words.fwords(fname, 'utf-8-sig')
    # le porto tutte in minuscolo
    word_list = [w.lower() for w in word_list]
    # mi ricavo il dizionario dalla lista
    # per ogni parola (key) ne associo le occorrenze (values)
    for word in word_list:
        d[word] = d.get(word, 0) +1
    # ritorno il dizionario
    return d

#prove
d = wdict('files/alice.txt')
print(d['alice'])
print(d['rabbit'])
print(d['queen'])

# %%esercizio_4
"""
4. nextw(fname) ritorna un dizionario che ad ogni parola del file fname associa l'insieme delle parole che
   seguono la parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempio
>>> d = nextw('alice.txt')
>>> d['go']
{'and', 'among', 'splashing', 'back', 'down', 'through', 'at', 'in', 'nearer', 'said', 'from', 'for', 
'no', 'there', 'to', 'his', 'after', 'let', 'with', 'by', 'on', 'alice', 'near', 'anywhere', 'round'}
>>> d['write']
{'that', 'this', 'it', 'one', 'with', 'out'}
"""

# definisco una funzione che ha come base la precedente
def nextw(fname):
    # inizializzo il dizionario
    d =  {}
    # creo la lista delle parole
    word_list = words.fwords(fname, 'utf-8-sig')
    # le porto tutte in minuscolo
    word_list = [w.lower() for w in word_list]
    # per ogni parola della lista
    # (tranne l'ultima che non è seguita da altre)
    for i in range(len(word_list)-1):
        # controllo se la parola è già nel dizionario
        if word_list[i] in d:
            # se già c'è, le aggiungo la successiva
            d[word_list[i]].add(word_list[i+1])
        # altrimenti aggiungo entrambe
        else:
            d[word_list[i]] = {word_list[i+1]}
    # ritorno d
    return d

# prove
d = nextw('files/alice.txt')
print(d['go'])
print(d['write'])

# %%esercizio_5
"""
5. mostf(fname, l) ritorna un insieme contenente le parole di lunghezza l di massima frequenza nel file
   fname . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
   Esempi
>>> mostf('holmes.txt', 7)
{'nothing', 'however'}
mostf('holmes.txt', 8)
{'sherlock'}
mostf('frankenstein.txt', 16) 
{'unenforceability', 'impracticability', 'perpendicularity', 'indiscriminately', 'inextinguishable'}
"""

def mostf(fname, l):
    # creo la lista delle parole
    word_list = words.fwords(fname, 'utf-8-sig')
    # le porto tutte in minuscolo e elimino quelle che non sono lunghe quanto l
    long_words = [w.lower() for w in word_list if len(w) == l]
    # mi ricavo il dizionario dalla lista
    # per ogni parola (key) ne associo le occorrenze (values)
    d = {}
    for word in long_words:
        d[word] = d.get(word, 0) +1
    # cerco il valore più alto nelle occorrenze
    max_occ = max(d.values())
    # ritorno il set con le parole con il valore = a max_occ
    return {w for w, occ in d.items() if occ == max_occ}

# prove
print(mostf('files/holmes.txt', 7))
print(mostf('files/holmes.txt', 8))
print(mostf('files/frankenstein.txt', 16))