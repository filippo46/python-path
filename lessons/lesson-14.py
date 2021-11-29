# -*- coding: utf-8 -*-

# %%intro
"""
Si vuole disegnare una città sullo schermo, rappresentata da una serie di
rettangoli appoggiati in basso, larghi 100 pixel e di altezza, posizione
orizzontale e colore variabili. Ciascun elemento della lista è una tupla
( coordinata_x, colore, altezza ) che descrive un rettangolo. Il colore di
ciascun rettangolo è una tupla (R, G, B) che indica i valori delle tre
componenti (rosso, verde, blu) del colore, ciascuna un intero tra 0 e 255
compresi che ne indica la luminosità (0=min, 255=max).

Esempio: (255, 0, 0) = rosso 
    	 (0, 255, 0) = verde
         (0, 0, 255) = blu
    	 (0, 0, 0)   = nero
         (255, 255, 255) = bianco
"""

# %%esercizio_01
"""
1. Supponiamo che i rettangoli debbano essere disegnati in ordine dal più alto
   al più basso in modo che nessun rettangolo resti completamente coperto dagli
   altri, e che in caso di parità si debba disegnare prima il rettangolo con
   posizione x minore. Si definisca la funzione ordina_palazzi(lista) che torna
   la lista di rettangoli ordinata come indicato senza modificare la lista
   originale.
   
   Esempio:
   lista = [(216, (54, 234, 22), 106),
		   (740, (94, 236, 163), 71),
		   (21, (49, 140, 100), 717),
		   (137, (204, 5, 140), 717),
		   (922, (15, 244, 140), 569),
		   (52, (2, 98, 163), 514),
		   (961, (138, 58, 166), 605),
		   (396, (116, 149, 25), 448),
		   (586, (129, 196, 183), 467),
		   (347, (218, 229, 143), 253)]
   
   ordina_palazzi(lista)
    [(21, (49, 140, 100), 717),
     (137, (204, 5, 140), 717),
     (961, (138, 58, 166), 605),
     (922, (15, 244, 140), 569),
     (52, (2, 98, 163), 514),
     (586, (129, 196, 183), 467),
     (396, (116, 149, 25), 448),
     (347, (218, 229, 143), 253),
     (216, (54, 234, 22), 106),
     (740, (94, 236, 163), 71)]
"""

lista = [(216, (54, 234, 22), 106),
		   (740, (94, 236, 163), 71),
		   (21, (49, 140, 100), 717),
		   (137, (204, 5, 140), 717),
		   (922, (15, 244, 140), 569),
		   (52, (2, 98, 163), 514),
		   (961, (138, 58, 166), 605),
		   (396, (116, 149, 25), 448),
		   (586, (129, 196, 183), 467),
		   (347, (218, 229, 143), 253)]

# definisco la fumzione
def ordina_palazzi(lista):
    # poiché non vogliamo modificare l'originale, assegno a una nuova
    palazzi_ordinati = sorted(lista, key = lambda x: (-x[2], x[0]))
    return palazzi_ordinati

# prova
print(ordina_palazzi(lista), sep='\n')

# direttamente con lambda
ordered_palaces = sorted(lista, key = lambda x: (-x[2], x[0]))

# prova
print (ordered_palaces, sep = '\n')


# %%esercizio_02
"""
2. Si scriva la funzione palazzo_piu_costoso(lista) che torna la tupla che
   descrive il palazzo più costoso da costruire, tenendo conto che il costo di
   costruzione:
   - è proporzionale all'altezza del palazzo
   - la costante di proporzionalità è la media dei tre valori che indicano il colore
   - a pari merito vogliamo quello più a destra
   
   Esempio:
       palazzo_piu_costoso(lista)
       (137, (204, 5, 140), 717)
"""

def palazzo_piu_costoso(lista):
    # il candidato sarà il "palazzo" con la superfice più grande e "colorata"
   candidate = max(lista, key = lambda palace: (palace[2] * (sum(palace[1]) / 3
                    ), palace[0])) 
   return candidate

# prova
print(palazzo_piu_costoso(lista))


# %%esercizio_03
"""
3. Si scriva la funzione palazzo_coperto(lista) che torna True se, disegnando i
    palazzi nell'ordine dato nella lista (senza riordinarli), esiste almeno un
    palazzo che è coperto in tutta la sua altezza da un altro, ovvero se:
   - esiste un palazzo P1 tale che esiste un palazzo P2 più alto o uguale a P1, 
	che viene disegnato dopo P1 
	con le due posizioni orizzontali P1.x e P2.x che differiscono meno di 100
    (in valore assoluto)
   Esempio:
       palazzo_coperto(lista)
       True
"""

def palazzo_coperto(lista):
    # genero le coppie da confrontare
    couples = ((p1, p2) for i, p1 in enumerate(lista[: -1]) for j, p2 in
               enumerate(lista[i+1 :]))
    # ritorno l'any del confronto
    return any(map(lambda x: x[0][2] <= x[1][2] and abs(x[0][0] - x[1][0]) <
                   100, couples))

# prova
print(palazzo_coperto(lista))


# %%esercizio_04
"""
4. Si scriva la funzione palazzi_scoperti(lista) che torna la lista dei soli
   palazzi non coperti neanche parzialmente dagli altri (se vengono disegnati
   nell'ordine dato senza riordinarli).
   
   Esempio:
    palazzi_scoperti(lista)
    [(740, (94, 236, 163), 71),
     (52, (2, 98, 163), 514),
     (961, (138, 58, 166), 605),
     (586, (129, 196, 183), 467),
     (347, (218, 229, 143), 253)]
"""

def palazzi_scoperti(lista):
    # ritorno una lista dei p1 non seguiti da nessun p2 che lo copre
    return [p1 for i ,p1 in enumerate(lista) 
            if all(map(lambda p2: abs(p2[0] - p1[0]) >= 100, lista[i+1 : ]))]

# prova
print(palazzi_scoperti(lista))


# %%esercizio_05
"""
5. Definire usando l'istruzione yield un iteratore quadrati_cubi(L) che, data 
   la lista L genera i quadrati ed i cubi degli elementi, alternati.
   
   Esempio:
   lista = [1, 2, 3, 4, 5]
   list(quadrati_cubi(lista))
   [1, 1, 4, 8, 9, 27, 16, 64, 25, 125 ]
"""

def quadrati_cubi(L):
    for n in L:
        yield n ** 2
        yield n ** 3
        
# prova
lista = [1, 2, 3, 4, 5]
print(list(quadrati_cubi(lista)))

# %%esercizo_6
"""
6. Definire l'iteratore quadrati_cubi(L) dell'esercizio 5 usando la list-comprehension.
   Esempio:
>>> lista = [1, 2, 3, 4, 5]
>>> list(quadrati_cubi(lista))
[1, 1, 4, 8, 9, 27, 16, 64, 25, 125 ]
"""

def quadrati_cubi(L):
    return (n**p for p in [2, 3] for n in L)

# prova
lista = [1, 2, 3, 4, 5]
print(list(quadrati_cubi(lista)))