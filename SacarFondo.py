import streamlit as st  # Importa la biblioteca Streamlit para crear la interfaz web
from PIL import Image  # Importa la clase Image de la biblioteca PIL (Python Imaging Library)
from rembg import remove  # Importa la función 'remove' del paquete 'rembg' para quitar fondos de imágenes
import io  # Importa la biblioteca 'io' para trabajar con datos en memoria
import os  # Importa la biblioteca 'os' para realizar operaciones con el sistema operativo

# ----FUNCTIONS----

def remove_background(image):
    # Crea un objeto de BytesIO para almacenar la imagen en memoria
    image_byte = io.BytesIO()

    # Guarda la imagen en formato PNG en el objeto BytesIO
    image.save(image_byte, format="PNG")

    # Establece la posición en el objeto BytesIO al inicio
    image_byte.seek(0)

    # Elimina el fondo de la imagen utilizando la función 'remove' de rembg
    processed_image_bytes = remove(image_byte.read())

    # Crea una nueva imagen PIL a partir de los bytes de la imagen procesada
    return Image.open(io.BytesIO(processed_image_bytes))


def process_image(image_uploaded):
    # Abre la imagen cargada
    image = Image.open(image_uploaded)

    # Procesa la imagen para quitar el fondo
    processed_imagen = remove_background(image)
    return processed_imagen


#----FRONT----
st.image("assets/auto.webp", width=400)  # Muestra una imagen en la interfaz de usuario
st.header("¡Bienvenido a la Aplicación para Eliminar Fondos!")  # Muestra un encabezado en la interfaz
st.subheader("Sube una imagen para eliminar su fondo")  # Muestra un subencabezado en la interfaz

uploaded_image = st.file_uploader("Seleccione una imagen para cargar (formatos admitidos: JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])  # Permite al usuario cargar una imagen

if uploaded_image is not None:
    # Comprueba si se ha cargado una imagen
    st.image(uploaded_image, caption="Aquí está la imagen que subiste:", use_column_width=True)  # Muestra la imagen cargada en la interfaz
    remove_button = st.button(label="Quitar fondo")  # Crea un botón llamado "Quitar fondo"
    
    if remove_button:
    # Comprueba si se ha hecho clic en el botón "Quitar fondo"
        processed_image = process_image(uploaded_image)  # Procesa la imagen para quitar el fondo
        st.image(processed_image, caption="¡Fondo eliminado con éxito!", use_column_width=True)  # Muestra la imagen con el fondo eliminado en la interfaz
        processed_image.save("processed_image.png")  # Guarda la imagen procesada en un archivo llamado "processed_image.png"
        with open("processed_image.png", "rb") as f:
            image_data = f.read()  # Lee los datos de la imagen procesada

        st.download_button("Haz clic aquí para descargar la imagen", data=image_data, file_name="processed_image.png")  # Muestra un botón de descarga para que el usuario pueda descargar la imagen procesada

        os.remove("processed_image.png")  # Elimina el archivo temporal de la imagen procesada del sistema operativo



# Pie de página con enlace a LinkedIn
st.markdown("""
---
#### Desarrollado por [Luis Ponce de León](https://www.linkedin.com/in/jponcedeleon/)
Sígueme en [LinkedIn](https://www.linkedin.com/in/jponcedeleon/) para más proyectos como este.
""", unsafe_allow_html=True)