from PIL import Image
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
    altura_recorte_inferior = int(alto * 0.174)

    # Calcular la altura del recorte
    altura_recorte_superior = int(alto * 0.095)

    # Definir el área de recorte
    area_recorte = (0, altura_recorte_superior, ancho, alto - altura_recorte_inferior)  # (left, top, right, bottom)

    # Recortar la imagen
    imagen_recortada = imagen.crop(area_recorte)

    # Guardar la imagen recortada
    imagen_recortada.save(imagen_ruta)

def recortar_bordes(ruta_imagenes, cant_mapas):
    imagenes = len(os.listdir(ruta_imagenes))
    n = 0
    for i in range (imagenes,0,-1):
        if n < cant_mapas:
            recortar_borde_arriba(ruta_imagenes+f"\{i}.jpg")
            n+=1
        else:
            recortar_borde_ambos(ruta_imagenes+f"\{i}.jpg")    
