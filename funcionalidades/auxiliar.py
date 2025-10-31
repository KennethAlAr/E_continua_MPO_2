import os
import datetime
    
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