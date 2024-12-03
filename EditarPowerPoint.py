from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE 


# Definir la ubicación específica para eliminar la tabla
ubicacion_deseada = {
    'left': 3391,  # Reemplaza con el valor deseado en EMUs (1 punto = 12700 EMUs)
    'top': -27384,   # Reemplaza con el valor deseado en EMUs
    'width': 9140610, # Reemplaza con el valor deseado en EMUs
    'height': 655320 # Reemplaza con el valor deseado en EMUs
}

# Definir las dimensiones específicas para eliminar la imagen
dimensiones_deseadas = {
    'width': 708571,  # Reemplaza con el valor deseado en EMUs
    'height': 656136  # Reemplaza con el valor deseado en EMUs
}


def quitarElementos(archivo_pptx):
    # Cargar la presentación
    if archivo_pptx:
        presentation = Presentation(archivo_pptx)
        # Palabras clave a buscar
        palabras_clave = ["Resultado", "Mapa", "Siguiente", "Observaciones", "Información", "Anterior"]

        # Recorrer las diapositivas
        for slide in presentation.slides:
            # Identificar cuadros de texto para eliminar
            for shape in slide.shapes:
                if shape.has_table:
                    # Obtener la posición y dimensiones de la tabla
                    left = shape.left
                    top = shape.top
                    width = shape.width
                    height = shape.height
                    
                    # Verificar si la tabla está en la ubicación deseada
                    if ((left == ubicacion_deseada['left'] and
                        top == ubicacion_deseada['top'] and
                        width == ubicacion_deseada['width'] and
                        height == ubicacion_deseada['height'])or(shape.table.cell(0, 0).text == "IMAGEN")):
                        sp = shape
                        sp._element.getparent().remove(sp._element)
                        
                if shape.shape_type == 13:  # 13 indica una imagen
                    # Obtener las dimensiones de la imagen
                    width = shape.width
                    height = shape.height
                    
                    # Verificar si las dimensiones coinciden con las deseadas
                    if width == dimensiones_deseadas['width'] and height == dimensiones_deseadas['height']:
                        # Eliminar la imagen
                        sp = shape
                        sp._element.getparent().remove(sp._element)  
                
                if shape.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE:
                    if shape.has_text_frame:   
                        texto = shape.text_frame.text.strip()
                        if any(palabra in texto for palabra in palabras_clave):
                            sp = shape
                            sp._element.getparent().remove(sp._element) 

        # Guardar los cambios en el mismo archivo
        presentation.save(archivo_pptx)
        print("Tablas y elementos eliminados. Archivo guardado.")
    else:
        print("No se seleccionó ningún archivo.")
