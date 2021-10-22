# -*- coding: utf-8 -*-

"""
1)  Modificate la funzione aggiorna_k_massimi in modo da usare una lista ordinata invece che disordinata 
    e misurate i tempi di esecuzione di k_massimi_casuali in Jupyter col comando %time per K=3000 e K=30 (e S=0, N=1000000).
"""

"""
Mia versione
"""

# base del Prof
import random
def k_massimi_casuali(S, N, K):
    '''estrae i K maggiori valori interi tra N generati a caso a partire dal seed S'''
    random.seed(S)
    massimi = []						# inizialmente i K valori massimi sono la lista vuota
    for i in range(N):						# per N volte
        X = random.randint(-1000000000, 1000000000)		# estraggo un valore intero a caso tra -1000000000 e +100000000000
        if i < 10:
            print(X)						# stampo i primi 10 valori generati per testare il funzionamento
        aggiorna_K_massimi_ord(massimi, X, K)			# aggiorno i K maggiori valori inserendoci X se necessario
    return massimi						# torno i K valori massimi

# mia funzione
def aggiorna_K_massimi_ord(massimi, V, K):
    if len(massimi) < K:    # se la lista ha < K elementi, aggiungo V
        massimi.append(V)
        return
    if V <= massimi[-1]:         # se V <= al minimo, lo ignoro
        return
    else:
        massimi[-1] = V      # altrimenti assegno V alla lista
        massimi.sort(reverse=True)
        
#################################################################################################
"""
Versione del Prof
"""

"""
def aggiorna_K_massimi(massimi, X, K):
    if len(massimi) < K:
        inserisci_in_lista_ordinata(X, massimi)
    elif X > massimi[-1] :
        inserisci_in_lista_ordinata(X, massimi)
        massimi.pop()
    # altrimenti non faccio niente
    
def inserisci_in_lista_ordinata(X, lista):
    inizio = 0
    fine   = len(lista) - 1
    while inizio <= fine :
        medio = (inizio+fine)//2	# va usata la divisione intera per ottenere un indice intero
        Y = lista[medio]
        if Y == X:
            lista.insert(medio, Y)
            return
        if X > Y:
            fine = medio - 1
        else:
            inizio = medio + 1
    lista.insert(inizio, X)
"""