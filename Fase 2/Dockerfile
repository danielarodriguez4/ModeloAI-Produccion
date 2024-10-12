# Usar una imagen base de Python 3
FROM python:3.9-slim-buster

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt
COPY train.py train.py
COPY predict.py predict.py

# Instalar las dependencias desde requirements.txt
RUN pip install -r requirements.txt

# Comando por defecto para ejecutar el script de entrenamiento o predicción
CMD ["bash", "start.sh"]
