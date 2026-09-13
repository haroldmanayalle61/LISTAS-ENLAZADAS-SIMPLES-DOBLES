from nodo import Nodo
from estudiante import Estudiante

class ListaSimple:

    def __init__(self):
        self.inicio = None
        self.fin = None

    def esta_vacia(self)-> bool:
        return self.inicio is None

    def inserter_inicio(self, estudiante: Estudiante)-> None:
        nuevo_nodo = Nodo(estudiante)

        if self.esta_vacia():
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo

        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo

    def insertar_final(self, estudiante: Estudiante)-> None:
        nuevo_nodo = Nodo(estudiante)

        if self.esta_vacia():
            self.inicio = nuevo_nodo

            
        else:
            self.fin.siguiente = nuevo_nodo

        self.fin = nuevo_nodo

    def insertar_posicion(self, estudiante: Estudiante, posicion: int) -> None:

        if posicion <0:
            raise IndexError("La posicion no puede ser negatica.")

        nuevo_nodo = Nodo(estudiante)

        #Insertar al inicio
        if posicion == 0:
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo

            if self.fin is None:
                self.fin = nuevo_nodo

            return

        nodo_actual = self.inicio
        contador = 0

        while nodo_actual is not None and contador < posicion -1:
            nodo_actual = nodo_actual.siguiente
            contador += 1

        if nodo_actual is None:
            raise IndexError("La posicion esta fuera del rango de la lista.")

        nuevo_nodo.siguiente = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo

        if nuevo_nodo.siguiente is None:
            self.fin = nuevo_nodo
  