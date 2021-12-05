# -*- coding: utf-8 -*-


""" LEZIONE 17 - ALBERI E RICORSIONE """

import os
import os.path

# %%esercizio_01
"""
1. countf(path) che preso in input il percorso path di un file o directory
   ritorna il numero totale di file contenuti a qualsiasi livello nella
   directory (se è una directory). Esempi
>>> countf('Informatica')					ritorna 27
>>> countf('Informatica/Software')				ritorna 19
>>> countf('Informatica/Hardware/Architetture/cache.txt')	ritorna  1
"""


def countf(path):
    # inizializzo il contatore
    count = 0
    # trovo il basename
    basename = os.path.basename(path)
    # casi base 1 e 2
    # se il file (o la dir) è nascosto/speiale o non esiste
    if basename[0] == '.' or not os.path.exists(path):
        # ritorno 0
        return 0
    # caso base 3
    # altrimenti, se path è un file
    elif os.path.isfile(path):
        # ritorno 1
        return 1
    # altrimenti è una dir
    else:
        # ne scandisco i nodi
        for node in os.listdir(path):
            # creo il nuovo percorso
            new_path = os.path.join(path, node)
            # e vado in ricorsione
            count += countf(new_path)
    # ritorno count
    return count


# prove
print(countf('files/Informatica'))
print(countf('files/Informatica/Software'))
print(countf('files/Informatica/Hardware/Architetture/cache.txt'))


# %%esercizio_02
"""
2. maxlev(path) che preso in input il percorso path di un file o directory
   ritorna il massimo livello dell'albero dei file e directory contenute nella
   directory (se è una directory). Esempi

>>> maxlev('Informatica')					ritorna 7
>>> maxlev('Informatica/Teoria')				ritorna 0	(non esiste)
>>> maxlev('Informatica/Hardware')				ritorna 6
>>> maxlev('Informatica/Software/SistemiOperativi/Linux.txt')	ritorna 1
"""


def maxlev(path):
    # trovo il basename
    basename = os.path.basename(path)
    # casi base 1 e 2
    # se il file (o la dir) è nascosto/speiale o non esiste
    if basename[0] == '.' or not os.path.exists(path):
        # ritorno 0
        return 0
    # caso base 3
    # altrimenti, se path è un file
    elif os.path.isfile(path):
        # ritorno 1
        return 1
    # altrimenti è una dir
    else:
        # creo una lista per ogni ricorsione
        levels = [maxlev(os.path.join(path, node))
                  for node in os.listdir(path)]
        # se la lista ha almeno un elemento
        if levels:
            # ritorno 1 più il valore più alto
            return 1 + max(levels)
        else:
            # ritorno 1
            return 1


# prove
print(maxlev('files/Informatica'))
print(maxlev('files/Informatica/Teoria'))
print(maxlev('files/Informatica/Hardware'))
print(maxlev('files/Informatica/Software/SistemiOperativi/Linux.txt'))


# %%esercizio_03
"""
3. permute_d(seq) ritorna una lista di tutte le permutazioni della sequenza
   seq, senza duplicati. Esempio
>>> permutazioni('ala')		ritorna ['ala', 'aal', 'laa', 'laa', 'aal', 'ala']
>>> permute_d('ala')		ritorna ['ala', 'aal', 'laa']
"""


def permute_d(seq):
    # caso base 1
    # la sequenza non è valida
    if not seq:
        # ritorno lista vuota
        return []
    # caso base 2
    # la sequenza è lunga 1
    elif len(seq) == 1:
        # ritorno l'unico elemento
        return [seq]
    # altrimenti
    else:
        # creo un set degli elementi già visti
        done = set()
        # inizializzo la lista delle permutazioni
        permutations = []
        # scorro la sequenza
        for i in range(len(seq)):
            el = seq[i]
            # se el non è nel set
            if el not in done:
                # lo aggiungo
                done.add(el)
                # ottengo il resto della sequenza
                sub_seq = seq[:i] + seq[i+1:]
                # ne calcolo le permutazione
                sub_permutations = permute_d(sub_seq)
                # e gli aggiungo el
                for permutation in sub_permutations:
                    permutations.append(el + permutation)
    # ritorno permutations
    return permutations


