# -*- coding: utf-8 -*-

# %%esercizio1
"""
1. Scrivere una funzione 'scontato' che prende in input un importo e una percentuale di sconto e ritorna
   l'importo scontato. Ad esempio, se l'importo è 1000 e lo sconto è 20 , la funzione ritorna 800 .
"""

# definisco la funzione scontato
def scontato(importo, sconto):
    # ritorno direttamente scontato
    return importo - (importo * sconto / 100)

# stampo la prova
print(scontato(1000, 20))

# %%esercizio2
"""
2. Scrivere una funzione 'secondi' che prende in input un lasso di tempo espresso tramite numero di ore
   hh , numero di minuti mm e numero secondi ss e ritorna l'equivalente numero di secondi. Ad esempio,
   se hh = 2 , mm = 1 e ss = 11 , la funzione ritorna 7271 .
"""

# definisco la funzione secondi
def secondi(hh, mm, ss):
    # ritorno direttamente il risultato
    return (hh*60**2) + (mm*60) + ss

# stampo la prova
print(secondi(2, 1, 11))

# %%esercizio3
"""
3. Scrivere una funzione 'invest' che prende in input un capitale C , un interesse annuale i e un numero di
   anni n e ritorna come intero il capitale maturato dopo un investimento di n anni all'interesse i .
   (usando la formula     maturato = capitale * (1+interesse/100)**anni )
   Ad esempio, se gli argomenti sono  C = 1000 , i = 10 e n = 2 , la funzione ritorna 1210 .
"""

# definisco la funzione
def invest(c, i, n):
    # ritorno direttamente maturato arrotondato
    return round(c * (1+i/100) ** n)

# stampo la prova
print(invest(1000, 10, 2))