
from __future__ import generators
import random


class Flor(object):
    def aceptar(self, visitar):
        visitar.visita(self)
    def polinizar(self, polinizador):
        print(self, "pollinated by", polinizador)
    def come(self, comedor):
        print(self, "eaten by", comedor)
    def __str__(self):
        return self.__class__.__name__

class Gladiolas(Flor): pass
class Runuculus(Flor): pass
class Crisantemo(Flor): pass

class Visitar(Flor):
    def __str__(self):
        return self.__class__.__name__


class Polinizador(Visitar): pass
class Depredador(Visitar): pass


class Abeja(Polinizador):
    def visita(self, flor):
        flor.polinizar(self)


class Volar(Abeja):
    def visita(self, flor):
        flor.polinizar(self)


class Gusano(Depredador):
    def visita(self, flor):
        flor.come(self)


abeja = abeja()
volar = volar()
gusano = gusano()

