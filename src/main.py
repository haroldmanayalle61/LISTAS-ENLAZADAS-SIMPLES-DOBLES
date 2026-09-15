import os
from estudiante import Estudiante
from lista_doble import Lista_doble
from lista_simple import ListaSimple
import orden_doble
import orden_simple
import Exception

def leer_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Error: debe ingresar un numero entero.")
        return None

def leer_flotante(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        print("Error: debe ingresar un numero valido.")
        return None
    
def menu_principal()-> None:
    #Menu principal
    while True:
        print(f'{"="*10}MENU PRINCIPAL{"="*10}')
        print("SISTEMA DE GESTION DE ESTUDIANES")
        print("1. Trabajar con Lista Simple")
        print("2. Trabajar con Lista Doble")
        print("3. Salir")
        numero = leer_entero("Ingrese una opcion")
        match numero :
            case 1 : 
                menu_lista_simple()
                limpiar_pantalla()
            case 2 : 
                menu_lista_doble()
                limpiar_pantalla
            case 3 : break
            case _ :
                print("Opcion fuera de rango")

def menu_lista_simple() -> None :
    while True:
        print(f'{"="*10}MENU LISTA SIMPLE{"="*10}')
        print("1. Insertar Estudiante al inicio")
        print("2. Insertar Estudiante al final")
        print("3. Insertar Estudiante por posicion")
        print("4. Insertar Estudiante y ordenar por código")
        print("5. Buscar estudiante por codigo")
        print("6. Modificar estudiante por código")
        print("7. Eliminar el primer estudiante registrado")
        print("8. Elimnar el ultimo estudiante registrado")
        print("9. Eliminar estudiante por código")
        print("10. Eliminar estudiante por posicion")
        print("11. Listar todos los estudiantes")
        print("12. Numero de estudiantes registrados")
        print("13. Obtener estudiante por posicion")
        print("14. Ordenar estudiantes por código")
        print("15. Ordenar estudiantes por apellidos")
        print("16. Ordenar estudiantes por promedio")
        print("17. Vaciar lista")
        print("0. Salir")
        numero = leer_entero("Ingrese una opcion")
        match numero :
            case 1 : 
                try:
                    estudiante = registar_estudiante()
                    ListaSimple.insertar_inicio(estudiante)
                    print("Realizado con exito")
                except Exception as e :
                    print (f"Error :{e}")

            case 2 :
                try:
                    estudiante = registar_estudiante()
                    ListaSimple.insertar_final(estudiante)
                    print("Realizado con exito")
                except Exception as e:
                    print (f"Error :{e}")

            case 3 :
                posicion = -1
                while posicion<0 :
                    posicion = leer_entero("Ingrese la posicion")
                    if posicion < 0:
                        print ("Ingrese un nuemero positivo")
                try:        
                    estudiante = registar_estudiante()
                    ListaSimple.insertar_posicion(estudiante,posicion)
                    print("Realizado con exito")
                except Exception as e:
                    print(f"Error : {e}")

            case 4 :
                try :
                    estudiante = registar_estudiante()
                    orden_simple.insertar_ordenado(estudiante)
                    print("Realizado con exito")
                except Exception as e:
                    print(f"Error : {e}")

            case 5 :
                try:
                    codigo = input("Ingrese el codigo del estudiante que busca")
                    estudiante = ListaSimple.buscar_codigo(codigo)
                    print(estudiante.__str__())
                except Exception as e:
                    print(f"Error : {e}")

            case 6 :
                try:
                    codigo = input("Ingrese el codigo del estudiante que busca")
                    nuevo_estudiante = registar_estudiante()
                    ListaSimple.modificar(codigo,nuevo_estudiante)
                    print("Realizado con exito")
                except Exception as e:
                    print(f"Error : {e}")

            case 7 :
                try:
                    ListaSimple.eliminar_primero()
                except Exception as e:
                    print(f"Error : {e}")

            case 8:
                try:
                    ListaSimple.eliminar_ultimo()
                except Exception as e:
                    print(f"Error : {e}")

            case 9:
                try:
                    codigo = input("Ingrese el codigo :")
                    ListaSimple.eliminar_codigo(codigo)
                except Exception as e:
                    print("Error : {e}")

            case 10:
                try:
                    posicion = leer_entero("Ingrese la posicion")
                    ListaSimple.eliminar_posicion(posicion)
                except Exception as e:
                    print (f"Error : {e}")

            case 11 :
                print(f"{'='*10}ESTUDIANTES REGISTRADOS {'='*10}")
                print(ListaSimple)
                print (f"{'='*10}"))

            case 12:
                print("Total de estudiantes registrados : ",ListaSimple.contar())

            case 13:
                try:
                    posicion = leer_entero("Ingrese la posicion : ")
                    estudiante = ListaSimple.obtener_posicion(posicion)
                    print(estudiante.__str__)
                except Exception as e:
                    print("Error : {e}")

            case 14:
                try:
                    orden_simple.ordenar(ListaSimple,'codigo')
                    print("Realizado con exito")
                except Exception as e:
                    print("Error : {e}")

            case 15:
                try:
                    orden_simple.ordenar(ListaSimple,'apellidos')
                    print("Realizado con exito")
                except Exception as e:
                    print("Error : {e}")

            case 16:
                try:
                    if ListaSimple.esta_vacia():
                    orden_simple.ordenar(ListaSimple,'promedio')
                    print("Realizado con exito")
                except Exception as e:
                    print("Error : {e}")

            case 17:
                ListaSimple.vaciar()

            
            case _ :
                print("Opcion fuera de rango")

        limpiar_pantalla()

