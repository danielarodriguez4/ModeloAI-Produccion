María Daniela Rodríguez Chacón

# Modelo AI en producción

- **Fase 1**:
    - Se escoge una competencia de Kaggle relacionada con transporte personal. Para este proyecto, se escogió la competición **Bike Sharing Demand**, donde se pide a los participantes que combinen patrones de uso históricos con datos meteorológicos para pronosticar la demanda de alquiler de bicicletas en el programa Capital Bikeshare en Washington, D.C.
      Enlace al Kaggle: https://www.kaggle.com/competitions/bike-sharing-demand/overview 
    - En este caso, se replica el modelo predictivo del usuario bike_sharing_demand
      
 - **Fase 2**:


# ¿Cómo ejecutar?
- **Fase 1**: 
    - Descargar los archivos test.csv y train.csv.
    - Seleccionar y abrir el colab "fase-1.pynb".
    - Cargar los archivos al colab y correr cada celda para obtener las predicciones.
  
- **Fase 2**
    - Corre el script "train.py" para entrenar un modelo de regresión lineal basado en el "train.csv" del modelo inicial.
    - Abre el scrpt "predict.py".
    - Carga el archivo "modelo_entrenado.pkl" para generar predicciones usando el modelo pre-entrenado generado en el punto anterior.
    - Una vez generadas las predicciones, corre el archivo 01 - generate data and model
