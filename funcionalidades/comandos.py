from funcionalidades.auxiliar import *
from colorama import Style, Fore, Back
import os


def listar_contenido(ruta_log):
    ruta = os.getcwd()
    try:
        contenido = os.listdir(ruta)
    except PermissionError:
        print("No tienes los permisos necesarios para ver esta carpeta.")
        return
    print(f"{Back.BLUE}Contenido de {ruta}{Style.RESET_ALL}")
    for elemento in contenido:
        if os.path.isdir(elemento):
            print(f"{Fore.YELLOW}    -📁 {elemento} - {ver_fecha(elemento)} - {ver_tamano_carpeta(elemento)} - {ver_numero_elementos(elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["txt", "docx", "doc", "odt", "rtf"]:
            print(f"{Fore.BLUE}    -📃 {elemento} - {ver_fecha(elemento)} - {ver_tamano(elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["jpg", "jpeg","png", "gif", "svg", "webp", "tiff", "tif", "bmp", "heic", "heif"]:
            print(f"{Fore.RED}    -📷 {elemento} - {ver_fecha(elemento)} - {ver_tamano(elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["mp3", "wma", "wav", "aac", "flac"]:
            print(f"{Fore.MAGENTA}    -🎵 {elemento} - {ver_fecha(elemento)} - {ver_tamano(elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["mp4", "wmv", "mov", "avi", "mkv", "webm"]:
            print(f"{Fore.CYAN}    -📽️ {elemento} - {ver_fecha(elemento)} - {ver_tamano(elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["py", "java", "html", "css", "js"]:
            print(f"{Fore.GREEN}    -🤖 {elemento} - {ver_fecha(elemento)} - {ver_tamano(elemento)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.WHITE}    -❓ {elemento} - {ver_fecha(elemento)} - {ver_tamano(elemento)} {Style.RESET_ALL}")
    print()
    anadir_comando_historial(ruta_log, f"Listado contenido de {ruta}")

def crear_directorio(ruta_log):
    nombre = input("Escribe el nombre de la nueva carpeta que quieres crear:")
    if os.path.isdir(os.path.join(os.getcwd(), nombre)):
        print("Ya existe un directorio con ese nombre")
        anadir_comando_historial(ruta_log, f"Intento fallido de crear directorio {os.path.join(os.getcwd(), nombre)}, el directorio ya existe")
        return
    os.mkdir(os.path.join(os.getcwd(), nombre))
    print(f"Creado directorio '{nombre}' en {os.getcwd()}")
    anadir_comando_historial(ruta_log, f"creado directorio {os.path.join(os.getcwd(), nombre)}")

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    pass

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    pass

def eliminar_elemento():
    # Elimina un archivo o carpeta
    pass

def renombrar_elemento():
    # Renombra un archivo o carpeta
    pass

def ver_historial(ruta_log):
    with open(ruta_log, "r", encoding='utf-8') as log:
        lineas = log.readlines()
        for linea in lineas:
            print(linea.strip()) #Ponemos el strip porque cada linea ya tiene un \n al final. Si lo dejamos queda un espacio entre lineas

def ir_carpeta_padre(ruta_log):
    ruta_actual = os.getcwd()
    try:
        os.chdir("..")
        # Si llegamos a la raíz y seguimos intentando ir a la carpeta padre, ponemos la opción en windows de cambiar de unidad de disco duro
        if os.getcwd() == ruta_actual: #Aquí hacemos la comprovación para saber si ya estamos en la carpeta raíz
            if os.name == "nt": #Aquí hacemos la comprovación para saber si estamos en Windows
                opcion = 0
                print('''Has llegado a la raíz en windows de esta unidad, ¿Quieres cambiar de unidad?
    1 - Sí
    2 - No''')
                while opcion != 2:
                    try:
                        opcion = int(input())
                        if opcion == 1:
                            print("Mostrando unidades disponibles:")
                            cambiar_unidades_windows()
                            anadir_comando_historial(ruta_log, f"Cambiada unidad a {os.getcwd()}")
                            return
                        elif opcion == 2:
                            return
                        else:
                            print("Por favor, introduce una opción válida")
                    except Exception:
                        print("Por favor, introduce una opción válida")            
    except PermissionError:
        print("No tienes los permisos para acceder a esta carpeta.")
    anadir_comando_historial(ruta_log, f"Cambiado directorio a {os.getcwd()}")

def ir_subcarpeta(ruta_log):
    ruta = os.getcwd()
    carpetas = []
    try:
        for elemento in os.listdir(ruta):
            if os.path.isdir(elemento):
                carpetas.append(elemento)
    except PermissionError:
        pass #Si no tenemos permisos para ver la carpeta directamente no aparecen.
    if len(carpetas) == 0:
        print("No hay subdirectorios en la carpeta actual.")
        return
    else:
        while True:
            print(f"{Back.BLUE}Subdirectorios de {os.path.abspath(ruta)}{Style.RESET_ALL}:")
            ver_carpetas()
            try:
                opcion = int(input("Introduce el número de la carpeta a la que quieres ir:\n"))
                os.chdir(carpetas[opcion-1])
                anadir_comando_historial(ruta_log, f"Cambiado directorio a {os.getcwd()}")
                return
            except Exception:
                print("Por favor, introduce un número válido.")
            