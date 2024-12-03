import os
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import keyboard

def seleccionar_directorio():
    global directorio_principal
    # Crear una ventana de selección de directorio
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter

    # Solicitar al usuario que seleccione el directorio principal
    directorio_principal = filedialog.askdirectory(title="Selecciona el directorio principal")
    if not directorio_principal:
        print("No se ha seleccionado un directorio principal. Saliendo del programa.")
        return
    procesar_directorio()

def procesar_directorio():
    if not directorio_principal:
        print("Directorio no seleccionado.")
        return

    subdirectorios = os.listdir(directorio_principal)
    for i, subdirectorio in enumerate(subdirectorios):
        ruta_subdirectorio = os.path.join(directorio_principal, subdirectorio)

        if os.path.isdir(ruta_subdirectorio):
            formato_directorio = os.path.join(ruta_subdirectorio, "Formato de reproductor de medios")

            if os.path.isdir(formato_directorio):
                carpetas = os.listdir(formato_directorio)

                if carpetas:
                    ruta_carpeta = os.path.join(formato_directorio, carpetas[0])
                    nueva_nombre = os.path.join(directorio_principal, f"{str(i+1).zfill(2)} - {carpetas[0]}")

                    try:
                        shutil.move(ruta_carpeta, nueva_nombre)
                        print(f"Movido: {ruta_carpeta} -> {nueva_nombre}")
                    except Exception as e:
                        print(f"Error moviendo {ruta_carpeta}: {e}")

                    try:
                        shutil.rmtree(ruta_subdirectorio)
                        print(f"Eliminado: {ruta_subdirectorio}")
                    except Exception as e:
                        print(f"Error eliminando {ruta_subdirectorio}: {e}")

    print("Proceso completado.")

def on_key_event(e):
    if e.name == 'p' and e.modifiers == {'ctrl'}:
        seleccionar_directorio()

# Configurar la escucha de eventos de teclado
keyboard.on_press(on_key_event)

# Mantener el script en ejecución
print("Presiona Ctrl + P para seleccionar un directorio.")
keyboard.wait('esc')  # Espera hasta que se presione Esc para terminar el script
