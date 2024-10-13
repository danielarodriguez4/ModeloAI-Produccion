
# Descripción  

 - **Fase 2**:
    - Se configura un contenedor Docker.
    - Se añade el script `01 - generate data and model.py` para generar datos sintéticos.
    - Se añade el script `02 - run scripts.py` para cargar los archivos generados en los scripts `train.py` y `predict.py`.
        **Nota:** estos dos scripts se añaden para hacer pruebas con los los scripts `train.py` y `predict.py`.
      
    - Se añade `train.py` a la carpeta `scripts` para entrenar un nuevo modelo de regresión lineal y guardarlo.
      - Para ejecutar este script, se debe cargar en el entorno el archivo "train.csv" de la carpeta "Fase 1" de este proyecto.
      - Este script genera un archivo llamado `modelo_entrenado.pkl`.
    - Se añade `predict.py` a la carpeta `scripts` para generar una predicción para cada dato de entrada.
      - Para ejecutar este script, se debe cargar en el entorno el archivo `modelo_entrenado.pkl` generado en el punto anterior y también el archivo "train.csv" de la carpeta "Fase 1" de este proyecto.
    - Se añade `start.sh` a la carpeta `scripts` para ejecutar el script `train.py` o `predict.py` dependiendo del caso.


## ¿Cómo ejecutar?
  
- **Fase 2. Configuración de un contenedor de Docker**
   Antes de iniciar, asegúrate de tener Docker instalado correctamente un tu computador. (página para descarga: https://docs.docker.com/get-docker/)
 **1. Clona el repositorio:**
  - Abre tu terminal o lìnea de comandos.
  - Navega hasta alguna carpeta donde quieras clonar el repositorio. Puedes usar el comando "cd" para hacerlo.
  - Ejecuta los siguientes comandos:
     ``` bash
       git clone https://github.com/danielarodriguez4/ModeloAI-Produccion.git
     ```
     ``` bash
       cd "carpeta-donde-clonaste-el-repositorio"/ModeloAI-Produccion
     ```
     ``` bash
       cd Fase 2
     ```
**2. Ejecuta los siguientes comandos para crear la imagen de Docker y correr los scripts:**
- Para crear la imagen:
     ``` bash
       docker build -t modelo-produccion .
     ```
- Para ejecutar el script de entrenamiento: 
     ``` bash
       docker run -it modelo-produccion train
     ```
- Para ejecutar el script de predicciones:
     ``` bash
       docker run -it modelo-produccion predict
     ```

 **3. Ejecuta el siguiente comando para parar el contenedor cuando desees detenerlo:**
 ``` bash
   docker stop modelo-produccion
 ```

## Pruebas con los scripts `01 - generate data and model.py` y `02 - run scripts.py`.
- Corre el script `train.py` para entrenar un modelo de regresión lineal basado en el "train.csv" del modelo inicial.
- Abre el script `predict.py`.
- Carga el archivo `modelo_entrenado.pkl` para generar predicciones usando el modelo pre-entrenado generado en el punto anterior.
- Una vez generadas las predicciones, cárgalas en `01 - generate data and model.py` y corre el código.
- Carga el archivo `predicciones.csv`, `test_new_data.csv` y train_new_data.csv` en el `02 - run scripts.py` y corre el código para obtener el nuevo modelo entrenado.
