María Daniela Rodríguez Chacón

# Modelo AI en producción

- **Fase 1**:
    - Se escoge una competencia de Kaggle relacionada con transporte personal. Para este proyecto, se escogió la competición **Bike Sharing Demand**, donde se pide a los participantes que combinen patrones de uso históricos con datos meteorológicos para pronosticar la demanda de alquiler de bicicletas en el programa Capital Bikeshare en Washington, D.C.
      Enlace al Kaggle: https://www.kaggle.com/competitions/bike-sharing-demand/overview 
    - En este caso, se replica el modelo predictivo del usuario bike_sharing_demand
      
 - **Fase 2**:
    - Se configura un contenedor de Docker.
    - Se crea una imagen dentro del contenedor de Docker.
    - Se añaden los scripts `train.py`, `predict.py` para entrenamiento y predicción del modelo, y `start.sh` para ejecutar el train y predict dentro del contenedor de Docker.
    - Se añade el script `01 - generate data and model.py` para generar datos sintéticos.
    - Se añade el script `02 - run scripts.py` para cargar los archivos generados en los scripts `train.py` y `predict.py`.

 - **Fase 3**:
    - Se configura un nuevo contenedor de Docker.
    - Se agrega el script `apirest.py`. Este script implementa una API REST usando Flask para exponer dos funcionalidades principales: entrenamiento de un modelo y generación de predicciones.
    - Se agrega el script `client.py`. Este script actúa como un cliente que interactúa con la API REST desplegada por apirest.py.


## ¿Cómo ejecutar?

  Para detalles sobre cómo ejecutar cada fase, revisar el README.md de cada carpeta. 

## Estructura del proyecto
```bash
  ModeloAI-Produccion/
  ├── Fase 1
  │   ├── fase_1.pynb
  │   ├── train.csv
  │   ├── test.csv
  │   ├── README.md
  ├── Fase 2
  │   ├── scripts
  │       ├── train.py
  │       ├── predict.py
  │       ├── start.sh
  │       ├── train.csv
  │   ├── Dockerfile
  │   ├── requirements.txt
  │   ├── 01_generate_data_and_model.py
  │   ├── 02_run_scripts.py
  │   ├── README.md
  ├── Fase 3
  │   ├── scripts
  │       ├── train.py
  │       ├── predict.py
  │       ├── start.sh
  │       ├── client.py
  │       ├── apirest.py
  │   ├── Dockerfile
  │   ├── requirements.txt
  │   ├── README.md
```


