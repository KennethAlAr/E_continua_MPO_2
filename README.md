# Gestor de Archivos en Consola

Este proyecto es un explorador y gestor de archivos básico que se ejecuta en la terminal, desarrollado en Python. Permite al usuario navegar por el sistema de archivos, crear, eliminar y modificar archivos y directorios a través de un menú interactivo.

## 🚀 Características

  * **Listado de contenido:** Muestra los archivos y carpetas del directorio actual además de la información básica del mismo directorio.
  * **Diferenciación visual:** Usa la librería `colorama` para mostrar iconos y colores distintos según el tipo de archivo (documento, imagen, vídeo, carpeta, etc.).
  * **Metadatos:** Muestra información relevante como la fecha de última modificación, el tamaño de los archivos, y el tamaño total y número de elementos dentro de las carpetas.
  * **Operaciones CRUD:**
      * Crear nuevos directorios.
      * Crear archivos `.txt` (con opción de escribir contenido inicial).
      * Añadir texto a archivos existentes.
      * Renombrar archivos y directorios.
      * Eliminar archivos y directorios (solo si están vacíos, por seguridad).
  * **Navegación:** Permite moverse a la carpeta padre (`cd ..`) o a una subcarpeta. Incluye una función especial para cambiar de unidad de disco en Windows si se llega a la raíz.
  * **Historial de Comandos:** Todas las acciones se registran en un archivo de log.

## 📋 Historial de Comandos

Todas las operaciones (crear, eliminar, renombrar, navegar) se registran en el archivo `historial/historial_de_comandos.txt` junto con la fecha y hora en formato `YYYY-MM-DD - HH:MM:SS`.

**Nota Importante:** Por diseño, el historial **se borra automáticamente** cada vez que se ejecuta `main.py` para evitar que el archivo de log crezca indefinidamente. Si deseas mantener un historial persistente, puedes eliminar o comentar las líneas 8 y 9 del archivo `main.py`.

## 🛠️ Instalación y Dependencias

El proyecto utiliza las librerías estándar de Python (`os`, `datetime`) y una librería externa:

  * `colorama`: Para dar color y estilo a la salida de la terminal.

### Uso de `requirements.txt`

Para instalar las dependencias necesarias, sigue estos pasos:

1.  Crea y activa un entorno virtual:

    ```bash
    # Crear el entorno
    python -m venv venv

    # Activar en Windows
    .\venv\Scripts\activate

    # Activar en macOS/Linux
    source venv/bin/activate
    ```

2.  Instala las dependencias desde el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Ejecución

Una vez instaladas las dependencias, puedes ejecutar el programa desde la carpeta raíz del proyecto:

```bash
python main.py
```

Aparecerá un menú interactivo en la consola para empezar a gestionar tus archivos.

## 📂 Estructura de Archivos

```
.
├── main.py                         # Script principal, contiene el menú.
├── funcionalidades/
│   ├── comandos.py                 # Lógica principal de todas las operaciones del menú.
│   └── auxiliar.py                 # Funciones de ayuda (formatear fecha, tamaño, etc.).
├── historial/
│   └── historial_de_comandos.txt   # Archivo de log.
├── requirements.txt                # Lista de dependencias.
└── README.md                       # Archivo README.
```