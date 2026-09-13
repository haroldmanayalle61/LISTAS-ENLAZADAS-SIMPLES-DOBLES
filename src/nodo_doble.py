from estudiante import Estudiante
class Nodo_doble:

#Unidad de almacenamiento para listas doblemente enlazadas
    def __init__(self,dato:Estudiante)->None:
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def __str__(self)->str:
        return str(self.dato)