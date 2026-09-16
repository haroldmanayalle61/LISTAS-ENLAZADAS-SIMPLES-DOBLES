import os

from estudiante import Estudiante
from lista_doble import Lista_doble
from lista_simple import ListaSimple

import orden_doble
import orden_simple


# Creamos las listas una sola vez.
lista_simple = ListaSimple()
lista_doble = Lista_doble()


def leer_entero(mensaje: str) -> int:
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Debe ingresar un número entero.") from None


def leer_flotante(mensaje: str) -> float:
    try:
        return float(input(mensaje))
    except ValueError:
        raise ValueError("Debe ingresar un número válido.") from None


def leer_posicion() -> int:
    posicion = leer_entero("Ingrese la posición (desde 0): ")
    if posicion < 0:
        raise IndexError("La posición no puede ser negativa.")
    return posicion


def limpiar_pantalla() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def registar_estudiante(lista, codigo_actual=None) -> Estudiante:
    if codigo_actual is None:
        # Registro de un estudiante nuevo.
        while True:
            codigo = input("Ingrese código: ").strip()

            if not codigo:
                print("El código no puede estar vacío.")
                continue

            if lista.codigo_existe(codigo):
                print("Código previamente registrado.")
                continue
            break
    else:
        # Modificación: se conserva el identificador.
        codigo = codigo_actual
        print(f"Código del estudiante: {codigo} (no modificable)")

    apellidos = input("Ingrese sus apellidos: ").strip()
    nombres = input("Ingrese sus nombres: ").strip()
    carrera = input("Ingrese su carrera: ").strip()
    ciclo = leer_entero("Ingrese su ciclo: ")
    promedio = leer_flotante("Ingrese su promedio: ")

    return Estudiante(codigo,apellidos,nombres,carrera,ciclo,promedio)

def elegir_descendente() -> bool:
    print("1. Ascendente (menor a mayor)")
    print("2. Descendente (mayor a menor)")

    opcion = leer_entero("Seleccione el orden: ")

    if opcion == 1:
        return False

    if opcion == 2:
        return True

    raise ValueError("Debe seleccionar 1 o 2.")

def menu_principal() -> None:
    limpiar_pantalla()

    while True:
        try:
            print(f"\n{'=' * 10} MENÚ PRINCIPAL {'=' * 10}")
            print("SISTEMA DE GESTIÓN DE ESTUDIANTES")
            print("1. Trabajar con Lista Simple")
            print("2. Trabajar con Lista Doble")
            print("3. Salir")

            numero = leer_entero("Ingrese una opción: ")

            match numero:
                case 1:
                    limpiar_pantalla()
                    menu_lista_simple()
                    limpiar_pantalla()

                case 2:
                    limpiar_pantalla()
                    menu_lista_doble()
                    limpiar_pantalla()

                case 3:
                    print("Programa finalizado.")
                    break

                case _:
                    print("Opción fuera de rango.")

        except EOFError:
            # Permite terminar si se cierra la entrada de la consola.
            raise

        except Exception as e:
            print(f"Error ({type(e).__name__}): {e}")


