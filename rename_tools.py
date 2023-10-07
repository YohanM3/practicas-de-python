import os

# Definir la ruta del directorio donde están los archivos a renombrar
directorio = "C:/Users/Usuario/Documents/Archivos"

# Obtener la lista de los nombres de los archivos en el directorio
archivos = os.listdir(directorio)

# Definir el prefijo que se usará para renombrar los archivos
prefijo = "nuevo_nombre_"

# Recorrer la lista de archivos y renombrar cada uno usando el prefijo y un número consecutivo
for i, archivo in enumerate(archivos):
    # Obtener la extensión del archivo
    extension = os.path.splitext(archivo)[1]
    # Construir el nuevo nombre del archivo
    nuevo_nombre = prefijo + str(i+1) + extension
    # Renombrar el archivo usando os.rename()
    os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_nombre))
