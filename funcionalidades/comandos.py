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
    nombre = input("Escribe el nombre de la nueva carpeta que quieres crear:\n")
    try:
        if os.path.exists(os.path.join(os.getcwd(), nombre)):
            if os.path.isdir(os.path.join(os.getcwd(), nombre)):
                print("Ya existe un directorio con ese nombre")
                return
            else:
                print("Ya existe un archivo con ese nombre")
                return
        os.mkdir(os.path.join(os.getcwd(), nombre))
        print(f"Creado directorio '{nombre}' en {os.getcwd()}")
        anadir_comando_historial(ruta_log, f"creado directorio {os.path.join(os.getcwd(), nombre)}")
    except PermissionError:
        print("No tienes los permisos para crear un directorio en esta carpeta.")
        return
    except Exception:
        print("Nombre de carpeta no válido.")


def crear_archivo(ruta_log):
    nombre = input("Escribe el nombre del nuevo archivo de texto que quieres crear (No hace falta poner la extensión):\n")
    try:
        if os.path.exists(os.path.join(os.getcwd(), nombre + ".txt")):
            print("El archivo que quieres crear ya existe.")
            return
        with open(os.path.join(os.getcwd(), nombre + ".txt"), "w", encoding="utf-8") as archivo:
            print('''¿Quieres escribir algo en el archivo?
    1- Sí
    2- No''')
            while True:
                try:
                    opcion = int(input())
                except ValueError:
                    print("Por favor, introduce una opción válida")
                    continue
                match(opcion):
                    case 1:
                        lineas = []
                        while True:                            
                            linea = input("Escribe el texto que quieres o pulsa 'Enter' sin nada escrito para terminar:\n")
                            if linea == "":
                                break
                            lineas.append(linea + "\n")
                        archivo.writelines(lineas)
                        print(f"Creado archivo {nombre}.txt")
                        anadir_comando_historial(ruta_log, f"creado archivo {nombre + ".txt"} en directorio {os.getcwd()}")
                        return
                    case 2:
                        print(f"Creado archivo {nombre}.txt")
                        anadir_comando_historial(ruta_log, f"Creado archivo {nombre + ".txt"} en directorio {os.getcwd()}")
                        return
                    case _:
                        print("Por favor, introduce una opción válida")
    except PermissionError:
        print("No tienes los permisos para crear un directorio en esta carpeta.")
        return
    except Exception:
        print("Nombre de carpeta no válido.")

def escribir_en_archivo(ruta_log):
    nombre = input("Escribe el nombre del archivo en el que quieres escribir:\n")
    try:
        if not os.path.exists(os.path.join(os.getcwd(), nombre)):
            print("El archivo no existe.\n")
            return
        with open (os.path.join(os.getcwd(), nombre), "a") as archivo:
            lineas = []
            while True:                            
                linea = input("Escribe el texto que quieres o pulsa 'Enter' sin nada escrito para terminar:\n")
                if linea == "":
                    break
                lineas.append(linea + "\n")
            archivo.writelines(lineas)
            print(f"Escrito en archivo {nombre}\n")
            anadir_comando_historial(ruta_log, f"Escrito en archivo {nombre} en directorio {os.getcwd()}")
            return
    except PermissionError:
        print(f"No tienes los permisos para escribir en {nombre}.")
        return

def eliminar_elemento(ruta_log):
    nombre = input("Escribe el nombre del archivo o directorio que quieres eliminar:\n")
    if not os.path.exists(os.path.join(os.getcwd(), nombre)):
        print("El archivo o directorio no existe.")
        return
    if os.path.isdir(nombre):
        while True:
            try:
                opcion = int(input(f'''Se va a eliminar el directorio {nombre}, ¿Estás seguro?
    1-Sí
    2-No'''))
                match opcion:
                    case 1:
                        os.rmdir(nombre)
                        print(f"Eliminado directorio {nombre}.")
                        anadir_comando_historial(ruta_log, f"Eliminado directorio '{nombre}' en directorio {os.getcwd()}")
                        return
                    case 2:
                        print(f"Eliminación de {nombre} cancelada.")
                        return
                    case _:
                        print("Por favor, introduce una opción válida.")
            except ValueError:
                print("Por favor, introduce una opción válida.")
            except PermissionError:
                print(f"No tienes los permisos para eliminar {nombre}.")
                return
            except OSError:
                print(f"El directorio {nombre} debe estar vacío para poder eliminarlo.")
                return
    while True:
        try:
            opcion = int(input(f'''Se va a eliminar el archivo {nombre}, ¿Estás seguro?
    1-Sí
    2-No'''))
            match opcion:
                case 1:
                    os.remove(nombre)
                    print(f"Eliminado archivo {nombre}.")
                    anadir_comando_historial(ruta_log, f"Eliminado archivo '{nombre}' en directorio {os.getcwd()}")
                    return
                case 2:
                    print(f"Eliminación de {nombre} cancelada.")
                    return
                case _:
                    print("Por favor, introduce una opción válida.")
        except ValueError:
            print("Por favor, introduce una opción válida.")
        except PermissionError:
            print(f"No tienes los permisos para eliminar {nombre}.")
            return

def renombrar_elemento(ruta_log):
    nombre = input("Escribe el nombre del archivo o directorio que quieres renombrar:\n")
    nuevo_nombre = input(f"Escribe el nuevo nombre para '{nombre}':\n")
    try:
        os.rename(nombre, nuevo_nombre)
        if os.path.isdir(nuevo_nombre):
            print(f"Directorio '{nombre}' renombrado a '{nuevo_nombre}'.\n")
            anadir_comando_historial(ruta_log, f"Directorio {nombre} renombrado a '{nuevo_nombre}' en directorio {os.getcwd()}")
        else:
            print(f"Archivo '{nombre}' renombrado a '{nuevo_nombre}'.\n")
            anadir_comando_historial(ruta_log, f"Archivo '{nombre}' renombrado a '{nuevo_nombre}' en directorio {os.getcwd()}")
    except FileNotFoundError:
        print(f"El archivo o directorio '{nombre}' no existe.\n")
    except FileExistsError:
        if os.path.isdir(nuevo_nombre):
            print(f"Ya existe un directorio llamado '{nuevo_nombre}'.")
        else:            
            print(f"Ya existe un archivo llamado '{nuevo_nombre}'.")
        return
    except OSError:
        if os.path.isdir(nombre):
            print(f"No tienes los permisos para renombrar el directorio '{nombre}' o el directorio está en uso.")
        else:            
            print(f"No tienes los permisos para renombrar el archivo '{nombre}' o el archivo está en uso.")

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
            