# Utiliza una imagen base de Python
FROM python:3.10-slim-buster

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Otorga permisos de ejecución a start.sh
RUN chmod +x start.sh

# Comando por defecto para iniciar el contenedor
CMD ["/bin/bash", "start.sh"]
