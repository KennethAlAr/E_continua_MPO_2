from funcionalidades.auxiliar import *
from colorama import Style, Fore, Back
import os


def listar_contenido(ruta):
    try:
        contenido = os.listdir(ruta)
    except PermissionError:
        print("No tienes los permisos necesarios para ver esta carpeta.")
        return
    print(f"{Back.BLUE}Contenido de {os.path.abspath(ruta)}{Style.RESET_ALL}")
    for elemento in contenido:
        if os.path.isdir(ruta + elemento):
            print(f"{Fore.YELLOW}    -📁 {elemento} - {ver_fecha(ruta + elemento)} - {ver_tamano_carpeta(ruta + elemento)} - {ver_numero_elementos(ruta + elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["txt", "docx", "doc", "odt", "rtf"]:
            print(f"{Fore.BLUE}    -📃 {elemento} - {ver_fecha(ruta + elemento)} - {ver_tamano(ruta + elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["jpg", "jpeg","png", "gif", "svg", "webp", "tiff", "tif", "bmp", "heic", "heif"]:
            print(f"{Fore.RED}    -📷 {elemento} - {ver_fecha(ruta + elemento)} - {ver_tamano(ruta + elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["mp3", "wma", "wav", "aac", "flac"]:
            print(f"{Fore.MAGENTA}    -🎵 {elemento} - {ver_fecha(ruta + elemento)} - {ver_tamano(ruta + elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["mp4", "wmv", "mov", "avi", "mkv", "webm"]:
            print(f"{Fore.CYAN}    -📽️ {elemento} - {ver_fecha(ruta + elemento)} - {ver_tamano(ruta + elemento)}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["py", "java", "html", "css", "js"]:
            print(f"{Fore.GREEN}    -🤖 {elemento} - {ver_fecha(ruta + elemento)} - {ver_tamano(ruta + elemento)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.WHITE}    -❓ {elemento} - {ver_fecha(ruta + elemento)} - {ver_tamano(ruta + elemento)} {Style.RESET_ALL}")
    print()
    anadir_comando_historial(f"Listado contenido de {ruta}")

def crear_directorio():
    # Crea una nueva carpeta
    pass

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

def ver_historial():
    with open("historial/historial_de_comandos.txt", "r") as log:
        lineas = log.readlines()
        for linea in lineas:
            print(linea.strip()) #Ponemos el strip porque cada linea ya tiene un \n al final. Si lo dejamos queda un espacio entre lineas

def ir_carpeta_padre(ruta):
    ruta_splitted = ruta.split(os.sep) 
    #Estaba teniendo problemas con el separador (En windows es "\" pero en linux es "/"), pero con os.sep lo pone dinámicamente dependiendo del sistema operativo que se use
    if len(ruta_splitted) == 2:
        #Tanto si la ruta es "C:\"(Windows) o "/"(Linux) el split con os.sep crea una lista de len = 2 (["C:", ""] o ["", ""]) En este caso dejamos la ruta como está porque no queremos subir mas.
        return ruta
    ruta_splitted.pop()
    ruta_splitted.pop()
    #Como la rutas que trabajo siempre tienen un separador al final, debo hacer pop() dos veces para eliminar el espacio vacío y el penúltimo elemento de la lista
    ruta_padre = os.sep.join(ruta_splitted) + os.sep
    anadir_comando_historial(f"Cambiado directorio a {ruta_padre}")
    return ruta_padre

def ir_subcarpeta(ruta):
    print(f"{Back.BLUE}Subdirectorios de {os.path.abspath(ruta)}{Style.RESET_ALL}:")
    carpetas = []
    try:
        for elemento in os.listdir(ruta):
            if os.path.isdir(ruta+elemento):
                carpetas.append(elemento)
    except PermissionError:
        print("No tienes los permisos necesarios para ver esta carpeta.")
    while True:
        if len(carpetas) == 0:
            print("No hay subdirectorios en la carpeta actual.")
            return ruta
        else:
            ver_carpetas(ruta)
            try:
                opcion = int(input("Introduce el número de la carpeta a la que quieres ir:\n"))
            except ValueError:
                print("Por favor, introduce un número válido.")
            try:
                anadir_comando_historial(f"Cambiado directorio a {ruta + carpetas[opcion-1] + os.sep}")
                return ruta + carpetas[opcion-1] + os.sep
            except IndexError:
                print("Por favor, introduce un número válido.")


def mostrar_ruta(ruta):
    return f"{Back.BLUE}Ruta actual: {ruta}{Style.RESET_ALL}"