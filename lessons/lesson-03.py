# -*- coding: utf-8 -*-
# %%esercizio1
"""
1. Scrivere una funzione media(vals) che prende in input una lista vals (i cui valori si assume siano
   numeri) e ritorna la media dei suoi valori.
"""

# definisco la funzione
def media(vals):
    # imposta la variabile somma che mi servirà nel ciclo
    somma = 0
    # sommo tutti i numeri della lista con un ciclo
    for n in vals:
        somma += n
    # calcolo la media e la ritorno
    media = somma / len(vals)
    return media

# provo la funzione
print(media([21, 40, 55, 75]))

# %%es1_pro_dition
"""
Versione avanzata
"""

# definisco la funzione
def media(vals):
    # ritorno direttamente il risultato
    return sum(vals) / len(vals)

# provo la funzione
print(media([21, 40, 55]))

# %%esercizio2
"""
2. Scrivere una funzione space(s, k) che prende in input una stringa s e un intero k e ritorna una nuova
   stringa che ha i caratteri di s separati da k spazi. Ad esempio
   space('ciao ciao', 1) ritorna la stringa

    'c i a o   c i a o'
"""

# definisco la funzione
def space(s, k):
    # impost la stringa nuova
    nuova_s = ''
    # avvio il ciclo che itera su s fino al
    # penultimo carattere (per non aggiungere spazi alla fine)
    for c in range(len(s)-1):
        # aggiungo il carattere e gli spazi
        nuova_s += s[c] + ' ' * k
    # aggiungo l'ultimo carattere e ritorno nuova_s
    nuova_s += s[-1]
    return nuova_s

# stampo la prova
print(space('ciao ciao', 1))

# %%esercizio3
"""
3. Scrivere una funzione crossing_over(m, f) che prese in input due liste m e f (che si assume abbiano
   la stessa lunghezza), ritorna una nuova lista che contiene l'incrocio delle due liste come illustrato dal
   seguente esempio (prendendo alternativamente un elemento dalla prima lista, poi dalla seconda, poi dalla prima ...):
   crossing_over([1, 3, 5], [2, 4, 6]) 
   ritorna la lista [1, 2, 3, 4, 5, 6]
"""

# definisco la funzione
def crossing_over (m, f):
    # imposto la lista finale
    risultato = []
    # avvio il ciclo su una delle liste iniziali
    for i in range(len(m)):
        # per ogni posizione aggiungo i rispettivi al risutato
        risultato += [m[i]] + [f[i]]
    # ritorno il risultato
    return risultato

# stampo la prova
print(crossing_over([1, 3, 5], [2, 4, 6]))