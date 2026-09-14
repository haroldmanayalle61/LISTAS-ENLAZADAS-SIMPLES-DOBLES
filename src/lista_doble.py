from estudiante import Estudiante
from nodo_doble import Nodo_doble


class Lista_doble:

    # Lista doblemente enlazada de estudiantes (usa enlaces anterior y siguiente)

    def __init__(self) -> None:
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def __str__(self) -> str:
        return f"Lista_doble con {self.tamanio} elemento(s)"

    # ------------------------------------------------------------------
    # Verificacion / consulta
    # ------------------------------------------------------------------
    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def contar_elementos(self) -> int:
        return self.tamanio

    def buscar_por_codigo(self, codigo: str) -> Estudiante | None:
        nodo = self._buscar_nodo(codigo)
        return nodo.dato if nodo is not None else None

    def obtener_por_posicion(self, posicion: int) -> Estudiante | None:
        nodo = self._nodo_en_posicion(posicion)
        return nodo.dato if nodo is not None else None

    # ------------------------------------------------------------------
    # Inserciones
    # ------------------------------------------------------------------
    def insertar_inicio(self, dato: Estudiante) -> None:
        nuevo = Nodo_doble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def insertar_final(self, dato: Estudiante) -> None:
        nuevo = Nodo_doble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1

    def insertar_posicion(self, dato: Estudiante, posicion: int) -> None:
        # posicion 0 = primer elemento
        if posicion <= 0:
            self.insertar_inicio(dato)
            return
        if posicion >= self.tamanio:
            self.insertar_final(dato)
            return

        actual = self._nodo_en_posicion(posicion)
        anterior = actual.anterior
        nuevo = Nodo_doble(dato)

        nuevo.anterior = anterior
        nuevo.siguiente = actual
        anterior.siguiente = nuevo
        actual.anterior = nuevo
        self.tamanio += 1

    def insertar_antes(self, codigo: str, dato: Estudiante) -> bool:
        actual = self._buscar_nodo(codigo)
        if actual is None:
            return False
        if actual.anterior is None:
            self.insertar_inicio(dato)
            return True

        anterior = actual.anterior
        nuevo = Nodo_doble(dato)

        nuevo.anterior = anterior
        nuevo.siguiente = actual
        anterior.siguiente = nuevo
        actual.anterior = nuevo
        self.tamanio += 1
        return True

    def insertar_despues(self, codigo: str, dato: Estudiante) -> bool:
        actual = self._buscar_nodo(codigo)
        if actual is None:
            return False
        if actual.siguiente is None:
            self.insertar_final(dato)
            return True

        siguiente = actual.siguiente
        nuevo = Nodo_doble(dato)

        nuevo.anterior = actual
        nuevo.siguiente = siguiente
        actual.siguiente = nuevo
        siguiente.anterior = nuevo
        self.tamanio += 1
        return True

    # ------------------------------------------------------------------
    # Modificacion
    # ------------------------------------------------------------------
    def modificar_estudiante(self, codigo: str, nuevo_dato: Estudiante) -> bool:
        nodo = self._buscar_nodo(codigo)
        if nodo is None:
            return False
        nodo.dato = nuevo_dato
        return True

    # ------------------------------------------------------------------
    # Eliminaciones
    # ------------------------------------------------------------------
    def eliminar_primero(self) -> bool:
        if self.esta_vacia():
            return False
        if self.cabeza is self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self.tamanio -= 1
        return True

    def eliminar_ultimo(self) -> bool:
        if self.esta_vacia():
            return False
        if self.cabeza is self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self.tamanio -= 1
        return True

    def eliminar_por_codigo(self, codigo: str) -> bool:
        nodo = self._buscar_nodo(codigo)
        if nodo is None:
            return False
        self._desenlazar(nodo)
        return True

    def eliminar_por_posicion(self, posicion: int) -> bool:
        nodo = self._nodo_en_posicion(posicion)
        if nodo is None:
            return False
        self._desenlazar(nodo)
        return True

    def vaciar_lista(self) -> None:
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    # ------------------------------------------------------------------
    # Recorridos (bidireccionales)
    # ------------------------------------------------------------------
    def mostrar_inicio_a_fin(self) -> None:
        if self.esta_vacia():
            print("La lista esta vacía.")
            return
        actual = self.cabeza
        while actual is not None:
            print(actual)
            actual = actual.siguiente

    def mostrar_fin_a_inicio(self) -> None:
        if self.esta_vacia():
            print("La lista esta vacía.")
            return
        actual = self.cola
        while actual is not None:
            print(actual)
            actual = actual.anterior

    # ------------------------------------------------------------------
    # Metodos internos de apoyo
    # ------------------------------------------------------------------
    def _buscar_nodo(self, codigo: str) -> Nodo_doble | None:
        actual = self.cabeza
        while actual is not None:
            if actual.dato.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def _nodo_en_posicion(self, posicion: int) -> Nodo_doble | None:
        if posicion < 0 or posicion >= self.tamanio:
            return None
        if posicion <= self.tamanio // 2:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.tamanio - 1 - posicion):
                actual = actual.anterior
        return actual

    def _desenlazar(self, nodo: Nodo_doble) -> None:
        if nodo.anterior is not None:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente

        if nodo.siguiente is not None:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.cola = nodo.anterior

        nodo.anterior = None
        nodo.siguiente = None
        self.tamanio -= 1
