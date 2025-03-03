# Utilizar una imagen de Phthon oficial
FROM python:3.10-slim

# Establecer el directorio del contenedor
WORKDIR /app

# Copiamos todos los archivos al directorio del contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que la aplicación va a correr en el contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación
#CMD ["bash", "-c", "python api_model.py --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501"]do
CMD ["sh", "-c", "uvicorn api_model:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port=8501"]
