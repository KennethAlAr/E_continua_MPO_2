import os
import datetime
from colorama import Fore, Back, Style
    
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
        #Por lo que he podido probar en linux hay una especie de acceso directo que el programa reconoce como archivos pero no lo son. Estos enlaces apuntan a otro archivo.
        #os.path.getsize()/getmtime()/listdir() no lo pueden leer y salta un error (FileNotFoundError, NotADirectoryError o PermissionError)
        #Los encapsulamos todos y si saltan devolvemos un mensaje de acceso denegado (en el caso de calcular tamaño de carpeta, no devolvemos nada a la suma).
    except Exception:
        return "[Acceso denegado]"

def ver_tamano(ruta):
    try:
        return formatear_tamano(os.path.getsize(ruta))
    except Exception:
        return "[Acceso denegado]"
    
def ver_numero_elementos(ruta):
    try:
        return f"{len(os.listdir(ruta))} elementos dentro"
    except Exception:
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
            try:
                total += os.path.getsize(ruta_archivo)
            except Exception:
                pass

    return formatear_tamano(total)

def ver_carpetas():
    carpetas = []
    try:
        for elemento in os.listdir(os.getcwd()):
            if os.path.isdir(elemento):
                carpetas.append(elemento)
    except PermissionError:
        pass # Si no tenemos permisos para ver una carpeta no la lista
    for i in range(len(carpetas)):
        print(f"{Fore.YELLOW}    {i+1}.-📁 {carpetas[i]}{Style.RESET_ALL}")

def anadir_comando_historial(ruta, mensaje):
    with open(ruta, "a", encoding='utf-8') as log:
        log.write(f"{datetime.datetime.now().strftime("%Y-%m-%d - %H:%M:%S")} - {mensaje}\n")

def cambiar_unidades_windows():
    unidades = []
    for letra in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        unidad = f"{letra}:\\"
        if os.path.exists(unidad):
            unidades.append(unidad)
    
    while True:
        for i in range(len(unidades)):
            print(f"{Back.BLUE}    {i+1}.-💾 {unidades[i]}{Style.RESET_ALL}")
        print("Introduce el número de la unidad a la que quieres ir:")
        try:
            opcion = int(input())
            try:
                os.chdir(unidades[opcion-1])
                return
            except IndexError:
                print("Por favor, introduce una opción válida.")
            except PermissionError:
                print("No tienes los permisos para acceder a esta unidad.")
        except ValueError:
            print("Por favor, introduce una opción válida.")

def contar_carpetas():
    contador = 0
    try:
        for elemento in os.listdir(os.getcwd()):
            if os.path.isdir(elemento):
                contador += 1
        return f"{contador} carpetas"
    except PermissionError:
        return "[Acceso denegado]"

def contar_archivos():
    contador = 0
    total = 0
    try:
        for elemento in os.listdir(os.getcwd()):
            if not os.path.isdir(elemento):
                contador += 1
                try:
                    total += os.path.getsize(elemento)
                except Exception:
                    pass
        return f"{contador} archivos ({formatear_tamano(total)})"
    except PermissionError:
        return "[Acceso denegado]"