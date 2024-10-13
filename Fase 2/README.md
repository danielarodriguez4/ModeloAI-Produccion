
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
  
**Prerrequisitos para seguir la guía**
- Asegúrate de tener Docker instalado correctamente un tu computador. (página para descarga: https://docs.docker.com/get-docker/).
- Este instructivo funciona en Windows.
- La versión de Python usada es 3.10, corresponde a la versión de Google Colab.
- Git para clonar el repositorio.
  
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
**2. Ejecuta el siguiente comando para crear la imagen de Docker:**
 - Crear la imagen:
     ``` bash
       docker build -t modelo-produccion .
     ```
     
**3. Ejecuta el siguiente comando para crear y ejecutar el contenedor:**
 - Crear y ejecutar el contenedor:
     ``` bash
       docker run -it --name contenedor modelo-produccion
     ```

**4. Ejecuta el siguiente comando dentro de la terminal del contenedor para escoger el script que desees correr:**
 - Script a correr
     ``` bash
       ./start.sh
     ```
 - **Nota:** primero debes ejecutar el `train.py` y luego el `predict.py`, ya que predict depende de los resultados de train.

 **5. Ejecuta el siguiente comando para parar el contenedor:**
  - Detener el contenedor:
 ``` bash
   docker stop modelo-produccion
 ```

## Pruebas con los scripts `01 - generate data and model.py` y `02 - run scripts.py`.
- Corre el script `train.py` para entrenar un modelo de regresión lineal basado en el "train.csv" del modelo inicial.
- Abre el script `predict.py`.
- Carga el archivo `modelo_entrenado.pkl` para generar predicciones usando el modelo pre-entrenado generado en el punto anterior.
- Una vez generadas las predicciones, cárgalas en `01 - generate data and model.py` y corre el código.
- Carga el archivo `predicciones.csv`, `test_new_data.csv` y train_new_data.csv` en el `02 - run scripts.py` y corre el código para obtener el nuevo modelo entrenado.
