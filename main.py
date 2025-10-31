from funcionalidades.comandos import *
import os

ruta = os.getcwd() + os.sep

def menu_principal(ruta):
    ruta_actual = ruta
    opcion = ""
    while opcion != 0:
        print(mostrar_ruta(ruta_actual))
        print('''Selecciona una opción:
            1. Listar contenido del directorio actual
            2. Crear un nuevo directorio
            3. Crear un archivo de texto
            4. Escribir texto en un archivo existente
            5. Eliminar un archivo o directorio
            6. Renombrar archivo o directorio
            7. Ver historial de comandos
            8. Ir a carpeta padre
            9. Ir a subcarpeta
            0. Salir''')
    
        try:
            opcion = int(input())
        except ValueError:
            print("Por favor, introduce una de las opciones indicadas en el menú.\n")

        match opcion:
            case 1:
                listar_contenido(ruta_actual)
            case 2:
                crear_directorio()
            case 3:
                crear_archivo()
            case 4:
                escribir_en_archivo()
            case 5:
                eliminar_elemento()
            case 6:
                renombrar_elemento()
            case 7:
                ver_historial()
            case 8:
                ruta_actual = ir_carpeta_padre(ruta_actual)
            case 9:
                ruta_actual = ir_subcarpeta(ruta_actual)

menu_principal(ruta)