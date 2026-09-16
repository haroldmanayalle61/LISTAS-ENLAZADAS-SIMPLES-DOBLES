from typing import TYPE_CHECKING
from estudiante import Estudiante
from nodo_doble import Nodo_doble

if TYPE_CHECKING:
    from lista_doble import Lista_doble

def ordenar(lista: 'Lista_doble', criterio: str, descendente: bool = False) -> None:
    #Ordena la lista doblemente enlazada intercambiando los datos de los nodos.
    if lista.esta_vacia() or lista.cabeza is lista.cola:
        return 
    actual = lista.cabeza
    while actual is not None:
        nodo_min_max = actual
        siguiente_nodo = actual.siguiente
        while siguiente_nodo is not None:
            cambiar = False
            if criterio == 'codigo':
                if not descendente and siguiente_nodo.dato.codigo < nodo_min_max.dato.codigo:
                    cambiar = True
                elif descendente and siguiente_nodo.dato.codigo > nodo_min_max.dato.codigo:
                    cambiar = True
            elif criterio == 'apellidos':
                if siguiente_nodo.dato.apellidos.lower() < nodo_min_max.dato.apellidos.lower():
                    cambiar = True
            elif criterio == 'promedio':
                if not descendente and siguiente_nodo.dato.promedio < nodo_min_max.dato.promedio:
                    cambiar = True
                elif descendente and siguiente_nodo.dato.promedio > nodo_min_max.dato.promedio:
                    cambiar = True
            if cambiar:
                nodo_min_max = siguiente_nodo   
            siguiente_nodo = siguiente_nodo.siguiente
        if nodo_min_max != actual:
            temp_dato = actual.dato
            actual.dato = nodo_min_max.dato
            nodo_min_max.dato = temp_dato 
        actual = actual.siguiente

def _verificar_orden_ascendente(lista: 'Lista_doble') -> bool:
    #Verifica si la lista esta ordenada por codigo ascendente.
    if lista.esta_vacia() or lista.cabeza is lista.cola:
        return True   
    actual = lista.cabeza
    while actual.siguiente is not None:
        if actual.dato.codigo > actual.siguiente.dato.codigo:
            return False
        actual = actual.siguiente
    return True

def insertar_ordenado(lista: 'Lista_doble', estudiante: Estudiante) -> None:
    #Inserta un estudiante manteniendo el orden ascendente por código modificando referencias.
    if not _verificar_orden_ascendente(lista):
        raise ValueError("La lista no está ordenada por código ascendente. Ordene la lista primero.") 
    nuevo_nodo = Nodo_doble(estudiante)
    
    # Caso 1: Lista vacía 
    if lista.esta_vacia():
        lista.cabeza = nuevo_nodo
        lista.cola = nuevo_nodo
        lista.tamanio += 1
        return
        
    # Caso 2: Insertar al inicio
    if estudiante.codigo < lista.cabeza.dato.codigo:
        nuevo_nodo.siguiente = lista.cabeza
        lista.cabeza.anterior = nuevo_nodo
        lista.cabeza = nuevo_nodo
        lista.tamanio += 1
        return
    if estudiante.codigo > lista.cola.dato.codigo:
        nuevo_nodo.anterior = lista.cola
        lista.cola.siguiente = nuevo_nodo
        lista.cola = nuevo_nodo
        lista.tamanio += 1
        return

    actual = lista.cabeza
    while actual.siguiente is not None and actual.siguiente.dato.codigo < estudiante.codigo:
        actual = actual.siguiente  
    # Si llegamos al final (Insertar al final)
    if actual.siguiente is None:
        nuevo_nodo.anterior = actual
        actual.siguiente = nuevo_nodo
        lista.cola = nuevo_nodo
    else:
        siguiente_nodo = actual.siguiente
        nuevo_nodo.anterior = actual
        nuevo_nodo.siguiente = siguiente_nodo
        actual.siguiente = nuevo_nodo
        siguiente_nodo.anterior = nuevo_nodo
    lista.tamanio += 1
