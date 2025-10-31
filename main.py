from funcionalidades.comandos import *

def menu_principal():
    opcion = ""
    while opcion != 0:
        print('''Selecciona una opción:
          1. Listar contenido del directorio actual
          2. Crear un nuevo directorio
          3. Crear un archivo de texto
          4. Escribir texto en un archivo existente
          5. Eliminar un archivo o directorio
          6. Mostrar información del archivo
          7. Renombrar archivo o directorio
          8. Ver historial de 
          0. Salir''')
    
        try:
            opcion = int(input())
        except ValueError:
            print("Por favor, introduce una de las opciones indicadas en el menú.\n")

        match opcion:
            case 1:
                listar_contenido("./")
            case 2:
                crear_directorio()
            case 3:
                crear_archivo()
            case 4:
                escribir_en_archivo()
            case 5:
                eliminar_elemento()
            case 6:
                mostrar_informacion()
            case 7:
                renombrar_elemento()
            case 8:
                ver_historial()
            case 9:
                mostrar_ruta()

menu_principal()