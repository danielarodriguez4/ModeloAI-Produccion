## Descripción  

**Fase 3**
- Se configura un nuevo contenedor de Docker.
- Se agrega el script `apirest.py`. Este script implementa una API REST usando Flask para exponer dos funcionalidades principales: entrenamiento de un modelo y generación de predicciones.
- Se agrega el script `client.py`. Este script actúa como un cliente que interactúa con la API REST desplegada por apirest.py.

## Consideraciones

Los archivos `input_data.csv` y `train.csv` se utiliza en diferentes scripts para entrenar el modelo y realizar predicciones, es importante que tus archivos de entrada tengan estos nombres o que actualices los scripts donde se usan:

**Archivo `train.csv`**
Este archivo contiene los datos de entrenamiento para el modelo y aparece en el script `train.py`:
    ``` bash
      data = pd.read_csv('train.csv')  # Carga train.csv
    ```
**Archivo `input_data.csv`**
Este archivo contiene datos de entrada para hacer predicciones y aparece en el script `predict.py`:
    ``` bash
    sys.argv = ['predict.py', '--data_file', 'input_data.csv', '--model_file', 'modelo_entrenado.pkl']
    ```
    
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
      cd Fase 3
    ```
**2. Ejecuta el siguiente comando para crear la imagen de Docker:**
 - Crear la imagen:
     ``` bash
       docker build -t flask-api .
     ```
     
**3. Ejecuta el siguiente comando para levantar el servidor de la API REST en un contenedor:**
 - Esto ejecutará el script `start.sh`, que por defecto levantará la API REST en `http://localhost:5000`.
     ``` bash
       docker run -p 5000:5000 flask-api
     ```

**4. Ejecuta el siguiente comando dentro de la terminal del contenedor para probar la API REST:**
 - Aquí ejecutamos `client.py` localmente para consumir los endpoints para el entrenamiento del modelo
     ``` bash
       python client.py
     ```
- El mismo `client.py` llamará después al endpoint /predict y mostrará las predicciones en consola.

 **5. Ejecuta el siguiente comando para parar el contenedor:**
  - Detener el contenedor:
 ``` bash
   docker stop flask-api .
 ```
---------------------------------------------------------------------------------------------------
**Notas:**
- Modelo Entrenado: Se guardará como `modelo_entrenado.pkl`.
- Predicciones: Se guardarán en `predicciones.csv` y se mostrarán en las respuestas de la API.
