# -*- coding: utf-8 -*-


# %%esercizio_01
"""
1. Contrasto dei colori dell'intera immagine, come da lezione precedente,
   usando le operazioni aritmetiche sui colori. Introdurre un metodo per
   correggere i colori fuori scala.
"""

# "adatto" la funzione della lezione 12
class Image(object):
    
    def contrast(self, c):
        res = Image(self.width(), self.height())
        for x in range(self.width()):
            for y in range(self.height()):
                color = self.get_pixel(x, y).contrast(c)
                res.set_pixel(x, y, color)
        return res
    
class Color:
    
    def _bounded(self):
        self.r = max(min(self.r, 255), 0)
        self.g = max(min(self.g, 255), 0)
        self.b = max(min(self.b, 255), 0)
        return self
    def contrast(self, c):
         grey = Color(128, 128, 128)
         return ((self - grey) * c) + grey._bounded()
     
     
# %%esercizio_02
"""
2. Generare mosaici, come da lezione precedente, introducendo un metodo per
   calcolare la media dei colori in un quadratino dell'immagine.
"""

# anche qui mi basterà adattare la funzione mosaic_average
class Image:
    
    def mosaic_average(self, s):
        mosaic = Image(self.width(), self.height())
        for x in range(0, self.width() + s, s):
            for y in range(0, self.height() + s, s):
                color = self._average_color(x, y, s, s)
                mosaic.draw_quad(x, y, s, s, color)
        return mosaic
    
    def _average_color(self, x, y, w, h):
        sum_c = Color(0, 0, 0)
        n = 0
        for i in range(x, min(x + w, self.width())):
            for j in range(y, min(y + h, self.height())):
                sum_c += self.get_pixel(i,j)
                n += 1
        return sum_c * (1 / n) if n else sum_c
    
    
# %%esercizio_03
"""
3. Introdurre la copia di parte di un'immagine su un'altra,
   come da lezione precedente.
"""

# vedi sopra
class Image:
    
    def copy(self, dest_img, xs, ys, xd, yd, w, h):
        for i in range(w):
            for j in range(h):
                pixel = self.get_pixel(xs + i, ys + j)
                dest_img.set_pixel(xd + i, yd + j, pixel)