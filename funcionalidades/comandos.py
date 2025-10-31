from funcionalidades.auxiliar import *
from colorama import Style, Fore, Back
import os
import datetime


def listar_contenido(ruta):
    contenido = os.listdir(ruta)
    print(f"{Back.BLUE}Contenido de {os.path.abspath(ruta)}{Style.RESET_ALL}")
    for elemento in contenido:
        if os.path.isdir(ruta+elemento):
            print(f"{Fore.YELLOW}    -📁 {elemento} - Última modificación: {formatear_fecha(os.path.getmtime(ruta+elemento))} - peso - {len(os.listdir(ruta+elemento))} elementos dentro{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["txt", "docx", "doc", "odt", "rtf"]:
            print(f"{Fore.BLUE}    -📃 {elemento} - Última modificación: {formatear_fecha(os.path.getmtime(ruta+elemento))} - {formatear_tamano(os.path.getsize(ruta+elemento))}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["jpg", "jpeg","png", "gif", "svg", "webp", "tiff", "tif", "bmp", "heic", "heif"]:
            print(f"{Fore.RED}    -📷 {elemento} - Última modificación: {formatear_fecha(os.path.getmtime(ruta+elemento))} - {formatear_tamano(os.path.getsize(ruta+elemento))}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["mp3", "wma", "wav", "aac", "flac"]:
            print(f"{Fore.MAGENTA}    -🎵 {elemento} - Última modificación: {formatear_fecha(os.path.getmtime(ruta+elemento))} - {formatear_tamano(os.path.getsize(ruta+elemento))}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["mp4", "wmv", "mov", "avi", "mkv", "webm"]:
            print(f"{Fore.CYAN}    -📽️ {elemento} - Última modificación: {formatear_fecha(os.path.getmtime(ruta+elemento))} - {formatear_tamano(os.path.getsize(ruta+elemento))}{Style.RESET_ALL}")
        elif elemento.split(".")[-1] in ["py", "java", "html", "css", "js"]:
            print(f"{Fore.GREEN}    -🤖 {elemento} - Última modificación: {formatear_fecha(os.path.getmtime(ruta+elemento))} - {formatear_tamano(os.path.getsize(ruta+elemento))}{Style.RESET_ALL}")
        else:
            print(f"{Fore.WHITE}    -❓ {elemento} - Última modificación: {formatear_fecha(os.path.getmtime(ruta+elemento))} - {formatear_tamano(os.path.getsize(ruta+elemento))} {Style.RESET_ALL}")

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

def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    pass

def renombrar_elemento():
    # Renombra un archivo o carpeta
    pass

def ver_historial():
    # Muestra el historial de comandos utilizados
    pass

def mostrar_ruta():
    print(os.getcwd())