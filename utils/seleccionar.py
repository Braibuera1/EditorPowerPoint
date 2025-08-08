from tkinter import filedialog
import tkinter as tk

def seleccionar_directorio():
    # Crear una ventana oculta
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    folder = filedialog.askdirectory(title="Guardar en..")
    if not folder:
        return 
    else:
        return folder.replace("/","\\")
    

def seleccionar_proyecto():    
    # Crear una ventana oculta
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    archivo_pptx = filedialog.askopenfilename(
        title="Selecciona un archivo PowerPoint",
        filetypes=[("PowerPoint files", "*.pptx")]
    )
    if not archivo_pptx:
        return
    return archivo_pptx.replace("/","\\")