# prova
print(permute_d('ala'))


# %%esercizio_04
"""
4. change(r, coins) ritorna il numero di combinazioni diverse di dare il resto
   r con i valori delle monete nella lista coins. Si assume che coins contenga
   sempre il valore 1 e che sia ordinata in senso crescente. Esempi
>>> change(8, [1, 5])			ritorna 2 infatti abbiamo 1+1+1+1+1+1+1+1 e 1+1+1+5
>>> change(15, [1, 5, 10])		ritorna 6
>>> change(100, [1, 5, 10, 20, 50])	ritorna 343

Suggerimento: conviene contare le combinazioni "generandole" con i valori
ordinati in senso crescente (per evitare di contare due volte la stessa
combinazione); generare tutte quelle che iniziano con il primo valore, poi
quelle che iniziano con il secondo valore e così via.
"""


def change(r, coins):
    return len(get_comb(r, coins))


def get_comb(r, coins):
    # se r è = 0, ritorno una soluzione
    if r == 0:
        return [[]]
    # se coins è vuota, ritorno lista vuota
    if not coins:
        return []
    # seleziono la prima moneta
    c = coins[0]
    # e il resto
    other_c = coins[1:]
    # se c > r, ritorno lista vuota
    if c > r:
        return []
    # inizializzo la lista comb
    comb_n = []
    # e la lista dei tagli usati
    used_c = []
    # uso un r di appoggio
    new_r = r
    # finché new_r è >= c
    while (new_r >= c):
        # aggiungo c ai tagli usati
        used_c.append(c)
        # e la sottraggo
        new_r -= c
        # cerco le sub con gli altri tagli
        sub_comb_n = get_comb(new_r, other_c)
        # e per ogni sub
        for comb in sub_comb_n:
            # aggiungo i tagli già usati
            comb_n.append(used_c + comb)
    # infine
    sub_comb_n = get_comb(r, other_c)
    comb_n += sub_comb_n
    return comb_n


# prove
print(change(8, [1, 5]))
print(change(8, [1, 5]))
print(change(8, [1, 5]))


# %%esercizio_05
"""
5. node_fstree(root, path) ritorna il nodo dell'albero di radice tree (di tipo
   FSNode ) che ha il path uguale a quello di input. Se non c'è, ritorna None.
   Esempi
>>> tree = gen_fstree('Informatica')
>>> node_fstree(tree, 'Informatica')
FSNode("Informatica", False)
>>> node_fstree(tree, 'Informatica/Hardware/Architetture')
FSNode("Informatica/Hardware/Architetture", False)
>>> print(repr(node_fstree(tree, 'Informatica/Software/Android')))
None
"""


# importo parte del codice usato a lezione

class FSNode(object):
    def __init__(self, path, isFile):
        self.isFile = isFile		# si tratta di un file (True) o una dir (False)
        self.path = path			# percorso nel file-system del file
        self.content = []		# lista dei nodi figli, inizialmente vuota

    def __str__(self):			# come sua rappresentazione come stringa
        return self.path			# prendiamo direttamente il path

    def __repr__(self):			# come rappresentazione adatta a costruirne uno
        # torniamo una stringa simile alla chiamata del costruttore
        return 'FSNode("{0.path}", {0.isFile})'.format(self)


def gen_fstree(path):
    '''Genera l'albero partendo dal percorso path e ritorna il nodo radice'''
    if os.path.isdir(path):                 # se è una directory
        root = FSNode(path, False)				# è una dir
        for name in os.listdir(path):			# per ogni file/dir contenuto
            if not name.startswith('.'):		      	# (se non è invisibile)
                # aggiungo ricorsivamente i nodi corrispondenti
                root.content += [gen_fstree(os.path.join(path, name))]
    else:
        root = FSNode(path, True)				# è un file
    return root