def menu_lista_simple() -> None:
    while True:
        try:
            print(f"\n{'=' * 10} MENÚ LISTA SIMPLE {'=' * 10}")
            print("1. Insertar estudiante al inicio")
            print("2. Insertar estudiante al final")
            print("3. Insertar estudiante por posición")
            print("4. Insertar estudiante ordenado por código")
            print("5. Buscar estudiante por código")
            print("6. Modificar estudiante por código")
            print("7. Eliminar el primer estudiante de la lista")
            print("8. Eliminar el último estudiante de la lista")
            print("9. Eliminar estudiante por código")
            print("10. Eliminar estudiante por posición")
            print("11. Listar todos los estudiantes")
            print("12. Número de estudiantes registrados")
            print("13. Obtener estudiante por posición")
            print("14. Ordenar estudiantes por código")
            print("15. Ordenar estudiantes por apellidos")
            print("16. Ordenar estudiantes por promedio")
            print("17. Vaciar lista")
            print("18. Insertar despues de un estudiante por codigo")
            print("0. Volver al menú principal")

            numero = leer_entero("Ingrese una opción: ")

            match numero:
                case 1:
                    estudiante = registar_estudiante(lista_simple)
                    lista_simple.insertar_inicio(estudiante)
                    print("Realizado con éxito.")

                case 2:
                    estudiante = registar_estudiante(lista_simple)
                    lista_simple.insertar_final(estudiante)
                    print("Realizado con éxito.")

                case 3:
                    posicion = leer_posicion()
                    # Se permite insertar al final: posición = total.
                    if posicion > lista_simple.contar():
                        raise IndexError("La posición está fuera del rango permitido para insertar.")

                    estudiante = registar_estudiante(lista_simple)
                    lista_simple.insertar_posicion(
                        estudiante, posicion
                    )
                    print("Realizado con éxito.")

                case 4:
                    estudiante = registar_estudiante(lista_simple)
                    orden_simple.insertar_ordenado(lista_simple, estudiante)
                    print("Realizado con éxito.")

                case 5:
                    codigo = input("Ingrese el código del estudiante: ").strip()
                    estudiante = lista_simple.buscar_codigo(codigo)
                    posicion = lista_simple.obtener_posicion(codigo)
                    print("ESTUDIANTE ENCONTRADO :")
                    print(estudiante)
                    print("Posicion :",posicion)

                case 6:
                    codigo = input("Ingrese el código del estudiante a modificar: ").strip()
                    # Si no existe, el método lanza ValueError.
                    estudiante = lista_simple.buscar_codigo(codigo)
                    print("Estudiante actual:")
                    print(estudiante)
                    nuevo_estudiante = registar_estudiante(lista_simple,codigo)
                    lista_simple.modificar(codigo, nuevo_estudiante)
                    print("Realizado con éxito.")

                case 7:
                    lista_simple.eliminar_primero()
                    print("Eliminado con éxito.")

                case 8:
                    lista_simple.eliminar_ultimo()
                    print("Eliminado con éxito.")

                case 9:
                    codigo = input("Ingrese el código: ").strip()
                    lista_simple.eliminar_codigo(codigo)
                    print("Eliminado con éxito.")

                case 10:
                    posicion = leer_posicion()
                    lista_simple.eliminar_posicion(posicion)
                    print("Eliminado con éxito.")

                case 11:
                    if lista_simple.contar() > 0 :
                        print(f"\n{'=' * 10} ESTUDIANTES REGISTRADOS {'=' * 10}")
                        print(lista_simple)
                    else :
                        print("La lista está vacía")

                case 12:
                    print("Total de estudiantes registrados:",lista_simple.contar())

                case 13:
                    if lista_simple.contar()>0:
                        posicion = leer_posicion()
                        estudiante = lista_simple.obtener_por_posicion(posicion)
                        if estudiante is None:
                            raise IndexError("La posición está fuera del rango de la lista.")
                        print(estudiante)
                    else :
                        print("La lista está vacía")

                case 14:
                    if lista_simple.contar()>0 :
                        descendente = elegir_descendente()
                        print("\nLISTA ANTES DEL ORDENAMIENTO:")
                        print(lista_simple)
                        orden_simple.ordenar(lista_simple,"codigo",descendente)
                        print("\nLISTA DESPUES DEL ORDENAMIENTO:")
                        print(lista_simple)
                    else:
                        print("La lista está vacía")
                case 15:
                    if lista_simple.contar()> 0 :
                        print("\nLISTA ANTES DEL ORDENAMIENTO:")
                        print(lista_simple)
                        orden_simple.ordenar(lista_simple,"apellidos")
                        print("\nLISTA DESPUES DEL ORDENAMIENTO:")
                        print(lista_simple)
                    else:
                        print("La lista está vacía")

                case 16:
                    if lista_simple.contar() > 0:
                        descendente = elegir_descendente()
                        print("\nLISTA ANTES DEL ORDENAMIENTO:")
                        print(lista_simple)
                        orden_simple.ordenar(lista_simple,"promedio",descendente)
                        print("\nLISTA DESPUÉS DEL ORDENAMIENTO:")
                        print(lista_simple)
                    else:
                        print("La lista está vacía")

                case 17:
                    if lista_simple.contar() > 0 :
                        lista_simple.vaciar()
                        print("Lista vaciada con éxito.")
                    else :
                        print("No se ha registrado ningun estudiante")

                case 18:
                    codigo = input("Código del estudiante de referencia: ").strip()
                    referencia = lista_simple.buscar_codigo(codigo)
                    print("\nESTUDIANTE DE REFERENCIA:")
                    print(referencia)
                    print("\nIngrese los datos del nuevo estudiante:")
                    estudiante = registar_estudiante(lista_simple)
                    print("\nLISTA ANTES DE INSERTAR:")
                    print(lista_simple)
                    lista_simple.insertar_despues(codigo,estudiante)

                    print("\nLISTA DESPUÉS DE INSERTAR:")
                    print(lista_simple)
                case 0:
                    break

                case _:
                    print("Opción fuera de rango.")

        except EOFError:
            raise

        except Exception as e:
            print(f"Error ({type(e).__name__}): {e}")


