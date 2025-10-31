import os
import datetime
from colorama import Fore, Style
    
def formatear_fecha(fecha):
    fecha_datetime = datetime.datetime.fromtimestamp(fecha)
    fecha_formateada = fecha_datetime.strftime("%d-%m-%Y %H:%M")
    return fecha_formateada

def formatear_tamano(tamano):
    if tamano < 1024:
        return f"{tamano} bytes"
    elif tamano < 1024**2:
        tamano_kb = tamano/1024
        return f"{tamano_kb:.2f} KB"
    elif tamano < 1024**3:
        tamano_mb = tamano/(1024**2)
        return f"{tamano_mb:.2f} MB"
    else:
        tamano_gb = tamano/(1024**3)
        return f"{tamano_gb:.2f} GB"

def ver_fecha(ruta):
    try:
        return formatear_fecha(os.path.getmtime(ruta))
    except PermissionError:
        return "[Acceso denegado]"

def ver_tamano(ruta):
    try:
        return formatear_tamano(os.path.getsize(ruta))
    except PermissionError:
        return "[Acceso denegado]"
    
def ver_numero_elementos(ruta):
    try:
        return f"{len(os.listdir(ruta))} elementos dentro"
    except PermissionError:
        return "[Acceso denegado]"

def ver_tamano_carpeta(ruta_carpeta):
    total = 0

    #Al principio tenía un try/except para esta función, pero os.walk() no eleva un error si encuentra una carpeta a la que no puede entrar o un archivo roto.
    #Simplemente no cuenta ese archivo o carpeta y ya está.
    for ruta, subcarpetas, archivos in os.walk(ruta_carpeta):
        #os.walk genera tres elementos: la ruta actual, una lista de subcarpetas y una lista de los archivos dentro de la carpeta y subcarpetas.
        #Solo queremos información del tercer elemento
        for archivo in archivos:
            #Con el segundo for recorremos todos los archivos de la carpeta original y de las subsiguientes subcarpetas
            ruta_archivo = os.path.join(ruta, archivo)
            total += os.path.getsize(ruta_archivo)

    return formatear_tamano(total)

def ver_carpetas(ruta):
    carpetas = []
    for elemento in os.listdir(ruta):
        if os.path.isdir(ruta+elemento):
            carpetas.append(elemento)
    for i in range(len(carpetas)):
        print(f"{Fore.YELLOW}    {i+1}.-📁 {carpetas[i]}{Style.RESET_ALL}")

def anadir_comando_historial(mensaje):
    with open("historial/historial_de_comandos.txt", "a") as log:
        log.write(f"{datetime.datetime.now().isoformat(timespec="seconds")} - {mensaje}\n")