# -*- coding: utf-8 -*-

# %%esercizio_1
"""
1. prec(g1, m1, a1, g2, m2, a2) ritorna True se la data g1, m1, a1 (giorno, mese, anno) è precedente
   o uguale alla data g2, m2, a2 .
   Esempi
   prec(13, 11, 2012,  2,  3, 2013)	ritorna	True
   prec(13, 11, 2012, 27, 12, 2011)	ritorna	False
   prec( 1, 10, 2013,  1, 11, 2013)	ritorna	True
"""

# definisco la funzione
def prec(g1, m1, a1, g2, m2, a2):
    # controllo prima gli anni
    if a1 < a2:
        return True
    elif a1 > a2:
        return False
    else:
        # poi i mesi
        if m1 < m2:
            return True
        elif m1 > m2:
            return False
        else:
            # infine i giorni
            if g1 <= g2:
                return True
            else:
                return False
            
# stampo le prove
print(prec(13, 11, 2012,  2,  3, 2013))
print(prec(13, 11, 2012, 27, 12, 2011))
print(prec( 1, 10, 2013,  1, 11, 2013))

# %%esercizio_1_avanzato
"""
Versione esteticamente migliore
"""

# definisco la funzione
def prec(g1, m1, a1, g2, m2, a2):
    # torno direttamente il confronto tra i due "set"
    return [a1, m1, g1] <= [a2, m2, g2]

# stampo le prove
print(prec(13, 11, 2012,  2,  3, 2013))
print(prec(13, 11, 2012, 27, 12, 2011))
print(prec( 1, 10, 2013,  1, 11, 2013))

# %%esercizio_2
"""
2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
   elementi di lst . Esempio
   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]
"""

# definisco la funzione come richiesto
def l2d(lst):
    # imposto la lista in output vuota
    risultato = []
    # per ogni elemento di lst trovo il valore relativo e lo aggiung a risultato
    for i in lst:
        if i == 'zero':
            risultato.append(0)
        elif i == 'uno':
            risultato.append(1)
        elif i == 'due':
            risultato.append(2)
        elif i == 'tre':
            risultato.append(3)
        elif i == 'quattro':
            risultato.append(4)
        elif i == 'cinque':
            risultato.append(5)
        elif i == 'sei':
            risultato.append(6)
        elif i == 'sette':
            risultato.append(7)
        elif i == 'otto':
            risultato.append(8)
        elif i == 'nove':
            risultato.append(9)
    return risultato

# stampo la prova
print(l2d(['nove','due','due','tre']))

# %%esercizio_2_avanzato
"""
La funzione può essere snellita a un paio di righe.
"""

# definisco la funzione come richiesto
def l2d(lst):
    # imposto la lista in output vuota
    risultato = []
    # creo una lista d'appoggio con le stringhe di tutti i numeri
    # (ogni stringa avrà l'index corrispondente al suo intero)
    stringhe = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    # cerco ogni elemento di lst in stringhe e lo aggiungo a risultato
    for i in lst:
        risultato.append(stringhe.index(i))
    return risultato

# stampo la prova
print(l2d(['nove','due','due','tre']))

# %%esercizio_2_avanzato_2
"""
Con list comprehension
"""

# definisco la funzione come richiesto
def l2d(lst):
    stringhe = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    # ritorno direttamente l'output con list comprehension
    return [stringhe.index(i) for i in lst]

# stampo la prova
print(l2d(['nove','due','due','tre']))

# %%esercizio_3
"""
3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
   ripetizioni.
   Esempi
   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']
"""

# definisco la funzione richiesta
def distinct(lst):
    # imposto la lista da ritornare
    risultato = []
    # per ogni elemento di lst
    for i in lst:
        # se non già presente in risultato
        if i not in risultato:
            # lo aggiungo
            risultato.append(i)
    # ritorno risultato
    return risultato

# stampo le prove
print(distinct([3,1,3,2,6,6]))
print(distinct(['a','ab','a','ab']))

# %%esercizio_4
"""
4. search(lst, andc, orc, notc) ritorna una nuova lista di stringhe che contiene le stringhe s della lista
   lst tali che tutte le stringhe della lista andc sono sottostringhe di s, almeno una delle stringhe della
   lista orc (se orc non è vuota) è una sottostringa di s e nessuna delle stringhe della lista notc è una
   sottostringa di s. 
   Esempi, sia lst = ['mela','pera','melo']
   search(lst,['el','a'],['ra','pe','m'],['tt','lo'])	ritorna ['mela']
   search(lst,[],['ra','pe','m'],['tt','lo'])		ritorna ['mela','pera']
   search(lst,['el','a'],[],['tt''lo'])			ritorna ['mela']
   search(lst,[],['ra','pe','m'],[])			ritorna ['mela','pera','melo']
"""

# definisco la funzione richiesta
def search(lst, andc, orc, notc):
    # imposto risultato vuota
    risultato = []
    # per ogni stringa di lst
    for stringa in lst:
        # controllo tutte le condizioni con una funzione
        if check_all(stringa, andc, orc, notc):
            # se True l'aggiungo al risultato
            risultato.append(stringa)
    # ritorno risultato
    return risultato

# definisco check_all
def check_all(stringa, andc, orc, notc):
    # ritorna il check delle tre condizionim
    return check_andc(stringa, andc) and check_orc(stringa, orc) and check_notc(stringa, notc)

# definisco check_andc
def check_andc(stringa, andc):
    # verifichiamo che gli elementi di andc sinno presenti tutti in stringa
    for s in andc:
        if s not in stringa:
            # se s non è in stringa possiamo già uscire
            return False
    # se il ciclo si conclude, torniamo True
    return True

# definisco check_orc
def check_orc(stringa, orc):
    # se orc è vuoto, non c'è altro da fare
    if orc == []:
        return True
    # verifichiamo che almeno uno degli elementi di orc sin presente in stringa
    for s in orc:
        if s in stringa:
            # se s è in stringa possiamo  uscire
            return True
    # se il ciclo si conclude, torniamo False
    return False

# definisco check_notc
def check_notc(stringa, notc):
    # verifichiamo che neanche un elemento di notc sia in stringa
    for s in notc:
        if s in stringa:
            # se s è in stringa possiamo già uscire
            return False
    # se il ciclo si conclude, torniamo True
    return True

# imposto lst per le prove
lst = ['mela','pera','melo']

# stampo le prove
print(search(lst, ['el', 'a'], ['ra', 'pe', 'm'], ['tt', 'lo']))
print(search(lst, [], ['ra', 'pe', 'm'], ['tt', 'lo']))
print(search(lst, ['el', 'a'], [], ['tt', 'lo']))
print(search(lst, [], ['ra', 'pe', 'm'], []))