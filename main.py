from PIL import Image
import streamlit as st
import io

OUTPUT_NAME = "ImagenPDF.pdf"

uploaded_files = st.file_uploader(
    "Escoge archivos",
    accept_multiple_files=True)

if len(uploaded_files) > 0:
    try:
        images = []
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            img = Image.open(
                io.BytesIO(bytes_data))
            img = img.convert('RGB')
            images.append(img)

        images[0].save(
            OUTPUT_NAME,
            save_all=True,
            append_images=images[1:]
        )

        with open(OUTPUT_NAME, 'rb') as archivo:
            st.download_button(
                label="Descargar",
                file_name=OUTPUT_NAME,
                data=archivo
            )
    except Exception as e:
        st.title("Error al descargar")
