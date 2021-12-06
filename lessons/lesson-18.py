# -*- coding: utf-8 -*-

""" LEZIONE 18 - RICORSIONE VS. ITERAZIONE """

# %%esercizio_01
"""
Es 1: Definite la funzione ricorsiva rovescia(lista) che rovescia una lista
costruendo mano a mano il risultato all'uscita dalla ricorsione. Per estrarre
elementi dalla lista usate solo il metodo lista.pop(0) che torna il primo
elemento della lista togliendolo dalla lista.
Nota: la lista originale viene modificata.
"""


def rovescia(lista):
    # caso base: lista è vuota
    if not lista:
        return lista
    else:
        # estraggo il primo elemento
        zero = lista.pop(0)
        # rovescio la lista restante
        rev_list = rovescia(lista)
        # e gli appendo zero
        rev_list.append(zero)
        return rev_list


# prova
print(rovescia([1, 2, 3, 4, 5]))
print(rovescia(['a', 'b', 'c', 'd', 'e']))

# %%esercizio_02
"""
Es 2: Definite la funzione rovescia2(lista) che torna una copia rovesciata di
una lista sfruttando una funzione ricorsiva ausiliaria a cui passa una lista di
appoggio iniziale vuota alla quale aggiungere gli elementi. La funzione
ausiliaria ricorsiva sfrutta il passaggio di argomenti in avanti e modifica
mano a mano la lista di appoggio in cui aggiunge mano a mano i valori, uno per
chiamata. Per estrarre elementi dalla lista usate solo il metodo lista.pop(0)
che torna il primo elemento della lista togliendolo dalla lista.
Nota: la lista originale viene modificata.
"""


def rovescia2(lista):
    return _rovescia2([], lista)


def _rovescia2(rev_list, lista):
    # caso base: lista è vuota
    if not lista:
        return rev_list
    else:
        # estraggo il primo elemento
        zero = lista.pop(0)
        # rovescio la lista restante
        rev_list = _rovescia2(rev_list, lista)
        # e gli appendo zero
        rev_list.append(zero)
        return rev_list


# prova
print(rovescia2([1, 2, 3, 4, 5]))
print(rovescia2(['a', 'b', 'c', 'd', 'e']))


# %%esercizio_03
"""
Es 3: A partire dalla definizione iterativa di massimo comun divisore (GCD) di
due numeri positivi x ed y, ovvero:

# per calcolare il GCD di x ed y interi positivi
    # ripeti se x != y
        # x = x-y		se x>y
        # y = y-x		se x<y
    # torna x

a) definite sua implementazione iterativa.
b) definite la implementazione ricorsiva che simula il ciclo passando i valori
   x ed y in avanti
"""


def gcd_iter(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


# ricorsivo
def gcd_rec(x, y):
    # caso base : x e y sono uguali
    if x == y:
        return x
    # se x > y
    elif x > y:
        return gcd_rec(x - y, y)
    # se y > x
    else:
        return gcd_rec(x, y - x)


# prova
print(gcd_iter(4, 40))
print(gcd_rec(30, 3))


# %%esercizio_04
"""
Es 4: Ripetete l'esercizio al contrario, partendo da questa diversa definizione
ricorsiva di massimo comun divisore (GCD) di due numeri positivi x ed y, ovvero
    GCD2(x, y) = x              se x==y
    GCD2(x, y) = GCD2(x%y,y)	se x>y
    GCD2(x, y) = GCD2(x,y%x)	se x<y

a) definite la funzione ricorsiva corrispondente
b) definite la funzione iterativa corrispondente partendo da quella ricorsiva
"""


def gcd2_rec(x, y):
    if y == 0:
        return x
    else:
        return gcd2_rec(y, x % y)


def gcd2_iter(x, y):
    while y != 0:
        x, y = y, (x % y)
    return x


# prova
print(gcd2_rec(1200, 900))
print(gcd2_iter(4250, 200))
