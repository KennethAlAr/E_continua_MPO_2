from funcionalidades.comandos import *
import os

ruta_log = os.path.abspath("historial/historial_de_comandos.txt")
#Cada vez que corre el código se borra el historial para que no acabe pesando demasiado, pero las líneas 6 y 7 podrían borrarse para mantenerlo activo.
with open(ruta_log, "w"):
    pass

def menu_principal():
    opcion = ""
    while opcion != 0:
        print(f"{Back.BLUE}Ruta actual: {os.getcwd()}{Style.RESET_ALL}")
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
            pass # Aunque salga el error, el match recogerá la opción default.

        match opcion:
            case 1:
                listar_contenido(ruta_log)
            case 2:
                crear_directorio(ruta_log)
            case 3:
                crear_archivo(ruta_log)
            case 4:
                escribir_en_archivo(ruta_log)
            case 5:
                eliminar_elemento()
            case 6:
                renombrar_elemento(ruta_log)
            case 7:
                ver_historial(ruta_log)
            case 8:
                ir_carpeta_padre(ruta_log)
            case 9:
                ir_subcarpeta(ruta_log)
            case _:
                print("Por favor, introduce una de las opciones indicadas en el menú.")

menu_principal()

#Mostrar información de archivo ya se ve en listar información