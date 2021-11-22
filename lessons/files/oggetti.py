
import image

class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def inverse(self):
        return Color( 255-self.r, 255-self.g, 255-self.b)
    def __add__(self, other):
        return Color( self.r + other.r, self.g + other.g, self.b + other.b )
    def __str__(self):
        return "Color({0.r}, {0.g}, {0.b})".format(self)
    def __mul__(self, f):
        return Color(round(self.r * f), round(self.g * f), round(self.b * f)) 
    def to_tuple(self):
        return self.r, self.g, self.b

class Image(object):
    def __init__(self, w, h):
        self._pixels = [ [ Color(0,0,0) for _ in range(w)] for _ in range(h) ]
    def width(self):
        return len(self._pixels[0])
    def height(self):
        return len(self._pixels)
    def set_pixel(self,i,j,color):
        if 0 <= i < self.width() and 0 <= j < self.height():
            self._pixels[j][i].r = color.r
            self._pixels[j][i].g = color.g
            self._pixels[j][i].b = color.b
    def get_pixel(self,i,j):
        if 0 <= i < self.width() and 0 <= j < self.height():
            return self._pixels[j][i]
    def load(self,filename):
        img = image.load(filename)
        self._pixels = [ [ Color(*c) for c in line ] for line in img ]
    def to_img(self):
        return [ [ c.to_tuple() for c in line ] for line in self._pixels ]
    def save(self,filename):
        image.save(filename, self.to_img())
    def visd(self, msg=None):
        image.visd(self.to_img(), msg)
    def __str__(self):
        return 'Image@'+str(self.width())+'x'+str(self.height())

    def draw_quad(self, x, y, w, h, c):
        for j in range(y, y+h):
            for i in range(x, x+w):
                self.set_pixel(i,j,c)
    def draw_gradienth(self, c0, c1):
        for j in range(self.height()):
            for i in range(self.width()):
                u = i / self.width()
                self.set_pixel(i,j,c0*(1-u)+c1*u)
    def draw_gradientv(self, c0, c1):
        for j in range(self.height()):
            for i in range(self.width()):
                v = j / self.height()
                self.set_pixel(i,j,c0*(1-v)+c1*v)
    def draw_gradientq(self, c00, c01, c10, c11):
        for j in range(self.height()):
            for i in range(self.width()):
                u = i / self.width()
                v = j / self.height()
                self.set_pixel(i,j,c00*(1-u)*(1-v)+ c01*(1-u)*v+c10*u*(1-v)+c11*u*v)

if __name__ == '__main__':

    img = Image(256,256)
    
    img.draw_quad(32,32,64,64,Color(255,128,0))
    img.draw_quad(160,160,64,64,Color(255,128,0))
    img.save('img_quad.png')
    
    img = Image(256,256)
    img.draw_gradienth(Color(255,0,0),Color(0,255,0))
    img.save('img_gradh.png')
    
    img = Image(256,256)
    img.draw_gradientv(Color(255,0,0),Color(0,255,0))
    img.save('img_gradv.png')
    
    img = Image(256,256)
    img.draw_gradientq(Color(255,0,0),Color(0,255,0),
    Color(0,0,255),Color(0,0,0))
    img.save('img_gradq.png')
    
