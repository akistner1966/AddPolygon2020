# -*- coding: utf-8 -*-
#@author: comet

class linie(object):
    def __init__(self, xa, ya, xe, ye):
        self.xa = xa
        self.ya = ya
        self.xe = xe
        self.ye = ye
        
    def steigung(self):
        if self.xa == self.xe: #senkrechte Gerade
            return(None)
        else:
            return((self.ya - self.ye)/(self.xa - self.xe))
        
    def xlcheck(self, _x2a, _y2a, _x2e, _y2e):
        """
        Quelle: https://de.wikipedia.org/wiki/Schnittpunkt
        Gerade 1: wurde in __init__ definiert
        Gerade 2: <_x2a>, <_y2a> - <_x2e>, <_y2e>
    
        Rückgabewerte:
        <crosscheck>
        1 genau ein Schnittpunkt
        0 kein Schnittpunkt (parallele, nicht identische Geraden)
        -1 unendlich viele Schnittpunkte (identische Geraden)
        <xs> x-Koordintate des Schnittpunkts
        <ys> y-Koordintate des Schnittpunkts
        """
        dx1 = self.xe - self.xa
        dy1 = self.ye - self.ya
        zx = (_x2e  -_x2a)*(self.xe*self.ya - self.xa*self.ye)
        zx -= (self.xe - self.xa)*(_x2e*_y2a - _x2a*_y2e)
        nx = (_y2e - _y2a)*(self.xe - self.xa)
        nx -= (self.ye - self.ya)*(_x2e - _x2a)
        zy = (self.ya - self.ye)*(_x2e*_y2a - _x2a*_y2e)
        zy -= (_y2a - _y2e)*(self.xe*self.ya - self.xa*self.ye)
        ny = nx
        if nx != 0:
            crosscheck = False
            xs = zx/nx
            ys = zy/ny
            dxs = xs - self.xa
            dys = ys - self.ya
            if dxs == 0: #senkrechte Gerade => alternativer Check
                lbda = dys/dy1
            else:
                lbda = dxs/dx1
            if (lbda >=0) and (lbda <= 1):
                crosscheck = True
        else: #parallel oder identisch?
            if dx1 == 0: #Sonderfall senkrechte Geraden
                if self.xa == _x2a: #identische Geraden
                    crosscheck = -1
                    xs = ys = 0
                else: #parallele Geraden
                    crosscheck = 0
                    xs = ys = 0
            elif dy1 == 0: #Sonderfall waagerechte Geraden
                if self.ya == _y2a: #identische Geraden
                    crosscheck = -1
                    xs = ys = 0
                else: #parallele Geraden
                    crosscheck = 0
                    xs = ys = 0
            else: #Allgemeiner Fall
                dx2 = _x2e - _x2a
                dy2 = _y2e - _y2a
                bg1 = self.ya - dy1/dx1*self.xa
                bg2 = _y2a - dy2/dx2*_x2a
                if bg1 == bg2: #identische Geraden
                    xs = ys = 0
                    crosscheck = -1
                else: #parallele Geraden
                    xs = ys = 0
                    crosscheck = 0
        return(crosscheck, xs, ys)

