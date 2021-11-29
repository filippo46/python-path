# -*- coding: utf-8 -*-


# %%intro
"""
Supponete di dover manipolare una tabella di valori, rappresentata come lista
di liste (ciascuna contiene i valori di una riga).
"""


# %%esercizio_01
"""
1. Usando la notazione per l'unpacking costruite una funzione
   somma_seconda_colonna(matrice)
   che somma tutti i valori della seconda colonna.
   Esempio:
>>> M = [[ 1, 2, 3, 4 ],
         [ 5, 6, 7, 8 ],
         [ 9, 10, 11, 12 ],
        ]
>>> somma_seconda_colonna(M)
18
"""


def somma_seconda_colonna(matrice):
    sub = 0
    for row in matrice:
        _, second, *_ = row
        sub += second
    return sub


M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     ]
print(somma_seconda_colonna(M))


# %%esercizio_02
"""
2. Ridefinite la funzione sfruttando le funzioni sum e map
   per estrarre dalla matrice la sola seconda colonna e sommarla.
"""


def somma_seconda_colonna(matrice):
    return sum(map(lambda row: row[1], matrice))


print(somma_seconda_colonna(M))


# %%esercizio_03
"""
3. Definite la funzione terne(...) che riceve un numero indefinito di elementi
   e torna una lista di terne complete, ignorando eventuali elementi spuri,
   usando l'assegnamento multiplo per raccogliere gli elementi delle terne
   dalla lista invece che le slice.
   Esempio
   (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""


def terne(*lst):
    out_lst = []
    while len(lst) > 2:
        x, y, z, *lst = lst
        out_lst.append([x, y, z])
    return out_lst


print(terne(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# %%esercizio_04
"""
4. Usando le funzioni nidificate o una lambda realizzate una funzione
   somma_colonna_K(matrice, K) che torna la somma di tutti gli elementi nella
   colonna K leggendo almeno un valore dal namespace della funzione
   somma_colonna_K() che la contiene.
   Esempio:
   M = [[ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        ]
  somma_colonna_K(M, 3)
  24
"""


def somma_colonna(matrice, K):
    return sum(map(lambda row: row[K], matrice))


print(somma_colonna(M, 3))
