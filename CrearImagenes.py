import os
import win32com.client

def powerpoint_to_images(pptx_path, output_folder):
    # Crear instancia de PowerPoint
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    
    # Abrir la presentación en modo de solo lectura
    presentation = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
    
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Exportar cada diapositiva como imagen JPG
    for slide_index, slide in enumerate(presentation.Slides, start=1):
        output_path = os.path.join(output_folder, f"{slide_index}.jpg")
        slide.Export(output_path, "JPG")
        print(f"Diapositiva {slide_index} exportada a: {output_path}")
    
    # Cerrar la presentación y PowerPoint
    presentation.Close()
    powerpoint.Quit()








