from nodo import Nodo
from estudiante import Estudiante

class ListaSimple:

    def __init__(self) -> None:
        self.inicio = None
        self.fin = None

    def esta_vacia(self)-> bool:
        return self.inicio is None

    def insertar_inicio(self, estudiante: Estudiante)-> None:
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

    def insertar_despues(self, codigo: str, estudiante: Estudiante) -> None:
        nodo_actual = self.inicio

        while nodo_actual is not None:

            if nodo_actual.dato.codigo == codigo:
                nuevo_nodo = Nodo(estudiante)

                nuevo_nodo.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo

                if nuevo_nodo.siguiente is None:
                    self.fin = nuevo_nodo

                return

            nodo_actual = nodo_actual.siguiente

        raise ValueError(f"No se encontró un estudiante con el código {codigo}")

    def buscar_codigo(self, codigo: str) -> Estudiante | None:
        nodo_actual = self.inicio

        while nodo_actual is not None:
            if nodo_actual.dato.codigo == codigo:
                return nodo_actual.dato
            nodo_actual = nodo_actual.siguiente

        raise ValueError(f"No se encontró un estudiante con el código {codigo}")

    def modificar (self, codigo: str, nuevo_estudiante: Estudiante) -> None:
        nodo_actual = self.inicio

        while nodo_actual is not None:
            if nodo_actual.dato.codigo == codigo:
                nodo_actual.dato = nuevo_estudiante
                return

            nodo_actual = nodo_actual.siguiente

        raise ValueError(f"No se encontró un estudiante con el código {codigo}")

    def eliminar_primero(self) -> None:

        if self.esta_vacia():
            raise ValueError("La lista está vacía. No se puede eliminar ningún estudiante.")

        nodo_eliminado = self.inicio
        self.inicio = self.inicio.siguiente
        nodo_eliminado.siguiente = None

        if self.inicio is None:
            self.fin = None

    def eliminar_ultimo(self) -> None:

        if self.esta_vacia():
            raise ValueError("La lista está vacía. No se puede eliminar ningún estudiante.")

        #Caso: Solo existe un nodo en la lista
        if self.inicio == self.fin:
            self.inicio = None
            self.fin = None
            return

        nodo_actual = self.inicio

        #Buscar el nodo anterior al último
        while nodo_actual.siguiente != self.fin:
            nodo_actual = nodo_actual.siguiente

        nodo_eliminado = self.fin

        self.fin = nodo_actual
        self.fin.siguiente = None
        nodo_eliminado.siguiente = None

    def eliminar_codigo(self, codigo: str) -> None:
        if self.esta_vacia():
            raise ValueError("La lista está vacía. No se puede eliminar ningún estudiante.")

        #Caso: Eliminar el primer nodo
        if self.inicio.dato.codigo == codigo:
            self.eliminar_primero()
            return

        nodo_anterior = self.inicio
        nodo_actual = self.inicio.siguiente

        while nodo_actual is not None:

            if nodo_actual.dato.codigo == codigo:

                nodo_anterior.siguiente = nodo_actual.siguiente

                #Si eliminamos el ultimo nodo
                if nodo_actual == self.fin:
                    self.fin = nodo_anterior

                nodo_actual.siguiente = None
                return

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        raise ValueError(f"No se encontró un estudiante con el código {codigo}")

    def eliminar_posicion(self, posicion: int) -> None:
        if self.esta_vacia():
            raise ValueError("La lista está vacía. No se puede eliminar ningún estudiante.")

        if posicion < 0:
            raise IndexError("La posición no puede ser negativa.")

        #Caso: Eliminar el primer nodo
        if posicion == 0:
            self.eliminar_primero()
            return

        nodo_anterior = self.inicio
        nodo_actual = self.inicio.siguiente

        contador = 1

        while nodo_actual is not None:
            if contador == posicion:
                nodo_anterior.siguiente = nodo_actual.siguiente

                if nodo_actual == self.fin:
                    self.fin = nodo_anterior

                nodo_actual.siguiente = None
                return

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            contador += 1

        raise IndexError("La posición está fuera del rango de la lista.")

    def mostrar(self) -> None:
        print(self)

    def contar(self) -> int:
        contador = 0
        nodo_actual = self.inicio

        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente

        return contador

    def obtener_posicion(self, codigo: str) -> int:
        nodo_actual = self.inicio
        posicion = 0

        while nodo_actual is not None:

            if nodo_actual.dato.codigo == codigo:
                return posicion
            
            nodo_actual = nodo_actual.siguiente
            posicion += 1

        raise ValueError(f"No se encontró un estudiante con el código {codigo}")

    def vaciar(self) -> None:
        self.inicio = None
        self.fin = None

    def __str__(self) -> str:
        if self.esta_vacia():
            return "La lista está vacía."

        mensaje = ""
        nodo_actual = self.inicio

        while nodo_actual is not None:
            mensaje += str(nodo_actual.dato)

            if nodo_actual.siguiente is not None:
                mensaje += "\n"

            nodo_actual = nodo_actual.siguiente

        return mensaje

    def codigo_existe(self,codigo:str)-> bool:
        nodo_actual = self.inicio
        while nodo_actual is not None:
            if nodo_actual.dato.codigo == codigo :
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def obtener_por_posicion(self, posicion: int) -> Estudiante:
        if posicion < 0:
            raise IndexError("La posición no puede ser negativa.")

        actual = self.inicio
        contador = 0

        while actual is not None:
            if contador == posicion:
                return actual.dato

            actual = actual.siguiente
            contador += 1

        raise IndexError("La posición está fuera del rango de la lista.")