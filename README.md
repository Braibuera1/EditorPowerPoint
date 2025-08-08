[README.md](https://github.com/user-attachments/files/21689910/README.md)
# 📄 Proyecto: Editor Automático de Presentaciones PowerPoint

Este proyecto automatiza el proceso de edición y exportación de presentaciones PowerPoint (`.pptx`) utilizadas en informes o reportes con mapas y observaciones.

## 🧠 Funcionalidades principales

- Eliminación automática de diapositivas iniciales y finales.
- Eliminación de íconos y elementos gráficos innecesarios.
- Exportación de cada diapositiva a imágenes `.jpg`.
- Recorte automático de bordes en las imágenes exportadas.
- Detección automática de cantidad de mapas y observaciones.
- Generación automática del nombre y ruta de destino.

## 📁 Estructura del proyecto

```
.
├── main.py
├── utils/
│   ├── EditorPPTX.py
│   ├── funcionesImagenes.py
│   ├── seleccionar.py
```

## ⚙️ ¿Cómo funciona?

1. Se ejecuta el archivo `main.py`.
2. Se solicita al usuario seleccionar un archivo `.pptx`.
3. Se procesa el archivo mediante `EditorPPTX`, que:
   - Elimina las primeras 4 diapositivas.
   - Elimina las diapositivas finales según la cantidad de mapas.
   - Elimina íconos de video y flechas específicas.
   - Exporta las diapositivas restantes como imágenes.
4. Las imágenes exportadas son procesadas con `Pillow`, recortando bordes superiores o ambos, según correspondan.
5. Las imágenes se guardan automáticamente en una carpeta generada a partir del texto de la primera diapositiva (por ejemplo: `CASO XXXX OBJ XXXX`).

## 🧩 Módulos

### `main.py`
- Punto de entrada del programa.
- Coordina todo el flujo de trabajo.

### `EditorPPTX.py`
- Usa `win32com.client` para manipular PowerPoint.
- Contiene la clase `EditorPPTX` con métodos para:
  - Editar la presentación.
  - Eliminar diapositivas y elementos gráficos.
  - Exportar a imágenes.
  - Contar mapas y observaciones.
  - Extraer texto clave para nombrar carpetas.

### `funcionesImagenes.py`
- Utiliza `PIL` para procesar las imágenes exportadas.
- Recorta bordes según si pertenecen a secciones de mapas u observaciones.

### `seleccionar.py`
- Muestra cuadros de diálogo para elegir archivos o directorios.
- Utiliza `tkinter` con ventanas ocultas para mejorar la experiencia de usuario.

## 🖥️ Requisitos

- Python 
- [pywin32](https://pypi.org/project/pywin32/)
- Pillow

Instalación recomendada:

```bash
pip install pywin32 Pillow
```

## 📝 Ejemplo de uso

```bash
python main.py
```

1. Seleccioná el archivo `.pptx` con el botón que aparece.
2. El sistema procesará automáticamente la presentación.
3. Las imágenes recortadas se guardarán en una carpeta con nombre generado automáticamente.
