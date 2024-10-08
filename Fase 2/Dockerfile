# Usar una imagen base de Python 3
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt ./

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación al contenedor
COPY . .

# Comando por defecto para ejecutar el script de entrenamiento o predicción
CMD ["python", "train.py"]
CMD ["python", "predict.py"] 
