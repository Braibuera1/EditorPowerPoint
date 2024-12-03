from PIL import Image
from tkinter import filedialog
import os



def recortar_bordes_blancos(imagen_ruta, porcentaje):
    # Abrir la imagen
    imagen = Image.open(imagen_ruta)
    ancho, alto = imagen.size

    # Calcular la altura del recorte
    altura_recorte = int(alto * porcentaje)

    # Definir el área de recorte
    area_recorte = (0, altura_recorte, ancho, alto)  # (left, top, right, bottom)

    # Recortar la imagen
    imagen_recortada = imagen.crop(area_recorte)

    # Guardar la imagen recortada
    imagen_recortada.save(imagen_ruta)

def recortar_bordes_debajo(imagen_ruta, porcentaje):
    # Abrir la imagen
    imagen = Image.open(imagen_ruta)
    ancho, alto = imagen.size

    # Calcular la altura del recorte
    altura_recorte = int(alto * porcentaje)

    # Definir el área de recorte
    area_recorte = (0, 0, ancho, alto - altura_recorte)  # (left, top, right, bottom)

    # Recortar la imagen
    imagen_recortada = imagen.crop(area_recorte)

    # Guardar la imagen recortada
    imagen_recortada.save(imagen_ruta)


# Solicitar al usuario que seleccione el directorio principal
# Abrir el cuadro de diálogo para seleccionar varios archivos de imagen
archivos_seleccionados = filedialog.askopenfilenames(
    title="Selecciona imágenes",
    filetypes=[
        ("Archivos de Imagen", "*.png;*.jpg;*.jpeg;*"),
        ("Todos los archivos", "*.*")  # Opción para todos los archivos si es necesario
    ]
)

if not archivos_seleccionados:
    print("No se ha seleccionado nada. Saliendo del programa.")
else:
    for archivo in archivos_seleccionados:
        recortar_bordes_blancos(archivo, 0.09)
    print("Proceso completado.")

# Solicitar al usuario que seleccione el directorio principal
# Abrir el cuadro de diálogo para seleccionar varios archivos de imagen
archivos_seleccionados = filedialog.askopenfilenames(
    title="Recortar debajo",
    filetypes=[
        ("Archivos de Imagen", "*.png;*.jpg;*.jpeg;*"),
        ("Todos los archivos", "*.*")  # Opción para todos los archivos si es necesario
    ]
)

if not archivos_seleccionados:
    print("No se ha seleccionado nada. Saliendo del programa.")
else:
    for archivo in archivos_seleccionados:
        recortar_bordes_debajo(archivo, 0.18)
    print("Proceso completado.")
