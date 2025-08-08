import win32com.client
import os
from data.rutas import RUTA_DESTINO
from .seleccionar import seleccionar_directorio


class EditorPPTX:
    
    # Crear instancia de PowerPoint
    def __init__(self, archivo_pptx):
        self.archivo_pptx = archivo_pptx
        # Crear instancia de PowerPoint
        self.powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        # Abrir la presentación en modo de solo lectura
        self.presentation = self.powerpoint.Presentations.Open(self.archivo_pptx, WithWindow=False)
        #Cantidad de mapas
        self.cant_mapas = self.contar_mapas()
        #Cantidad de diapositivas de observaciones
        self.cant_observaciones = self.contar_observaciones()
        # Seleccionar destino 
        self.ruta_destino = RUTA_DESTINO + f"\\CASO " + self.obtenertextos() + " OBJ XXXX" 



    def editarPPTX(self):
        self.eliminar_diapositivas()
        self.quitarIconoVideo()
        self.powerpoint_to_images()
        # Cierra la presentación
        self.presentation.Close()
        # Cierra PowerPoint
        self.powerpoint.Quit()



    def eliminar_diapositivas(self):
        #Eliminar primeras 4 diapostivas
        for indice in sorted(range(1,5),reverse=True):
            self.presentation.Slides(indice).Delete()

        #Total de diapositivas
        totalDiapositivas = self.presentation.Slides.count
        for indice in range(totalDiapositivas,totalDiapositivas-self.cant_mapas,-1):
            self.presentation.Slides(indice).Delete()



    def quitarIconoVideo(self):

        contador = self.cant_mapas
        lista_borrar = []
        icono_video = {
            "width": 
            {
                "min":54,
                "max":58
            },
            "height": 
            {
                "min":50,
                "max":54
            }
        }

        flechas = {
            "width": 
            {
                "min":88,
                "max":92
            },
            "height": 
            {
                "min":55,
                "max":59
            }
        }
        # Recorrer las diapositivas
        for slide in self.presentation.Slides:
            # Identificar cuadros de texto para eliminar
            for shape in slide.Shapes:
                if contador > 0:
                    if  flechas["width"]["min"] <= round(shape.Width) <= flechas["width"]["max"] and flechas["height"]["min"] <= round(shape.Height) <= flechas["height"]["max"]:
                        #print(f"WIDTH: {round(shape.Width)} - HEIGHT: {round(shape.Height)} - {shape.Name}")
                        lista_borrar.append(shape)

                if shape.Type == 13:  # 19 indica imagen 
                    #print(f"WIDTH: {round(shape.Width)} - HEIGHT: {round(shape.Height)} - {shape.Name}")
                    if  icono_video["width"]["min"] <= round(shape.Width) <= icono_video["width"]["max"] and icono_video["height"]["min"] <= round(shape.Height) <= icono_video["height"]["max"]:
                        #print(f"WIDTH: {round(shape.Width)} - HEIGHT: {round(shape.Height)} - {shape.Name}")
                        lista_borrar.append(shape)
            contador -= 1
                    

                    

        for s in lista_borrar:
            s.Delete()             
        print(f"Tablas y elementos eliminados. Archivo guardado.")



    def powerpoint_to_images(self):
        contador = self.cant_mapas
        # Crear la carpeta de salida si no existe
        if not os.path.exists(self.ruta_destino):
            os.makedirs(self.ruta_destino)
        
        # Exportar cada diapositiva como imagen JPG
        for slide_index, slide in enumerate(self.presentation.Slides, start = 0):
            output_path = os.path.join(self.ruta_destino, 
                                       f"{self.presentation.Slides.count-contador+1}.jpg" 
                                       if  contador > 0
                                       else f"{slide_index-self.cant_mapas+1}.jpg")
            slide.Export(output_path, "JPG")
            print(f"Diapositiva {slide_index+1} exportada a: {output_path}")
            contador -= 1 


    def contar_mapas(self):
        # Convertir cm a puntos
        cant_mapas = 0
        for slide in self.presentation.Slides:
            for shape in slide.Shapes:
                if shape.Type == 17 and shape.TextFrame.HasText:
                    if "MAPA" in shape.TextFrame.TextRange.Text:
                        cant_mapas += 1
                        break
        return cant_mapas       

    def contar_observaciones(self):
        # Convertir cm a puntos
        obs_cant = 0
        for slide in self.presentation.Slides:
            for shape in slide.Shapes:
                if shape.Type == 17 and shape.TextFrame.HasText:
                    if "OBSERVACIONES" in shape.TextFrame.TextRange.Text:
                        obs_cant += 1
                        break
        return obs_cant

    def obtenertextos(self):
  
        for shape in self.presentation.Slides(1).Shapes:
            if shape.Type == 17 and shape.TextFrame.HasText and "Caso" in (shape.TextFrame.TextRange.Text):
                texto = shape.TextFrame.TextRange.Text.split(":")
        return texto[len(texto)-1]