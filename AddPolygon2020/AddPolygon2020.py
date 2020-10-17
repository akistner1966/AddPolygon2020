# -*- coding: utf-8 -*-
#@author: comet

import math

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
        
    def lne_x_chk(self, _x2a, _y2a, _x2e, _y2e):
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
        für den Schnittpunkt ist es unwichtig, ob sich dieser innerhalb
        der Grenzen der Geraden (_x2a, _y2a, _x2e, _y2e) und
        (self.xa, self.ya, self.xe, self.ye) befindet oder nicht.
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
            if (dxs == 0) and (dys == 0): #Schnittpunkt = Endpunkt
                lbda = 0
            elif (dxs == 0) and (dys != 0): #Senkrechte Gerade
                lbda = dys/dy1
            elif (dxs != 0) and (dys == 0): #Waagerechte Gerade
                lbda = dxs/dx1
            else: #Allgemeinster Fall
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

class poly(object):
    def __init__(self, xlist, ylist):
        """
        Übergabeparameter:
        <xlist>: x-Koordinaten der Ecken
        <ylist>: y-Koordinaten der Ecken
        Rückgabewert:
        False: Definition des Polygons was nicht erfolgreich
        True: Definition des Polygons was erfolgreich
        """
        if len(xlist) != len(ylist):
            self.OK = False
        else:
            self.xl = xlist
            self.yl = ylist
            self.xl.append(self.xl[0]) #Polygon schließen (x-Koordinate)
            self.yl.append(self.yl[0]) #Polygon schließen (y-Koordinate)
            self.OK = True

    def klaenge(self):
        """
        berechnet die Kantenlänge des Polygons
        """
        umfang = 0
        for cnt, ele in enumerate(self.xl, 0):
            if cnt > 0:
                umfang += math.sqrt((self.xl[cnt] - self.xl[cnt - 1])**2 + \
                    (self.yl[cnt] - self.yl[cnt - 1])**2)
        return(umfang)


    def xcheck(self):
        """
        Prüfung, ob sich zwei oder mehrere Teilstrecken des Polygons
        kreuzen. Rückgabewert ist die Anzahl der Kreuzungspunkte.
        """
        for cnt1, ele1 in enumerate(self.xl, 0):
            for cnt2, ele2 in enumerate(self.xl, 0):
                if cnt1 != cnt2:
                    pass

    def flaeche(self):
        """
        berechnet den Flächeninhalt des Polygons
        """
        ymin = self.yl[0]
        for ele in self.yl:
            ymin = min(ymin, ele)
        flaeche = 0
        for cnt, ele in enumerate(self.xl, 0):
            if cnt > 0:
                delta = (self.xl[cnt] - self.xl[cnt - 1])*\
                    ((self.yl[cnt] + self.yl[cnt - 1])/2 - ymin)
                if self.xl[cnt - 1] > self.xl[cnt]: #positiver Flächenzuwachs
                    flaeche += delta
                else: #negativer Flächenzuwachs
                    flaeche -= delta
        return(abs(flaeche))


    def inside(self, px, py):
        """
        """
        pass

def polytest(xli, yli):
    if len(xli) == len(yli):
        p = poly(xli, yli)
        ausstr = 'Polygon: '
        for cnt, ele in enumerate(xlst, 0):
            ausstr += '(' + str(xli[cnt]) + ',' + str(yli[cnt]) + ')'
        print(ausstr)
        print('Kantenlänge gesamt: ' + str(p.klaenge()))
        print('Fläche: ' +str(p.flaeche()))
    else:
        print('fehlerhaftes Polygon!')


def linetest(x11, y11, x12, y12, x21, y21, x22, y22):
    lgrund = linie(x11, y11, x12, y12)
    (xc_ger, xs_ger, ys_ger) = lgrund.lne_x_chk(x21, y21, x22, y22)
    ausstr = 'Linien: '
    ausstr += '(' + str(x11) + ',' + str(y11) + ')-('
    ausstr += str(x12) + ',' + str(y12) + ') und '
    ausstr += '(' + str(x21) + ',' + str(y21) + ')-('
    ausstr += str(x22) + ',' + str(y22) + ')\n'
    if xc_ger == 1: #ein Kreuzungspunkt
        ausstr += 'Kreuzungspunkt der Geradenstücke: '
        ausstr += str(xs_ger) + ',' + str(ys_ger)
    elif xc_ger == 0: #Parallele Geraden => kein Kreuzungspunkt
        ausstr += 'Kein Kreuzungspunkt. Nicht parallele, nicht'
        ausstr += ' identische Geraden'
    else: #identische Geraden => unendlich viele Kreuzungspunkte
        ausstr += 'Unendliche viele Kreuzungspunkte, identische Geraden'
    print(ausstr + '\n')

linetest(0, 0, 1, 1, 2, 2, 3, 1)
linetest(0, 0, 1, 1, 0, 1, 1, 0)
linetest(0, 0, 1, 0, 0, 1, 0, 0)