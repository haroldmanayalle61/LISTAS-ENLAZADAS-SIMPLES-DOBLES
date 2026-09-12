from estudiante import Estudiante

class Nodo:

#Unidad de almacenamiento para una lista simple

    def __init__(self,dato:Estudiante)->None:
        self.dato = dato
        self.siguiente = None

    def __str__(self)->str:
        return str(self.dato)
