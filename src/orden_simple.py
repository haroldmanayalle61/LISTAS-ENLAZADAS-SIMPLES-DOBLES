from typing import TYPE_CHECKING
from estudiante import Estudiante
from nodo import Nodo

if TYPE_CHECKING:
    from lista_simple import ListaSimple


def ordenar(lista: 'ListaSimple', criterio: str, descendente: bool = False) -> None:
    # Ordena la lista enlazada intercambiando los datos de los nodos (no los nodos en si).
    if lista.esta_vacia() or lista.inicio is lista.fin:
        return  # lista vacia o con un solo elemento, no hay nada que ordenar
    actual = lista.inicio
    while actual is not None:
        nodo_min_max = actual
        siguiente_nodo = actual.siguiente
        while siguiente_nodo is not None:
            cambiar = False
            # Evaluacion segun el criterio pedido
            if criterio == 'codigo':
                if not descendente and siguiente_nodo.dato.codigo < nodo_min_max.dato.codigo:
                    cambiar = True
                elif descendente and siguiente_nodo.dato.codigo > nodo_min_max.dato.codigo:
                    cambiar = True
            elif criterio == 'apellidos':
                # apellidos siempre ascendente, asi lo acordo el equipo
                if siguiente_nodo.dato.apellidos.lower() < nodo_min_max.dato.apellidos.lower():
                    cambiar = True
            elif criterio == 'promedio':
                if not descendente and siguiente_nodo.dato.promedio < nodo_min_max.dato.promedio:
                    cambiar = True
                elif descendente and siguiente_nodo.dato.promedio > nodo_min_max.dato.promedio:
                    cambiar = True
            else:
                raise ValueError("Criterio invalido, debe ser codigo, apellidos o promedio.")
            if cambiar:
                nodo_min_max = siguiente_nodo
            siguiente_nodo = siguiente_nodo.siguiente
        if nodo_min_max is not actual: #Intercambio de datos entre nodos
            temp_dato = actual.dato
            actual.dato = nodo_min_max.dato
            nodo_min_max.dato = temp_dato
        actual = actual.siguiente


def _verificar_orden_ascendente(lista: 'ListaSimple') -> bool:
    # Revisa si la lista ya esta ordenada por codigo ascendente
    if lista.esta_vacia() or lista.inicio is lista.fin:
        return True
    actual = lista.inicio
    while actual.siguiente is not None:
        if actual.dato.codigo > actual.siguiente.dato.codigo:
            return False
        actual = actual.siguiente
    return True


def insertar_ordenado(lista: 'ListaSimple', estudiante: Estudiante) -> None:
    # Inserta un estudiante manteniendo el orden ascendente por codigo
    if not _verificar_orden_ascendente(lista):
        raise ValueError("La lista no esta ordenada por codigo ascendente. Ordene la lista primero.")
    nuevo_nodo = Nodo(estudiante)
    if lista.esta_vacia():
        lista.inicio = nuevo_nodo
        lista.fin = nuevo_nodo
        return
    if estudiante.codigo == lista.inicio.dato.codigo:
        raise ValueError(f"Ya existe un estudiante con el codigo '{estudiante.codigo}'.")
    if estudiante.codigo < lista.inicio.dato.codigo:
        nuevo_nodo.siguiente = lista.inicio
        lista.inicio = nuevo_nodo
        return
    actual = lista.inicio
    while actual.siguiente is not None and actual.siguiente.dato.codigo < estudiante.codigo:
        actual = actual.siguiente
    if actual.siguiente is not None and actual.siguiente.dato.codigo == estudiante.codigo:
        raise ValueError(f"Ya existe un estudiante con el codigo '{estudiante.codigo}'.")
    nuevo_nodo.siguiente = actual.siguiente
    actual.siguiente = nuevo_nodo
    if nuevo_nodo.siguiente is None:
        lista.fin = nuevo_nodo