def node_fstree(root, path):
    # se il path è uguale all'albero, ritorno lo stesso
    if root.path == path:
        return root
    # altrimenti cerco nei sotto alberi
    for sub_root in root.content:
        found = node_fstree(sub_root, path)
        # e ritorno
        if found:
            return found
    # altrimenti torno NONE
    return None


# prove
tree = gen_fstree('files/Informatica')
print(node_fstree(tree, 'files/Informatica'))
tree2 = gen_fstree('files/Informatica/Hardware/Architetture')
print(node_fstree(tree2, 'files/Informatica/Hardware/Architetture'))
tree3 = gen_fstree('files/Informatica/Software/Android')
print(node_fstree(tree, 'files/Informatica/Software/Android'))


# %%esercizio_06
"""
6. file_fstree(root) ritorna una lista contenente i percorsi di tutti i file
   (no directory) contenuti nell'albero di radice root (di tipo FSNode).
   Esempio
>>> tree = gen_fstree('Informatica')
>>> subtree = node_fstree(tree, 'Informatica/Hardware')
>>> file_fstree(subtree)
['Informatica/Hardware/Architetture/cache.txt',
'Informatica/Hardware/Architetture/memorie.txt',
'Informatica/Hardware/Architetture/Processori/CISC/x86/AMD_Phenom.txt',
'Informatica/Hardware/Architetture/Processori/CISC/x86/Intel_Haswell.txt',
'Informatica/Hardware/Architetture/Processori/CISC/x86/Pentium4.txt',
'Informatica/Hardware/Architetture/Processori/RISC/ARM.txt',
'Informatica/Hardware/Architetture/Processori/RISC/MIPS.txt',
'Informatica/Hardware/Architetture/storia.txt']
"""


def file_fstree(root):
    # caso base: root è già un file
    if root.isFile:
        return [root.path]
    # inizializzo la lista
    files_path = []
    # per ogni dir, cerco ricorsivamente i file
    for directory in root.content:
        files_path += file_fstree(directory)
    return files_path


# prove
tree = gen_fstree('files/Informatica')
subtree = node_fstree(tree, 'files/Informatica/Hardware')
print(file_fstree(subtree))


# %%esercizio_07
"""
7. size_fstree(root) ritorna un dizionario che associa ad ogni percorso di
   directory nell'albero di radice root (di tipo FSNode ) il numero di nodi del
   suo sottoalbero (cioè il numero di directory e file contenuti a qualsiasi
   livello nella directory). Se il nodo root rappresenta un file, ritorna un
   dizionario vuoto. Esempio
>>> tree = gen_fstree('Informatica')
>>> size_fstree(tree)
{'Informatica': 40,
 'Informatica/Hardware': 13,
 'Informatica/Hardware/Architetture': 12,
 'Informatica/Hardware/Architetture/Processori': 8,
 'Informatica/Hardware/Architetture/Processori/CISC': 4,
 'Informatica/Hardware/Architetture/Processori/CISC/x86': 3,
 'Informatica/Hardware/Architetture/Processori/RISC': 2,
 'Informatica/Software': 25,
 'Informatica/Software/Linguaggi': 17,
 'Informatica/Software/Linguaggi/Imperativi': 4,
 'Informatica/Software/Linguaggi/OO': 5,
 'Informatica/Software/Linguaggi/Funzionali': 4,
 'Informatica/Software/SistemiOperativi': 5,
 'Informatica/Software/BasiDati': 0}
"""


def size_fstree(root):
    # se root è un file, ritorno dizionario vuoto
    if root.isFile:
        return {}
    # inizializzo il dizionario
    root_dict = {root.path: 0}
    # e per ogni sub dir, ripeto il conteggio
    for sub_tree in root.content:
        sub_size = size_fstree(sub_tree)
        root_dict.update(sub_size)
        root_dict[root.path] += sub_size.get(sub_tree.path, 0) + 1
    return root_dict


# prove
tree = gen_fstree('files/Informatica')
print(size_fstree(tree))
