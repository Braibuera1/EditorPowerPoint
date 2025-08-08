from utils.seleccionar import seleccionar_proyecto, seleccionar_directorio
from utils.EditorPPTX import EditorPPTX
from utils.funcionesImagenes import recortar_bordes
from tkinter import messagebox

class FileValidationError(Exception):
    """Excepción base para errores de validación de archivos"""
    pass

def mensajeError(e):
    messagebox.showerror("Interrupción", e)

if __name__ == "__main__":

    try:
        
        archivo_pptx = seleccionar_proyecto()

        if not archivo_pptx :
            raise TypeError("No ha seleccionado un caso")
        
        #ruta_destino = seleccionar_directorio()

        #if not ruta_destino:
        #    raise TypeError("No ha seleccionado una carpeta destino")
        
        editor = EditorPPTX(archivo_pptx)
        editor.editarPPTX()
        recortar_bordes(editor.ruta_destino, editor.cant_mapas)

    except (TypeError,FileValidationError) as e:
        mensajeError(e)