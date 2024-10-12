# Utiliza una imagen base de Python
FROM python:3.9-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt ./
COPY train.py ./
COPY predict.py ./
COPY fase_1.py ./
COPY start.sh ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establece los permisos de ejecución para el script de inicio
RUN chmod +x start.sh

# Comando por defecto al ejecutar el contenedor
CMD ["/bin/bash", "start.sh"]
