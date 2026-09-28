# Image Contrast Stretching OpenCV

Script en **Python** enfocado en el procesamiento digital de imágenes utilizando **OpenCV** y **NumPy**. Implementa una técnica de estiramiento de contraste y corrección de intensidad recortando valores de píxeles fuera de un rango específico y normalizando el resultado al espectro completo de 8 bits (0-255).

---

## 🚀 Características

- **Carga y Guardado de Imágenes:** Manejo de archivos de imagen con las funciones nativas `cv2.imread` y `cv2.imwrite`.
- **Ajuste de Intensidad (Clipping):** Limitación de píxeles mediante `.clip()` dentro de los rangos mínimo (`i_min = 10`) y máximo (`i_max = 80`).
- **Normalización Matemática:** Escalamiento lineal de matriz para redistribuir la intensidad en la escala de 0 a 1.
- **Transformación de Rango:** Reescalamiento a valores discretos de color en formato de entero de 8 bits (`0-255`).

---

## 📂 Estructura del Proyecto

```text
Image-Contrast-Stretching-OpenCV/
│
├── main.py                     # Script de procesamiento de imagen
├── img3_E13.jpg                # Imagen original
└── img3_corregida_E13.jpg      # Imagen procesada con contraste ajustado
