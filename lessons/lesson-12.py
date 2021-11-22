# -*- coding: utf-8 -*-

# %%esercizio_01
"""
1. rotL90(img) ritorna una nuova immagine che è l'immagine img ruotata a sinistra di 90 gradi. 
   Esempio: nel file es1.png vedete come l'immagine img_in_01.png viene ruotata
"""

# importo il modulo image
from files import image as im

# definisco la funzione
def rotL90(img):
    # imposto larghezza e altezza (len della matrice)
    w, h = len(img[0]), len(img)
    # creo la base dell'immagine ruotata
    ret = im.create(h, w, (0,0,0))
    # per ogni punto (x, y)
    for y in range(h):
        for x in range(w):
            # per ruotare di 90 gradi a sinistra scambio x e y con le x che decrescono
            ret[x][y] = img[y][w-x-1]
    # ritorno la nuova immagine
    return ret

# prova
img = im.load('files/img_in_01.png')
im.visd(img)
rot_90_img = rotL90(img)
im.visd(rot_90_img)

# %%esercizio_2
"""
2. red(img, s) ritorna una nuova immagine che è l'immagine img ridotta di un fattore s . Si assume che
   s sia un intero positvo che divide esattamente sia la larghezza che l'altezza di img . 
   Per calcolare il colore di un pixel dell'immagine ridotta si usi la tecnica di mosaic_average() . 
   Ad esempio, red(img, 2) e red(img, 4) , dove img è l'immagine img_in_01.png , 
   producono le immagini es2_1.png e es2_2.png
"""

