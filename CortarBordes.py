from PIL import Image
from tkinter import filedialog
import os



def recortar_borde_arriba(imagen_ruta):
    # Abrir la imagen
    imagen = Image.open(imagen_ruta)
    ancho, alto = imagen.size

    # Calcular la altura del recorte
    altura_recorte_superior = int(alto * 0.095)

    # Definir el área de recorte
    area_recorte = (0, altura_recorte_superior, ancho, alto)  # (left, top, right, bottom)

    # Recortar la imagen
    imagen_recortada = imagen.crop(area_recorte)

    # Guardar la imagen recortada
    imagen_recortada.save(imagen_ruta)

def recortar_borde_ambos(imagen_ruta):
    # Abrir la imagen
    imagen = Image.open(imagen_ruta)
    ancho, alto = imagen.size

    # Calcular la altura del recorte
    altura_recorte = int(alto * 0.175)

    # Calcular la altura del recorte
    altura_recorte_superior = int(alto * 0.095)

    # Definir el área de recorte
    area_recorte = (0, altura_recorte_superior, ancho, alto - altura_recorte)  # (left, top, right, bottom)

    # Recortar la imagen
    imagen_recortada = imagen.crop(area_recorte)

    # Guardar la imagen recortada
    imagen_recortada.save(imagen_ruta)


def recortar_bordes(ruta_imagenes, mapas):
    imagenes = len(os.listdir(ruta_imagenes))
    for i in range (1, imagenes+1):
        if i <= mapas:
            recortar_borde_arriba(ruta_imagenes+f"\{i}.jpg")
        else:
            recortar_borde_ambos(ruta_imagenes+f"\{i}.jpg")



    




