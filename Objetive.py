from tkinter import filedialog
import tkinter as tk
from EditarPowerPoint import *
from CrearImagenes import *
from CortarBordes import recortar_bordes

def seleccionar_directorio():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    # Solicitar al usuario que seleccione el directorio principal
    directorio_principal = filedialog.askdirectory(title="Nuevo Objetivo: Eliga la carpeta donde guardara las imagenes")
    if not directorio_principal:
        print("No se ha seleccionado un directorio principal. Saliendo del programa.")
        return
    else:
        return directorio_principal
    
def solicitar_cantidad_mapas():
    """Solicitar al usuario la cantidad de mapas y validar la entrada."""
    while True:
        try:
            return int(input("Cantidad de Mapas: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            

if __name__ == "__main__":
    #Seleccionar Carpeta destino
    destino = seleccionar_directorio()

    # Abrir cuadro de diálogo para seleccionar el archivo PowerPoint
    archivo_pptx = filedialog.askopenfilename(
        title="Selecciona un archivo PowerPoint",
        filetypes=[("PowerPoint files", "*.pptx")]
    )
    if not archivo_pptx:
        exit()

    cantMapas = solicitar_cantidad_mapas()
    # Ejecutar funciones
    try:
        quitarElementos(archivo_pptx)
        powerpoint_to_images(os.path.abspath(archivo_pptx),os.path.abspath(destino))
        recortar_bordes(destino, cantMapas)
   
    except Exception as e:
        print (f"Se produjo un error {e}")    

