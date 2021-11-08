# -*- coding: utf-8 -*-

# %%esercizio_1
"""
1. size(ll) prende in input una lista di liste ll e ritorna il numero di righe,
   la lunghezza mimima e massima delle righe e il numero totale di elementi. 
   
   Esempio
>>> size([[1,2,3],['a','b'],[1,2,'A',4,5]]) 
(3, 2, 5, 10)
"""

def size(ll):
    # per il numero di righe mi basta calcolare la lunghezza di ll
    n_rows = len(ll)
    # per la lunghezza minima e massima uso la key len su min e max
    min_l = len(min(ll, key = len))
    max_l = len(max(ll, key = len))
    # per il numero totale degli elementi, sommo le singole len
    tot_l = sum([len(row) for row in ll])
    # ritorno tutti
    return n_rows, min_l, max_l, tot_l

# prova
print(size([[1,2,3],['a','b'],[1,2,'A',4,5]]))

# %%esercizio_2
"""
2. draw_h_line(img, x, y, w, c) che disegna sulla immagine img una linea
   orizzontale che parte dalla coordinata x, y, di lunghezza w e colore c
   senza sbordare.

   Esempio
>>> import image as im
>>> img = im.create(500,150,(0,255,0))
>>> draw_h_line(img, 100, 50,  300, (255, 0, 0) )
>>> draw_h_line(img,  50, 100, 700, (0, 0, 255) )
>>> im.visd(img)

mostra l'immagine del file es2-1.png
"""

# definisco una funzione "inside" per non sbordare
def inside(img, i, j):
    # ritorna True se il pixel (i, j) e' dentro l'immagine img
    iw, ih = len(img[0]), len(img)
    return 0 <= i < iw and 0 <= j < ih

# definisco la funzione richiesta
def draw_h_line(img, x, y, w, c):
    # mi posiziono alla posizione e inizio a colorare
    for i in range(x, x+w):
        # controllo se sono dentro
        if inside(img, i, y):
            # se ci sono, coloro
            img[y][i] = c
            
# imposto per la prova
from files import image as im
img = im.create(500,150,(0,255,0))

# provo la funzione
draw_h_line(img, 100, 50,  300, (255, 0, 0) )
draw_h_line(img,  50, 100, 700, (0, 0, 255) )

# visualizzo l'immagine
im.visd(img)

# %%esercizio_3
"""
3. draw_v_line(img, x, y, h, c) che disegna sulla immagine img una linea
   verticale che parte dalla coordinata x, y, di altezza w e colore c
   senza sbordare.

   Esempio
>>> import image as im
>>> img = im.create(500,150,(0,0,0))
>>> draw_v_line(img, 100, 50,  300, (255, 0, 0) )
>>> draw_v_line(img,  50, 100, 700, (0, 0, 255) )
>>> im.visd(img)

mostra una immagine uguale al file es3-1.png
"""

# prendo come base la funzione dell'esercizio precedente
# e ne sostituisco solo gli elementi per renderla "verticale"
def draw_v_line(img, x, y, h, c):
    # mi posiziono alla posizione e inizio a colorare
    for i in range(y, y+h):
        # controllo se sono dentro
        if inside(img, x, i):
            # se ci sono, coloro
            img[i][x] = c

# imposto per la prova
img = im.create(500,150,(0,0,0))

# provo la funzione
draw_v_line(img, 100, 50,  300, (255, 0, 0) )
draw_v_line(img,  50, 100, 700, (0, 0, 255) )

# visualizzo l'immagine
im.visd(img)

# %%esercizio_4
"""
4. draw_quad_out(img, x1, y1, x2, y2, c) disegna sull'immagine img
   il contorno di un rettangolo di colore c che ha lo spigolo in alto
   a sinistra in (x1, y1) e quello in basso a destra in (x2, y2) . 
   
   Esempi
>>> import image as im
>>> img = im.create(300,150,(0,0,0))
>>> draw_quad_out(img,  50,  20, 100,140,(255,128,0))
>>> im.visd(img)
>>> draw_quad_out(img, 120, -10, 180, 70, (255,255,255))
>>> im.visd(img)
>>> draw_quad_out(img, 140,  40, 320, 120, (80,80,255))
>>> im.visd(img)

mostra immagini uguali a quelle allegate es4-1.png, es4-2.png, es4-3.png
"""

def draw_quad_out(img, x1, y1, x2, y2, c):
    # definisco larghezza e altezza
    w = x2 -x1
    h = y2 - y1
    # richiamo le funzioni precedenti per ogni lato
    # base superiore
    draw_h_line(img, x1, y1, w, c)
    # base inferiore
    draw_h_line(img, x1, y2, w, c)
    # lato sx
    draw_v_line(img, x1, y1, h, c)
    # lato dx
    draw_v_line(img, x2, y1, h, c)
    
# imposto le prove
img = im.create(300,150,(0,0,0))

# prova 1
draw_quad_out(img,  50,  20, 100,140,(255,128,0))
im.visd(img)

# prova 2
draw_quad_out(img, 120, -10, 180, 70, (255,255,255))
im.visd(img)

# prova 3
draw_quad_out(img, 140,  40, 320, 120, (80,80,255))
im.visd(img)

# %%esercizio_5
"""
5. draw_grid(img, s, c) disegna sull'immagine img una griglia di linee
   orizzontali e verticali di colore c separate da s pixels le une dalle altre.
   Questo significa che se s è zero, le linee sono adiacenti.
   
   Esempi
>>> img = im.create(200, 100, (200,200,200))
>>> draw_grid(img, 2, (0,0,0))
>>> im.visd(img)

mostra una immagine uguale al file es5-1.png

>>> img = im.create(400, 200, (240,240,240))
>>> for k in range(6):
...     s = int(8*(1.5**k))
...     c = 200 - 40*k
...     draw_grid(img, s, (c, c, c))
>>> im.visd(img)

mostra una immagine uguale al file es5-2.png
"""

# definisco la funzione con h_line e v_line come base
def draw_grid(img, s, c):
    # altezza e larghezza corrispondono con img
    w, h = len(img[0]), len(img)
    # disegno linee orizzontali a intervalli di s
    for y in range(0, h, s+1):
        draw_h_line(img, 0, y, w, c)
    # idem con le verticali
    for x in range(0, w, s+1):
        draw_v_line(img, x, 0, h, c)
            
# prova 1        
img = im.create(200, 100, (200,200,200))
draw_grid(img, 2, (0,0,0))
im.visd(img)

# prova 2
img = im.create(400, 200, (240,240,240))
for k in range(6):
    s = int(8*(1.5**k))
    c = 200 - 40*k
    draw_grid(img, s, (c, c, c))
im.visd(img)