def menu_lista_doble() -> None:
    while True:
        try:
            print(f"\n{'=' * 10} MENÚ LISTA DOBLE {'=' * 10}")
            print("1. Insertar estudiante al inicio")
            print("2. Insertar estudiante al final")
            print("3. Insertar estudiante por posición")
            print("4. Insertar estudiante ordenado por código")
            print("5. Buscar estudiante por código")
            print("6. Modificar estudiante por código")
            print("7. Eliminar el primer estudiante de la lista")
            print("8. Eliminar el último estudiante de la lista")
            print("9. Eliminar estudiante por código")
            print("10. Eliminar estudiante por posición")
            print("11. Listar todos los estudiantes")
            print("12. Número de estudiantes registrados")
            print("13. Obtener estudiante por posición")
            print("14. Ordenar estudiantes por código")
            print("15. Ordenar estudiantes por apellidos")
            print("16. Ordenar estudiantes por promedio")
            print("17. Vaciar lista")
            print("18. Insertar después de un estudiante por código")
            print("19. Insertar antes de un estudiante por código")
            print("20. Recorrer la lista de fin a inicio")
            print("0. Volver al menú principal")

            numero = leer_entero("Ingrese una opción: ")

            match numero:
                case 1:
                    estudiante = registar_estudiante(lista_doble)
                    lista_doble.insertar_inicio(estudiante)
                    print("Realizado con éxito.")

                case 2:
                    estudiante = registar_estudiante(lista_doble)
                    lista_doble.insertar_final(estudiante)
                    print("Realizado con éxito.")

                case 3:
                    posicion = leer_posicion()
                    if posicion > lista_doble.contar_elementos():
                        raise IndexError("La posición está fuera del rango permitido para insertar.")
                    estudiante = registar_estudiante(lista_doble)
                    lista_doble.insertar_posicion(estudiante, posicion)
                    print("Realizado con éxito.")

                case 4:
                    estudiante = registar_estudiante(lista_doble)
                    orden_doble.insertar_ordenado(lista_doble, estudiante)
                    print("Realizado con éxito.")

                case 5:
                    if lista_doble.contar_elementos() > 0 :
                        codigo = input("Ingrese el código del estudiante: ").strip()
                        estudiante = lista_doble.buscar_por_codigo(codigo)
                        if estudiante is None:
                            raise ValueError(f"No se encontró un estudiante con el código {codigo}.")
                        print(estudiante)
                    else :
                        print("La lista está vacía")

                case 6:
                    if lista_doble.contar_elementos() > 0:
                        codigo = input("Ingrese el código del estudiante a modificar: ").strip()
                        estudiante = lista_doble.buscar_por_codigo(codigo)
                        if estudiante is None:
                            raise ValueError(f"No se encontró un estudiante con el código {codigo}.")
                        print("Estudiante actual:")
                        print(estudiante)
                        nuevo_estudiante = registar_estudiante(lista_doble,codigo)

                        if not lista_doble.modificar_estudiante(
                            codigo, nuevo_estudiante
                        ):
                            raise ValueError("No se pudo modificar el estudiante.")
                        print("Realizado con éxito.")
                    else :
                        print("La lista está vacía")

                case 7:
                    if not lista_doble.eliminar_primero():
                        raise ValueError("La lista está vacía, No se puede eliminar ningún estudiante.")
                    print("Eliminado con éxito.")

                case 8:
                    if not lista_doble.eliminar_ultimo():
                        raise ValueError("La lista está vacía, No se puede eliminar ningún estudiante.")
                    print("Eliminado con éxito.")

                case 9:
                    if lista_doble.contar_elementos() > 0:
                        codigo = input("Ingrese el código: ").strip()
                        if not lista_doble.eliminar_por_codigo(codigo):
                            raise ValueError(f"No se encontró un estudiante con el código {codigo}.")
                        print("Eliminado con éxito.")
                    else :
                        print("La lista está vacía")

                case 10:
                    if lista_doble.contar_elementos()>0:
                        posicion = leer_posicion()
                        if not lista_doble.eliminar_por_posicion(posicion):
                            raise IndexError("La posición está fuera del rango de la lista.")
                        print("Eliminado con éxito.")
                    else:
                        print("La lista está vacía")

                case 11:
                    print(f"\n{'=' * 10} ESTUDIANTES REGISTRADOS {'=' * 10}")
                    lista_doble.mostrar_inicio_a_fin()

                case 12:
                    print("Total de estudiantes registrados:",lista_doble.contar_elementos())

                case 13:
                    if lista_doble.contar_elementos()>0:
                        posicion = leer_posicion()
                        estudiante = lista_doble.obtener_por_posicion(posicion)
                        if estudiante is None:
                            raise IndexError("La posición está fuera del rango de la lista.")
                        print(estudiante)
                    else:
                        print("La lista está vacía")

                case 14:
                    if lista_doble.contar_elementos()>0:
                        descendente = elegir_descendente()
                        print("\nLISTA ANTES DEL ORDENAMIENTO:")
                        lista_doble.mostrar_inicio_a_fin()
                        orden_doble.ordenar(lista_doble,"codigo",descendente)
                        print("\nLISTA DESPUES DEL ORDENAMIENTO:")
                        lista_doble.mostrar_inicio_a_fin()
                    else:
                        print("La lista está vacía")

                case 15:
                    if lista_doble.contar_elementos()>0:
                        print("\nLISTA ANTES DEL ORDENAMIENTO:")
                        lista_doble.mostrar_inicio_a_fin()
                        orden_doble.ordenar(lista_doble,"apellidos")
                        print("\nLISTA DESPUES DEL ORDENAMIENTO:")
                        lista_doble.mostrar_inicio_a_fin()
                    else:
                        print("La lista está vacía")

                case 16:
                    if lista_doble.contar_elementos()>0:
                        descendente = elegir_descendente()
                        print("\nLISTA ANTES DEL ORDENAMIENTO:")
                        lista_doble.mostrar_inicio_a_fin()
                        orden_doble.ordenar(lista_doble,"promedio",descendente)
                        print("\nLISTA DESPUÉS DEL ORDENAMIENTO:")
                        lista_doble.mostrar_inicio_a_fin()
                    else :
                        print("La lista está vacía")

                case 17:
                    if lista_doble.contar_elementos()>0:
                        lista_doble.vaciar_lista()
                        print("Lista vaciada con éxito.")
                    else:
                        print("La lista ya estaba vacía")

                case 18:
                    if lista_doble.contar_elementos()>0:
                        codigo = input("Código del estudiante de referencia: ").strip()
                        referencia = lista_doble.buscar_por_codigo(codigo)

                        if referencia is None:
                            raise ValueError(f"No se encontró un estudiante con el código {codigo}.")

                        print("Ingrese los datos del nuevo estudiante:")
                        estudiante = registar_estudiante(lista_doble)

                        if not lista_doble.insertar_despues(codigo, estudiante):
                            raise ValueError("No se pudo insertar el estudiante.")
                        print("Realizado con éxito.")
                    else :
                        print("La lista esta vacia")

                case 19:
                    if lista_doble.contar_elementos()>0:
                        codigo = input("Código del estudiante de referencia: ").strip()
                        referencia = lista_doble.buscar_por_codigo(codigo)

                        if referencia is None:
                            raise ValueError(f"No se encontró un estudiante con el código {codigo}.")
                        print("Ingrese los datos del nuevo estudiante:")
                        estudiante = registar_estudiante(lista_doble)

                        if not lista_doble.insertar_antes(codigo, estudiante):
                            raise ValueError("No se pudo insertar el estudiante.")
                        print("Realizado con éxito.")
                    else :
                        print("La lista esta vacia")

                case 20:
                    lista_doble.mostrar_fin_a_inicio()

                case 0:
                    break

                case _:
                    print("Opción fuera de rango.")

        except EOFError:
            raise

        except Exception as e:
            print(f"Error ({type(e).__name__}): {e}")

if __name__ == "__main__":
    try:
        menu_principal()

    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")