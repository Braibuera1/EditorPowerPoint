import tkinter as tk
from tkinter import filedialog

def seleccionar_directorio(ruta_predeterminada):
    """Muestra una ventana con una ruta editable y permite cambiarla mediante un botón o escribiéndola directamente."""
    def cambiar_ruta():
        """Permite al usuario seleccionar un nuevo directorio desde un cuadro de diálogo."""
        nueva_ruta = filedialog.askdirectory(title="Selecciona un nuevo directorio")
        if nueva_ruta:
            entrada_ruta.delete(0, tk.END)  # Borra el contenido actual
            entrada_ruta.insert(0, nueva_ruta)  # Inserta la nueva ruta seleccionada

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Seleccionar Directorio")
    ventana.geometry("500x200")

    # Etiqueta de instrucción
    etiqueta_instruccion = tk.Label(ventana, text="Ruta del directorio:")
    etiqueta_instruccion.pack(pady=5)

    # Campo de texto para mostrar y editar la ruta
    entrada_ruta = tk.Entry(ventana, width=60)
    entrada_ruta.insert(0, ruta_predeterminada)  # Ruta predeterminada
    entrada_ruta.pack(pady=5)

    # Botón para abrir el cuadro de diálogo y seleccionar el directorio
    boton_cambiar = tk.Button(ventana, text="Seleccionar Carpeta", command=cambiar_ruta)
    boton_cambiar.pack(pady=10)

    # Botón para confirmar la selección
    boton_confirmar = tk.Button(ventana, text="Confirmar", command=ventana.quit)
    boton_confirmar.pack(pady=10)

    # Iniciar el bucle principal
    ventana.mainloop()

    # Obtener la ruta final ingresada o seleccionada
    ruta_final = entrada_ruta.get()
    ventana.destroy()  # Cerrar la ventana
    return ruta_final

# Uso de la función con una ruta predeterminada
ruta_predeterminada = "C:/Users/Usuario/Documentos"
ruta_seleccionada = seleccionar_directorio(ruta_predeterminada)
print(f"Ruta seleccionada: {ruta_seleccionada}")
