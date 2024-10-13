# Utiliza una imagen base de Python
FROM python:3.9-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos que se encuentren al mismo nivel del repositorio que el Dockerfile
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establece los permisos de ejecución para el script de inicio
RUN chmod +x start.sh

# Comando por defecto al ejecutar el contenedor
CMD ["/bin/bash", "start.sh"]
