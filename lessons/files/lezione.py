#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:02:45 2018

@author: andrea
"""

import image

class Color:
    """Classe che rappresenta un pixel RGB"""
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def inverse(self):
        "calcola il colore inverso (negativo)"
        return Color(255 - self.r, 255 - self.g, 255 - self.b)
    
    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b+other.b)

    def __mul__(self, f):
        return Color(self.r*f, self.g*f, self.b*f)

    def __repr__(self):
        return 'Color({0.r}, {0.g}, {0.b})'.format(self)

    def bound(self):
        def _bound(v):
            return int(min(255, max(0, round(v))))        
        self.r = _bound(self.r)
        self.g = _bound(self.g)
        self.b = _bound(self.b)

    def to_tuple(self):
        return self.r, self.g, self.b
    def set_color(self, other):
        self.r = other.r
        self.g = other.g
        self.b = other.b

class Image:
    """Classe che rappresenta una immagine RGB"""
    def __init__(self, w, h):
        """Costruisco una immagine w x h di pixel neri"""
        self._pixels = [
                [ Color(0, 0, 0) for _ in range(w)] 
                for _ in range(h)
                ]
    def width(self):
        return len(self._pixels[0])
    def height(self):
        return len(self._pixels)
    def __str__(self):
        return 'Image({},{})'.format(self.width(),self.height() )
    def set_pixel(self, x, y, c):
        if 0 <= x < self.width() and 0 <= y < self.height():
            self._pixels[y][x].set_color(c)
    def get_pixel(self, x, y):
        if 0 <= x < self.width() and 0 <= y < self.height():
            return self._pixels[y][x]
        else:
            return Color(0,0,0)
    def to_img(self):
        return [ [ c.to_tuple() for c in riga ] for riga in self._pixels ]
    
    def save(self, filename):
        img = self.to_img()
        image.save(filename, img)
    
    def visd(self, msg=''):
        image.visd(self.to_img(), msg)

    def draw_quad(self, x, y, w, h, c):
        for xx in range(x, x+w):
            for yy in range(y, y+h):
                self.set_pixel(xx, yy, c)
    
    def draw_gradienth(self, c0, c1):
        for x in range(self.width()):
            u = x / self.width()
            c = c0*(1-u)+c1*u
            c.bound()
            for y in range(self.height()):
                self.set_pixel(x, y, c)
    
    def draw_gradientv(self, c0, c1):
        for y in range(self.height()):
            u = y / self.height()
            c = c0*(1-u)+c1*u
            c.bound()
            for x in range(self.width()):
                self.set_pixel(x, y, c)

    def draw_gradientq(self, c00, c01, c10, c11):
        for y in range(self.height()):
            for x in range(self.width()):
                u = x/self.width()
                v = y/self.height()
                c = c00*(1-u)*(1-v) + c01*(1-u)*v + c10*u*(1-v) + c11*u*v
                c.bound()
                self.set_pixel(x, y, c)

    
    def inverse(self):
        img = Image(self.width(), self.height())
        for x in range(self.width()):
            for y in range(self.height()):
                img.set_pixel(x, y, self.get_pixel(x, y).inverse())
        return img
    
    
