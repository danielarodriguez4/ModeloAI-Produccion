
# Descripción  

 - **Fase 2**:
    - Se configura un contenedor Docker para 
    - Se añade el script `01 - generate data and model.py` para generar datos sintéticos.
    - Se añade el script `02 - run scripts.py` para cargar los archivos generados en los scripts `train.py` y `predict.py`.
    - Se añade `train.py` a la carpeta `scripts` para entrenar un nuevo modelo y guardarlo.
    - Se añade `predict.py` a la carpeta `scripts` para generar una predicción para cada dato de entrada, usando un modelo previamente creado en el script `train.py`.
    - Se añade `start.sh` a la carpeta `scripts` para ejecutar el script `train.py` o `predict.py` dependiendo del caso.
 **Nota:** estos dos scripts se añaden para hacer pruebas con los los scripts `train.py` y `predict.py`.

# ¿Cómo ejecutar?
  
- **Fase 2. Configuración de un contenedor de Docker**
-  Antes de iniciar, asegúrate de tener Docker instalado correctamente un tu computador. (página para descarga: https://docs.docker.com/get-docker/)
    - Descargar el contenido del archivo `Dockerfile` y los tres archivos dentro de la carpeta `scripts`.
    - Abrir la terminal y navegar hasta el directorio donde quedó guardado el `Dockerfile`. Puedes navegar utilizando el comando `cd`. 
    - Ejecutar el comando `docker build -t modelo-ia .` en la terminal para construir la imagen. Puedes sustituir "modelo-ia" por el nombre que prefieras para la imagen.
    - Para entrenar el modelo, ejecuta el comando `docker run -it --rm mi-modelo train`.
    - Luego, para las predicciones ejecuta el comando `docker run -it --rm mi-modelo predict`.

# Pruebas con los scripts `01 - generate data and model.py` y `02 - run scripts.py`
    - Corre el script `train.py` para entrenar un modelo de regresión lineal basado en el "train.csv" del modelo inicial.
    - Abre el script `predict.py`.
    - Carga el archivo `modelo_entrenado.pkl` para generar predicciones usando el modelo pre-entrenado generado en el punto anterior.
    - Una vez generadas las predicciones, cárgalas en `01 - generate data and model.py` y corre el código.
    - Carga el archivo `predicciones.csv`, `test_new_data.csv` y train_new_data.csv` en el `02 - run scripts.py` y corre el código para obtener el nuevo modelo entrenado.
