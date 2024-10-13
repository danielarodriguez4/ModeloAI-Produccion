# Utiliza una imagen base de Python
FROM python:3.10-slim-buster

# Establece el directorio de trabajo dentro del contenedor como /app. Todos los comandos posteriores se ejecutarán dentro de este directorio.
WORKDIR /app

# Copia todos los archivos y subdirectorios del directorio actual (donde se encuentra el Dockerfile) al directorio de trabajo dentro del contenedor. 
COPY . .

# Instala las dependencias descritas en el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Establece los permisos de ejecución para el script de inicio
RUN chmod +x start.sh

# Establece el comando por defecto que se ejecutará cuando se inicie un contenedor a partir de esta imagen. En este caso, se ejecutará el script Bash /bin/bash y se le pasará como argumento el script start.sh.
CMD ["/bin/bash", "start.sh"]