def menu_lista_doble() -> None :
    while True:
        print(f'{"="*10}MENU LISTA DOBLE{"="*10}')
        print("1. Insertar Estudiante al inicio")
        print("2. Insertar Estudiante al final")
        print("3. Insertar Estudiante por posicion")
        print("4. Insertar Estudiante y ordenar por código")
        print("5. Buscar estudiante por codigo")
        print("6. Modificar estudiante por código")
        print("7. Eliminar el primer estudiante registrado")
        print("8. Elimnar el ultimo estudiante registrado")
        print("9. Eliminar estudiante por código")
        print("10. Eliminar estudiante por posicion")
        print("11. Listar todos los estudiantes")
        print("12. Numero de estudiantes registrados")
        print("13. Obtener estudiante por posicion")
        print("14. Ordenar estudiantes por código")
        print("15. Ordenar estudiantes por apellidos")
        print("16. Ordenar estudiantes por promedio")
        print("17. Vaciar lista")
        print("18. Insertar despues un estudiante (codigo)")
        print("19. Insertar antes de un estudiante (codigo)")
        print("20. Recorrer la lista de estudiantes de fin a inicio")
        print("0. Salir")
        numero = leer_entero("Ingrese una opcion")
        match numero :
            case 1 : 
                try:
                    estudiante = registar_estudiante()
                    Lista_doble.insertar_inicio(estudiante)
                    print("Realizado con exito")
                except Exception as e :
                    print (f"Error :{e}")

            case 2 :
                try:
                    estudiante = registar_estudiante()
                    Lista_doble.insertar_final(estudiante)
                    print("Realizado con exito")
                except Exception as e:
                    print (f"Error :{e}")

            case 3 :
                posicion = -1
                while posicion<0 :
                    posicion = leer_entero("Ingrese la posicion")
                    if posicion < 0:
                        print ("Ingrese un nuemero positivo")
                try:        
                    estudiante = registar_estudiante()
                    ListaSimple.insertar_posicion(estudiante,posicion)
                    print("Realizado con exito")
                except Exception as e:
                    print(f"Error : {e}")

            case 4 :
                try :
                    estudiante = registar_estudiante()
                    orden_simple.insertar_ordenado(estudiante)
                    print("Realizado con exito")
                except Exception as e:
                    print(f"Error : {e}")

            case 5 :
                try:
                    codigo = input("Ingrese el codigo del estudiante que busca")
                    estudiante = ListaSimple.buscar_codigo(codigo)
                    print(estudiante.__str__())
                except Exception as e:
                    print(f"Error : {e}")

            case 6 :
                try:
                    codigo = input("Ingrese el codigo del estudiante que busca")
                    nuevo_estudiante = registar_estudiante()
                    ListaSimple.modificar(codigo,nuevo_estudiante)
                    print("Realizado con exito")
                except Exception as e:
                    print(f"Error : {e}")

            case 7 :
                try:
                    ListaSimple.eliminar_primero()
                except Exception as e:
                    print(f"Error : {e}")

            case 8:
                try:
                    ListaSimple.eliminar_ultimo()
                except Exception as e:
                    print(f"Error : {e}")

            case 9:
                try:
                    codigo = input("Ingrese el codigo :")
                    ListaSimple.eliminar_codigo(codigo)
                except Exception as e:
                    print("Error : {e}")

            case 10:
                try:
                    posicion = leer_entero("Ingrese la posicion")
                    ListaSimple.eliminar_posicion(posicion)
                except Exception as e:
                    print (f"Error : {e}")

            case 11 :
                print(f"{'='*10}ESTUDIANTES REGISTRADOS {'='*10}")
                print(ListaSimple)
                print (f"{'='*10}"))

            case 12:
                print("Total de estudiantes registrados : ",ListaSimple.contar())

            case 13:
                try:
                    posicion = leer_entero("Ingrese la posicion : ")
                    estudiante = ListaSimple.obtener_posicion(posicion)
                    print(estudiante.__str__)
                except Exception as e:
                    print("Error : {e}")

            case 14:
                try:
                    orden_simple.ordenar(ListaSimple,'codigo')
                    print("Realizado con exito")
                except Exception as e:
                    print("Error : {e}")

            case 15:
                try:
                    orden_simple.ordenar(ListaSimple,'apellidos')
                    print("Realizado con exito")
                except Exception as e:
                    print("Error : {e}")

            case 16:
                try:
                    if ListaSimple.esta_vacia():
                    orden_simple.ordenar(ListaSimple,'promedio')
                    print("Realizado con exito")
                except Exception as e:
                    print("Error : {e}")

            case 17:
                ListaSimple.vaciar()

            
            case _ :
                print("Opcion fuera de rango")

                
        limpiar_pantalla()   

def limpiar_pantalla()-> None:
    os.system('cls')

def registar_estudiante()-> Estudiante:
    while True:
        codigo = input("Ingrese codigo :")
        if ListaSimple.codigo_existe(codigo):
            print("Codigo previamente ya registrado")
            continue
        break
    apellidos = input("Ingrese sus apellidos :")
    nombres = input("Ingrese sus nombres : ")
    carrera = input("Ingrese su carrera : ")
    ciclo = leer_entero("Ingrese su ciclo : ")
    promedio = leer_flotante("Ingrese su promedio:")
    return Estudiante (codigo,apellidos,nombres,carrera,ciclo,promedio)