import streamlit as st
import requests
import base64

# URL del endpoint de FastAPI
url = "http://127.0.0.1:8000/recomendacion"

# Estilo para agregar el fondo
st.markdown(
    """
    <style>
    /* Fondo de toda la página */
    .stApp {
        background-color: #2b4b82;
    }
    /* Color del texto */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título y subtítulo centrados
st.markdown('<h1 class="title" style="color:white;">XplorIA</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">¡Bienvenido a XplorIA! ¡Planes donde sea, cuando sea!</p>', unsafe_allow_html=True)

# Pregunta más grande y centrada justo encima de la caja de texto
consulta_usuario = st.text_input("¿Qué plan buscas hoy?", "")

# Botón de búsqueda centrado
if st.button("¡Explora!", key="recomendacion_btn"):
    if consulta_usuario:
        data = {"consulta": consulta_usuario}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            recomendacion = response.json()
            st.markdown(
                f'<div style="background-color: black; color: white; padding: 10px; border-radius: 5px;">'
                f'Recomendación: {recomendacion}'
                f'</div>',
                unsafe_allow_html=True
            )
        else:
            st.error("Hubo un error al obtener la recomendación.")
    else:
        st.warning("Por favor ingresa una consulta.")
