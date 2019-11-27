from abc import ABC, abstractmethod

class EsterioCars(ABC):
    @abstractmethod
    def accion(self):
        pass

class CambiarCancion(EsterioCars):
    def __init__(self, EsterioCars):
        self.esterio = EsterioCars

    def accion(self):
        self.esterio.Cambiar()
        

class Apagar(EsterioCars):
    def __init__(self, EsterioCars):
        self.esterio = EsterioCars

    def action(self):
        self.esterio.Apagar()

class Volumen(EsterioCars):
    def __init__(self, EsterioCars):
        self.esterio = EsterioCars

    def accion(self):
        self.esterio.Volumen()

class Menu:
    def Cambiar(self):
        print("Cambiar cancion")
        
    def Apagar(self):
        print("Apagar")
        
    def Volumen(self):
        print(" Volumen")

class Acciones:
    
    def __init__(self):
        self._accion = []

    def requestActions(self, EsterioCars):
        self._accion.append(EsterioCars)
       EsterioCars.accion()

class main():
    menu = Menu()
    esterio_Apagar = Apagar(menu)
    esterio_CambiarCancion = CambiarCancion(menu)
    esterio_Volumen = Volumen(menu)

    act = Acciones()
    act.requestAccion(esterio_Volumen)
    act.requestAccion(esterio_CambiarCancion)
    act.requestAccion(esterio_Volumen)
    act.requestAccion(esterio_Apagar)

        
    
        
        