# copio mosaic_average ma elimino la parte della ripetizione
def red(img, s):
    h, w = len(img), len(img[0])
    ret = im.create(w // s, h  // s ,(0,0,0))
    for jj in range(h//s):
        for ii in range(w//s):
            c = [0,0,0]
            n = 0
            for j in range(jj*s,(jj+1)*s):
                for i in range(ii*s,(ii+1)*s):
                    if im.inside(img, i, j):
                        n += 1
                        for idx in range(3):
                            c[idx] += img[j][i][idx]
            for idx in range(3):
                col = round(c[idx] / n)
                col = min(max(col, 0), 255)
                c[idx] = col
            ret[jj][ii] = tuple(c)
    return ret

# prova (stampo le dimensioni per verificare)
img = im.load('files/img_in_01.png')
im.visd(img)
print(len(img), len(img[0]))
red_2 = red(img, 2)
im.visd(red_2)
print(len(red_2), len(red_2[0]))
red_4 = red(img, 4)
im.visd(red_4)
print(len(red_4), len(red_4[0]))

# %%esercizio_3
"""
3. mult(img, s) ritorna una nuova immagine, con le stesse dimensioni di img , che contiene s x s copie
   ridotte di img . Si assume che s è un intero positvo che divide esattamente sia la larghezza che l'altezza
   di img . 
   Esempi, se img è l'immagine img_in_01.png , mult(img, 2) e mult(img, 4) producono, rispettivamente,
   le immagini dei file es3_1.png ed es3_2.png
"""

# definisco la funzione
def mult(img, s):
    # imposto le dimensioni
    w, h = len(img[0]), len(img)
    smallw, smallh = w//s, h//s
    # riduco l'immagine con la funzione dell'esercizio precedente
    small = red(img, s)
    # creo la nuova immagine
    res = im.create(w, h, im.black)
    for y in range(0, h, smallh):
        for x in range(0, w, smallw):
            im.copy(res, small, x, y, 0, 0, smallw, smallh)
    return res

# prove
img = im.load('files/img_in_01.png')
im.visd(img)
mul2 = mult(img, 2)
im.visd(mul2)
mul4 = mult(img, 4)
im.visd(mul4)

# %%esercizio_4
"""
4. gray(img) ritorna una nuova immagine ottenuta trasformando i colori di img in livelli di grigio. 
   Ad esempio, se applicata alla solita immagine produce l'immagine es4_1.png
"""

def gray(img):
    # ottengo le dimensioni
    h, w = len(img), len(img[0])
    # creo la nuova immagine
    gray_img = im.create(w, h, im.black)
    # per ogni pixel
    for x in range(w):
        for y in range(h):
            # calcolo la media dei tre colori
            c = sum(img[y][x]) // 3
            # e l'assegno
            gray_img[y][x] = c, c, c
    # ritorno l'immagine
    return gray_img

# prove
img = im.load('files/img_in_01.png')
im.visd(img)
gray_img = gray(img)
im.visd(gray_img)

# %%esercizio_5
"""
5. patchwork(img, s) ritorna un nuova immagine ottenuta dividendo l'immagine img in quadratini di
   lato s e su ognuno di questi applicando in modo casuale una delle seguenti trasformazioni: 
   - identità (cioè il quadratino è lasciato invariato), 
   - invert() , 
   - contrast() con c = 0.5 , 
   - contrast() con c = 2.0
   - e gray() . 
   Ad esempio, se img è l'immagine img_in_01.png , patchwork(img, 64) e patchwork(img, 16) producono, 
   rispettivamente immagini simili alle es5_1.png e es5_2.png
"""
import random

def patchwork(img, s):
    # dimensioni
    w, h = len(img[0]), len(img)
    # nuova immagine
    patched = im.create(w, h, im.black)
    # per ogni pixel di una sezione
    for x in range(w // s):
        for y in range(h // s):
            # creo la sezione
            section = im.create(s, s, im.black)
            im.copy(section, img, 0, 0, x * s, y * s, s, s)
            # randomizzo le scelte
            r = random.randint(1, 5)
            if r == 1:
                pass
            elif r == 2:
                section = im.invert(section)
            elif r == 3:
                section = im.contrast(section, 0.5)
            elif r == 4:
                section = im.contrast(section, 2.0)
            else:
                section = gray(section)
            im.copy(patched, section, x * s, y * s, 0, 0, s, s)
    return patched

# prove
patch64 = patchwork(img, 64)
im.visd(patch64)

patch16 = patchwork(img, 16)
im.visd(patch16)

# %%esercizio_06
"""
6. edge(img, t, bg) ritorna una nuova immagine ottenuta dall'immagine img colorando con il colore
   nero i pixel di confine tra zone di colore significativamente differente. Il parametro t è la soglia minima
   (un float tra 0.0 e 1.0) della differenza di colore affinché un pixel sia considerato di confine. 
   Se bg = None , i pixel non di confine sono lasciati con i colori originali, altrimenti sono colorati con il colore bg .

   Per determinare se un pixel p è di confine si controlla se nell'intorno di p (cioè gli 8 pixel adiacenti per
   lato o spigolo a p) c'è almeno un pixel la cui distanza normalizzata da p è maggiore o uguale a t ed è più
   chiaro di p . Come distanza normalizzata si può usare la somma delle differenze assolute delle tre
   componenti colore diviso per 765 (=3*255). 

   Esempi, sia img e img2 le immagini img_in_01.png e img_in_02.png , 
   edge(img, 0.1, None), edge(img, 0,05, None), edge(img2, 0.2, (240,240,240)) ed edge(img2, 0.15, (240,240,240)) 
   producono rispettivamente le immagini es6_1.png, es6_2.png, es6_3.png, es6_4.png
"""

def edge(img, t, bg):
    w, h = len(img[0]), len(img)
    edged_img = im.create(w, h, im.black)
    # nel range escludiamo un pixel di "confine"
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            # salvo il primo colore
            c0 = img[y][x]
            # default per i pixel vicini
            on_edge = False
            # controllo i pixel adiacenti
            for yy in range(-1, 2):
                for xx in range(-1, 2):
                    # escludo lo stesso
                    if xx or yy:
                        # controllo il colore
                        c1 = img[y + yy][x + xx]
                        # verifico il bordo
                        on_edge |= is_on_edge(c0, c1, t)
            # applico le condizioni
            if on_edge:
                edged_img[y][x] = im.black
            elif bg:	
                edged_img[y][x] = bg
            else:
                edged_img[y][x] = img[y][x]
    return edged_img

# controllo del "confine"
def is_on_edge(p0, p1, t):
    sub = 0
    for i in range(3):
        sub += abs(p0[i] - p1[i])
    return sub / (3 * 255) >= t and sum(p0) > sum(p1)

# prove
test1 = edge(img, 0.1, None)
im.visd(test1)

test2 = edge(img, 0.05, None)
im.visd(test2)

img2 = im.load('files/img_in_02.png')
im.visd(img2)

test3 = edge(img2, 0.2, (240,240,240))
im.visd(test3)

test4 = edge(img2, 0.15, (240,240,240))
im.visd(test4)